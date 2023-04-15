#include <TinyGPS++.h>

#define MAX_PACKETS_TO_BE_CACHED 1

#define TIME_BETWEEN_GPS_PACKETS_MS 1000

//---------------------------------
//pins
#define BUSY_PIN 8

#define REAR_PIN 2
#define FRONT_LEFT_PIN 3
#define FRONT_RIGHT_PIN 18

//---------------------------------
//config
#define DIAGNOSTICS 1

#define SEND_FAKE_GPS 1
//---------------------------------
//suspension
const int analogInPin[4] = {A0, A1, A2, A3};  // Analog input pin that the potentiometer is attached to

//---------------------------------
//gps
TinyGPSPlus gps;

unsigned long oldtime = 0;
unsigned long newtime;


//---------------------------------
//rpms
volatile int rear_count, front_left_count, front_right_count;


//---------------------------------

typedef enum
{   
    SEND_DATA,
    WAIT_TO_SEND,
    COLLECT_DATA
}States_t;

States_t state;

//---------------------------------
//binary stuff

const byte FrameStart=0xfa;
const byte FrameEnd=0xfb;
const byte FrameESC=0xfc;
//const byte FrameZero=0x00;

union {
    uint32_t bytes;
    float float_part;
}float_to_bytes;

struct datapacket_struct  {
  uint8_t datapackage_type;
  uint16_t front_right; //int 2 bytes
  uint16_t front_left; // 4
  uint16_t back_right; // 6
  uint16_t back_left; // 8
  
  uint16_t rear_rpm; //10
  uint16_t front_left_rpm; //12
  uint16_t front_right_rpm; // 14

//  uint16_t test; // 16


  uint32_t gps_latitude; //floats 4 bytes, 18
  uint32_t gps_longtitude; //22
  uint32_t gps_speed; //26
};

datapacket_struct dps[MAX_PACKETS_TO_BE_CACHED];


//---------------------------------

int num_of_datapackets = 0;

int byte_count = 0;

void get_new_datapacket();

void switch_state();

//---------------------------------
//data collecting functions

void suspension(struct datapacket_struct *);

void gps_data(struct datapacket_struct *);

void gps_fill_with_empty(struct datapacket_struct *datapacket);

void rpms(struct datapacket_struct *);

void rear_rpm_inc(); void front_left_rpm_inc(); void front_right_rpm_inc(); 

//---------------------------------
//other
void send_datapacket();

void sendoverserial();

void print_datapackets();

//---------------------------------

void setup() {
  ADCSRA &= ~(bit (ADPS0) | bit (ADPS1) | bit (ADPS2)); // clear prescaler bits
  
  // uncomment as required
  
//  ADCSRA |= bit (ADPS0);                               //   2  
//  ADCSRA |= bit (ADPS1);                               //   4  
//  ADCSRA |= bit (ADPS0) | bit (ADPS1);                 //   8  
//  ADCSRA |= bit (ADPS2);                               //  16 
//  ADCSRA |= bit (ADPS0) | bit (ADPS2);                 //  32 
//  ADCSRA |= bit (ADPS1) | bit (ADPS2);                 //  64 
  
  ADCSRA |= bit (ADPS0) | bit (ADPS1) | bit (ADPS2);   // 128
  
  Serial.begin(115200); //monitor, only for diagnostics
  
  Serial1.begin(9600); //gps
  
  Serial2.begin(57600); //data out

  pinMode(BUSY_PIN, INPUT);

  attachInterrupt(digitalPinToInterrupt(REAR_PIN), rear_rpm_inc, FALLING);
  attachInterrupt(digitalPinToInterrupt(FRONT_LEFT_PIN), front_left_rpm_inc, FALLING);
  attachInterrupt(digitalPinToInterrupt(FRONT_RIGHT_PIN), front_right_rpm_inc, FALLING);



  state = COLLECT_DATA;

  
}

void loop() {
  delay(analogRead(A14));
  
  switch(state) {
    case(COLLECT_DATA):
      
      get_new_datapacket();
      
      #ifdef DIAGNOSTICS
      Serial.println("COLLECTING");
      #endif
      break;
      
    case(SEND_DATA):
      #ifdef DIAGNOSTICS
      Serial.println("SENDING");     
      #endif
      
      send_datapacket();
      num_of_datapackets = 0;
      break;
    case(WAIT_TO_SEND):
      Serial.println("WAITING TO SEND");
      Serial.println(digitalRead(BUSY_PIN));
      break;
    
   }
  
  switch_state();

  
}

void get_new_datapacket() {
  //unsigned long newtime = millis();
  
  datapacket_struct dp;
  dp.datapackage_type = 1;
  suspension(&dp);

  /*
  if (newtime - oldtime > TIME_BETWEEN_GPS_PACKETS_MS) {
    gps_data(&dp, false);
    }
  else {
    gps_data(&dp, true);
    }
    */
  gps_fill_with_empty(&dp);

  rpms(&dp);

  dps[num_of_datapackets] = dp;
  

  num_of_datapackets++;
  
}

void switch_state() {
  #ifdef DIAGNOSTICS  
  Serial.println(digitalRead(BUSY_PIN));
  #endif
  if (digitalRead(BUSY_PIN) && num_of_datapackets != 0) {
    
    state = SEND_DATA;
    
    }
  else{
    if (num_of_datapackets == MAX_PACKETS_TO_BE_CACHED) {

      state = WAIT_TO_SEND;
    }
    else state = COLLECT_DATA;
  }
  
}

void suspension(struct datapacket_struct *datapacket) {

  for (int i = 0; i < 4; i++) {

    int t = analogRead(analogInPin[i]);    
    
    switch(i) {
      case(0):  
        datapacket->front_right = t;
        break;
      case(1):  
        datapacket->front_left = t;
        break;
      case(2):  
        datapacket->back_right = t;
        break;
      case(3):
        datapacket->back_left = t;
        break;
      }
  }  
    
}


void gps_fill_with_empty(struct datapacket_struct *datapacket) {
  float lat_ = 40.04036000;
  float long_ = 76.106712;
  float speed_ = 69.0000;

  memcpy(&(datapacket->gps_latitude), &lat_, sizeof(datapacket->gps_latitude));
  memcpy(&(datapacket->gps_longtitude), &long_, sizeof(datapacket->gps_longtitude));
  memcpy(&(datapacket->gps_speed), &speed_, sizeof(datapacket->gps_speed));


  return;
 }
 
/* 
void gps_data(struct datapacket_struct *datapacket) {


    
  if (SEND_FAKE_GPS) {
    datapacket->gps_latitude = 32.236750;
    datapacket->gps_longtitude = 110.952167;
    datapacket->gps_speed = 3.4028235;
    }
  else {
    
    while (Serial1.available() > 0){
      
    gps.encode(Serial1.read());

    if (gps.location.isValid()) {
      
      if (gps.location.isUpdated()){
        datapacket->gps_latitude = gps.location.lat();
        datapacket->gps_longtitude = gps.location.lng();
        datapacket->gps_speed = gps.speed.mph();
        }
      
      }
       
    }
    
  }  
   
}
*/

void rear_rpm_inc() {
  rear_count++;
  } 
  
void front_left_rpm_inc() {
  front_left_count++;
  } 
  
void front_right_rpm_inc() {
  front_right_count++;
  }

void rpms(struct datapacket_struct *datapacket) {

  if (rear_count == 0) {
    datapacket->rear_rpm = -1;
    }
  else { datapacket->rear_rpm = rear_count; }

  if (front_left_count == 0) {
    datapacket->front_left_rpm = -1;
    }
  else { datapacket->front_left_rpm = front_left_count; }

  if (front_right_count == 0) {
    datapacket->front_right_rpm = -1;
    }
  else { datapacket->front_right_rpm = front_right_count; }

  rear_count = 0;
  front_left_count = 0;
  front_right_count = 0;

  }

/*
#ifdef DIAGNOSTICS
void print_datapacket() {
  char temp[500];

  sprintf(temp, "\nSFR\tSFL\tSBR\tSBL\tRR\tFRR\tFLR\tLAT\tLON\tSPD\n");
  for (int i = 0; i < 10; i++) {
    switch(i) {
      case(0): sprintf(temp + strlen(temp), "%d\t", dps[0].front_right); break;
      
      case(1): sprintf(temp + strlen(temp), "%d\t", dps[0].front_left); break;
      
      case(2): sprintf(temp + strlen(temp), "%d\t", dps[0].back_right); break;
      
      case(3): sprintf(temp + strlen(temp), "%d\t", dps[0].back_left); break;
      
      case(4): sprintf(temp + strlen(temp), "%d\t", dps[0].rear_rpm); break;
      
      case(5): sprintf(temp + strlen(temp), "%d\t", dps[0].front_right_rpm); break;
      
      case(6): sprintf(temp + strlen(temp), "%d\t", dps[0].front_left_rpm); break;

      case(7):
        char t[15];
        dtostrf(dps[0].gps_latitude, 15, 6, t); 
        sprintf(temp + strlen(temp), "%s\t", t); 
        break;
      case(8):
        char s[15];
        dtostrf(dps[0].gps_longtitude, 15, 6, s); 
        sprintf(temp + strlen(temp), "%s\t", s); 
        break;
      case(9):
        char i[15];
        dtostrf(dps[0].gps_speed, 15, 6, i); 
        sprintf(temp + strlen(temp), "%s\t", i); 
        break;
      }
    }

  Serial.print(temp);
}
#endif
*/
void send_datapacket() {
  byte_count = 0;
    
  Serial2.write(FrameStart);
  
  for (int s = 0; s < num_of_datapackets; s++) {
    
    byte* structPtr = (byte*) &dps[s];
    
    for (size_t i=0; i < sizeof(dps[s]); i++) {
      
      if ((structPtr[i] == FrameStart) || (structPtr[i] == FrameEnd) || (structPtr[i] == FrameESC)) {
        #ifdef DIAGNOSTICS  
        Serial.println("special byte sent");
        #endif
        

        Serial2.write(FrameESC);
        Serial2.write(structPtr[i] ^ 0xA5);
        byte_count = byte_count + 2;
        
        
      } 
      else {
        Serial2.write(structPtr[i]);
        byte_count++;
        }
      }
      
    }
  

  Serial2.write(FrameEnd);
  byte_count = byte_count + 2;
  //sprintf(k, "%d DATAPACKET SENT, TOTAL OF %d BYTES", num_of_datapackets, size_of_packet); 

  #ifdef DIAGNOSTICS  
  Serial.println(byte_count);
  #endif
}

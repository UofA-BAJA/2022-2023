#include <TinyGPS++.h>

#define MAX_PACKETS_TO_BE_CACHED 1

#define BUSY_PIN 4

#define DIAGNOSTICS 1

#define READ_SUSPENSION 1
#define READ_GPS 0
#define READ_RPM 0

const int analogInPin[4] = {A4, A5, A6, A7};  // Analog input pin that the potentiometer is attached to

TinyGPSPlus gps_;

unsigned long timer = 0;


const byte FrameStart=0xfa;
const byte FrameEnd=0xfb;
const byte FrameESC=0xfc;

struct datapacket_struct  {
  uint16_t front_right;
  uint16_t front_left;
  uint16_t back_right;
  uint16_t back_left;
};

typedef enum
{   
    SEND_DATA,
    WAIT_TO_SEND,
    COLLECT_DATA
}States_t;

datapacket_struct dps[MAX_PACKETS_TO_BE_CACHED];

States_t state;

int num_of_datapackets = 0;

void get_new_datapacket();

void suspension(struct datapacket_struct *);

void gps(struct datapacket_struct *);

void send_datapacket();

void sendoverserial();

void print_datapackets();

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

  state = COLLECT_DATA;
}

void loop() {
  delay(50);
  
  switch(state) {
    case(COLLECT_DATA):
      
      get_new_datapacket();
      
      
      #ifdef DIAGNOSTICS
      Serial.print("COLLECTING");
        
      #endif

      num_of_datapackets++;
      break;
      
    case(SEND_DATA):
      #ifdef DIAGNOSTICS      
      #endif
      send_datapacket();
      num_of_datapackets = 0;
      break;
    case(WAIT_TO_SEND):
      while(digitalRead(BUSY_PIN)) {
        #ifdef DIAGNOSTICS
        Serial.println("WAITING TO SEND");
        delay(1000);
        #endif
        }
      break;
    
   }

  if (!digitalRead(BUSY_PIN) && num_of_datapackets != 0) {
    
    state = SEND_DATA;
    
    }
  else{
    if (num_of_datapackets == MAX_PACKETS_TO_BE_CACHED) {
      state = WAIT_TO_SEND;
      num_of_datapackets = 0;
    }
    else state = COLLECT_DATA;
    }

  
}

void get_new_datapacket() {
  unsigned long init = micros();
  datapacket_struct dp;

  suspension(&dp);

  //gps(&dp);

  dps[num_of_datapackets] = dp;

  #ifdef DIAGNOSTICS  
  unsigned long diff = micros() - init;
  char charVal[100];
  sprintf(charVal, "TIME FOR DATAPACKET IS: %lu", diff);
  Serial.println(charVal);
  #endif
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

void gps(struct datapacket_struct *datapacket) {
  while (Serial1.available() > 0){
    gps_.encode(Serial1.read());
    if (gps_.location.isUpdated()){
      // Latitude in degrees (double)
      Serial.print("Latitude= "); 
      Serial.print(gps_.location.lat(), 6);      
      // Longitude in degrees (double)
      Serial.print(" Longitude= "); 
      Serial.println(gps_.location.lng(), 6);
    }
  }
}

#ifdef DIAGNOSTICS
void print_datapackets() {
  char temp[500];

  sprintf(temp+strlen(temp), "\n\nDATAPACKET %d ", num_of_datapackets);
  sprintf(temp+strlen(temp), "SENDING:\n\tFR:%d\n\tFL:%d\n\tBR:%d\n\tBL:%d",dps[num_of_datapackets].front_right,dps[num_of_datapackets].front_left, dps[num_of_datapackets].back_right, dps[num_of_datapackets].back_left);
  
  sprintf(temp+strlen(temp), "\nTIMER IN MS: %lu", timer);  

  Serial.println(temp);
}
#endif

void send_datapacket() {
  //for (int i = 0; i < sizeof(buffer_message); i++) Serial.write(buffer_message[i]);
  int size_of_packet = 0;
  Serial.print("\npacket sent: ");
  Serial.print(dps[0].front_right); Serial.print(","); Serial.print(dps[0].front_left); Serial.print(","); Serial.print(dps[0].back_right); Serial.print(","); Serial.print(dps[0].back_left);
  Serial.print("\n");  
  
   Serial2.write(FrameStart);
  for (int s = 0; s < num_of_datapackets; s++) {
    
    byte* structPtr = (byte*) &dps[s];
    
    for (size_t i=0; i < sizeof(dps[s]); i++) {
      if ((structPtr[i] == FrameStart) || (structPtr[i] == FrameEnd) || (structPtr[i] == FrameESC)) {
        Serial.println("special byte spent");

        Serial2.write(FrameESC);
        Serial2.write(structPtr[i] ^ 0xA5);
      } else Serial2.write(structPtr[i]);
      
      size_of_packet++;
    }
  }

  Serial2.write(FrameEnd);

  Serial.print("SENT ");
  Serial.print(size_of_packet);
  Serial.print("BYTES");
  Serial.println();  
}

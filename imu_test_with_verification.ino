// Library for I2C Communication
#include <Wire.h>

//To read to SD cards
//#include <SPI.h>
//#include <SD.h>

//imu libraries
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

#include <SPI.h>
#include <SD.h>

#define TCAADDR 0x70

/* VERY IMPORTANT */

#define ENABLE_WRITE_TO_SD
/*ENABLED: arduino writes to the sd card and this will disable all serial communication for speed on the sd card */
//#define PLOT

/*----------------*/

#define LED_PIN 2
#define LED_DELAY 150
#define MUX_DELAY 7
#define IMU_SETUP_DELAY 250

uint16_t BNO055_SAMPLERATE_DELAY_MS = 10;

// Check I2C device address and correct line below (by default address is 0x29 or 0x28)
//                                   id, address
Adafruit_BNO055 bno_0 = Adafruit_BNO055(1, 0x28);
Adafruit_BNO055 bno_1 = Adafruit_BNO055(2, 0x28);
Adafruit_BNO055 bno_2 = Adafruit_BNO055(3, 0x28);

Adafruit_BNO055 bno_3 = Adafruit_BNO055(4, 0x28);
Adafruit_BNO055 bno_4 = Adafruit_BNO055(5, 0x28);
Adafruit_BNO055 bno_5 = Adafruit_BNO055(6, 0x28);
Adafruit_BNO055 bno_arr[6] = {bno_1, bno_2, bno_3, bno_4, bno_5, bno_0};

bool imu_detected_arr[6] = {false, false, false, false, false, false}; 

//////////////////////////////   imu helper functions   //////////////////////////////////////////////////////////////
void tcaselect(uint8_t i) {
  //the mux choices are "IMU" and "LIDAR"
  //i is the mux bus #
  if (i > 7) return;

  Wire.beginTransmission(TCAADDR);
  
  Wire.write(1 << i);
  Wire.endTransmission();  

  //Serial.print("\n Successfully switched to port "); Serial.print(i); Serial.print("\n");
}


bool setup_imu(Adafruit_BNO055 *bno, int num) {
  /* Initialise the sensor */
  if (!(*bno).begin())
  {
    /* There was a problem detecting the BNO055 ... check your connections */

    #ifndef ENABLE_WRITE_TO_SD

      #ifndef PLOT
      Serial.print("\n Ooops, BNO055 "); Serial.print(num); Serial.print(" not detected ... Check your wiring or I2C ADDR!");
      #endif
    #endif
    //while(1);
    
    return false;

  }

  #ifndef ENABLE_WRITE_TO_SD
   #ifndef PLOT
    Serial.print("\n"); Serial.print("IMU "); Serial.print(num); Serial.print(" successfully detected");
    #endif
  #endif

  return true;
  
 
}

void get_data(Adafruit_BNO055 *bno, int num, char event_type_select[], double fill_array[3]){
  //could add VECTOR_ACCELEROMETER, VECTOR_MAGNETOMETER,VECTOR_GRAVITY...
  //sensors_event_t angVelocityData, accelerometerData, orientationData;
  sensors_event_t orientationData;
  //(*bno).getEvent(&angVelocityData, Adafruit_BNO055::VECTOR_GYROSCOPE);
  //(*bno).getEvent(&accelerometerData, Adafruit_BNO055::VECTOR_ACCELEROMETER);
  (*bno).getEvent(&orientationData, Adafruit_BNO055::VECTOR_EULER);

  //Serial.print("\n----------TEST FOR "); Serial.print(num); Serial.print("----------\n");
  double x = -1000000, y = -1000000 , z = -1000000; //dumb values, easy to spot problem

  /*
  if (strcmp(event_type_select, "LINEAR_ACCEL") == 0) {
    // result_array = getData(&accelerometerData);
  
    //Serial.print("Accl:");
    x = accelerometerData.acceleration.x;
    y = accelerometerData.acceleration.y;
    z = accelerometerData.acceleration.z;
    
   }
   */
    
  if (strcmp(event_type_select, "ORIENTATION") == 0){
    // result_array = getData(&angVelocityData);
    x = orientationData.orientation.x;
    z = orientationData.orientation.z;
    
    y = orientationData.orientation.y;
   
    } 

  fill_array[0] = x;
  fill_array[1] = y;
  fill_array[2] = z;

  //Serial.print("IMU "); Serial.print(num); Serial.print(" deg: ");  Serial.print(x);  Serial.print("\n"); 
  //Serial.print(data_arr[0]); Serial.print(" "); Serial.print(data_arr[1]);  Serial.print(" "); Serial.print(data_arr[2]);  Serial.print("\n"); 

  delay(BNO055_SAMPLERATE_DELAY_MS);
}

double get_angle(int imu_num) {
  double oritnt[3];
    
  //get_data(&bno_arr[imu_num], imu_num, "LINEAR_ACCEL", lin_acc);
  get_data(&bno_arr[imu_num], imu_num, "ORIENTATION", oritnt);

  return *(oritnt + 0);
}

unsigned long getTime() {
  return millis();
  }

void flash_led(int times) {

  for (int i = 0; i < times; i++) {
    digitalWrite(LED_PIN, HIGH);
    delay(LED_DELAY);
    digitalWrite(LED_PIN, LOW);
    delay(LED_DELAY);
  }
}

void setup() {


  Wire.begin();

  #ifndef ENABLE_WRITE_TO_SD
  Serial.begin(115200);
  #endif

  // put your setup code here, to run once:

  for (int imu_num = 0; imu_num < 6; imu_num++) {
    tcaselect(imu_num);
    delay(MUX_DELAY);
    imu_detected_arr[imu_num] = setup_imu(&bno_arr[imu_num], imu_num);
    delay(IMU_SETUP_DELAY);
  }

  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

  delay(200);

  #ifndef ENABLE_WRITE_TO_SD
    #ifndef PLOT
 
    Serial.print("\n Initializing SD card...");
    #endif

  #endif
    if (!SD.begin(10)) {
     
      
     #ifndef ENABLE_WRITE_TO_SD
     #ifndef PLOT
        Serial.print("\n initialization failed!!!!");
     #endif   
      #endif
    }
    else {
      flash_led(10);
      #ifndef ENABLE_WRITE_TO_SD  
      #ifndef PLOT
        Serial.print("\n SD Card successfully initialized"); 
        #endif
      #endif
    }

  

  File myFile = SD.open("poopee6.txt", FILE_WRITE);
  // if the file opened okay, write to it:
  if (myFile) {
    #ifndef ENABLE_WRITE_TO_SD
    #ifndef PLOT
      Serial.print("\n SUCCESSFULLY OPENED FILE: ");
      #endif
    #endif
    
    #ifdef ENABLE_WRITE_TO_SD
    myFile.print("TIME(s)"); myFile.print(",");
    for (int imu_num = 0; imu_num < 6; imu_num++) {

      if(!imu_detected_arr[imu_num]) {
      //Serial.print("SKIPPED IMU"); Serial.print(imu_num); Serial.print("\n"); 
      continue;
      }
      
      myFile.print("IMU"); myFile.print(imu_num); myFile.print("(deg)"); 
     

      if (imu_num != 5) {
        myFile.print(",");
        }
    }
    myFile.print("\n");
    myFile.close();
    #endif
  }
  else {
    #ifndef ENABLE_WRITE_TO_SD
    #ifndef PLOT
      Serial.print("\n failed to open file");
      #endif
    #endif 
  }
}

void loop() {
  
  #ifdef ENABLE_WRITE_TO_SD
  
  File myFile = SD.open("poopee7.txt", FILE_WRITE);
  
  //Serial.print(filename_buf);
 
  myFile.print(getTime()); myFile.print(",");
  #endif
  
  int imu_num;

  for (imu_num = 0; imu_num < 6; imu_num++) {

    if(!imu_detected_arr[imu_num]) {
      //Serial.print("SKIPPED IMU"); Serial.print(imu_num); Serial.print("\n"); 
      continue;
      }
    
    tcaselect(imu_num);

    delay(MUX_DELAY);
    
    //Serial.print("\n"); Serial.print("main lin acc "); Serial.print(lin_acc[0]); Serial.print(" "); Serial.print(lin_acc[1]); Serial.print(" "); Serial.print(lin_acc[2]);
  
    //imu_data[0] = *(lin_acc + 0); imu_data[1] = *(lin_acc + 1); imu_data[2] = *(lin_acc + 2);
    
    //imu_data[3] = *(oritnt + 0); imu_data[4] = *(oritnt + 1); imu_data[5] = *(oritnt + 2);
  
   // myFile.print(*(lin_acc + 0)); myFile.print(","); myFile.print(*(lin_acc + 1)); myFile.print(","); myFile.print(*(lin_acc + 2)); myFile.print(",");
   double x = get_angle(imu_num);   

   #ifdef ENABLE_WRITE_TO_SD
    myFile.print(x); 
    #endif

    #ifndef ENABLE_WRITE_TO_SD
    #ifndef PLOT
    Serial.print("IMU"); Serial.print(imu_num); Serial.print(": "); Serial.print(x);
    #else
    Serial.print(x);
    #endif
    #endif
      
    if (imu_num != 5) {
      #ifdef ENABLE_WRITE_TO_SD
      myFile.print(",");
      #else
      Serial.print("\t");  
      #endif  
   }
    
  }

  #ifdef ENABLE_WRITE_TO_SD
  myFile.print("\n");

  myFile.close();
  #else
  Serial.print("\n"); 
  #endif

}

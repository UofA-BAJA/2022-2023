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

uint16_t BNO055_SAMPLERATE_DELAY_MS = 50;

// Check I2C device address and correct line below (by default address is 0x29 or 0x28)
//                                   id, address
Adafruit_BNO055 bno_0 = Adafruit_BNO055(1, 0x28);
Adafruit_BNO055 bno_1 = Adafruit_BNO055(2, 0x28);
Adafruit_BNO055 bno_2 = Adafruit_BNO055(3, 0x28);

Adafruit_BNO055 bno_3 = Adafruit_BNO055(4, 0x28);
Adafruit_BNO055 bno_4 = Adafruit_BNO055(5, 0x28);
Adafruit_BNO055 bno_5 = Adafruit_BNO055(6, 0x28);
Adafruit_BNO055 bno_arr[6] = {bno_1, bno_2, bno_3, bno_4, bno_5, bno_0};

int rand_num = random(0,99);
String filename = "AX" + String(rand_num) + ".txt";


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


void setup_imu(Adafruit_BNO055 *bno, int num) {
  /* Initialise the sensor */
  if (!(*bno).begin())
  {
    /* There was a problem detecting the BNO055 ... check your connections */
    Serial.print("\n Ooops, BNO055 "); Serial.print(num); Serial.print(" not detected ... Check your wiring or I2C ADDR!");
    //while(1);
    
  }
  else {Serial.print("\n"); Serial.print("IMU "); Serial.print(num); Serial.print(" successfully detected");}

  delay(100);
 
}

void get_data(Adafruit_BNO055 *bno, int num, char event_type_select[], double fill_array[3]){
  //could add VECTOR_ACCELEROMETER, VECTOR_MAGNETOMETER,VECTOR_GRAVITY...
  sensors_event_t angVelocityData, accelerometerData, orientationData;
  //(*bno).getEvent(&angVelocityData, Adafruit_BNO055::VECTOR_GYROSCOPE);
  (*bno).getEvent(&accelerometerData, Adafruit_BNO055::VECTOR_ACCELEROMETER);
  (*bno).getEvent(&orientationData, Adafruit_BNO055::VECTOR_EULER);


  //Serial.print("\n----------TEST FOR "); Serial.print(num); Serial.print("----------\n");

  double* result_array;
  double x = -1000000, y = -1000000 , z = -1000000; //dumb values, easy to spot problem

  double data_arr[3];

  if (strcmp(event_type_select, "LINEAR_ACCEL") == 0) {
    // result_array = getData(&accelerometerData);
  
    //Serial.print("Accl:");
    x = accelerometerData.acceleration.x;
    y = accelerometerData.acceleration.y;
    z = accelerometerData.acceleration.z;
    
   }
    
  else if (strcmp(event_type_select, "ORIENTATION") == 0){
    // result_array = getData(&angVelocityData);
    x = orientationData.orientation.x;
    z = orientationData.orientation.z;

    Serial.print("Gyro:");
    y = orientationData.orientation.y;
    Serial.print(y);
    }
     Serial.print("\n"); 

  fill_array[0] = x;
  fill_array[1] = y;
  fill_array[2] = z;

  //Serial.print("IMU "); Serial.print(num); Serial.print(" deg: ");  Serial.print(x);  Serial.print("\n"); 
  //Serial.print(data_arr[0]); Serial.print(" "); Serial.print(data_arr[1]);  Serial.print(" "); Serial.print(data_arr[2]);  Serial.print("\n"); 

  delay(BNO055_SAMPLERATE_DELAY_MS);
}


void setup() {


  Wire.begin();
  Serial.begin(115200);
  // put your setup code here, to run once:

  for (int imu_num = 0; imu_num < 6; imu_num++) {
    tcaselect(imu_num);
    setup_imu(&bno_arr[imu_num], imu_num);
  }

  delay(200);

  Serial.print("\n Initializing SD card...");
  if (!SD.begin(4)) {
    Serial.print("\n initialization failed!!!!");
  }
  else {  Serial.print("\n SD Card successfully initialized"); }


  char filename_buf[filename.length()];
  filename.toCharArray(filename_buf, filename.length()+1);

  /*

  myFile = SD.open("po01.txt", FILE_WRITE);
  // if the file opened okay, write to it:
  if (myFile) {
    Serial.print("\n FILE OPEN SUCCESS");
    //myFile.print("LIN_ACC_X_IMU_0\t\tLIN_ACC_Y_IMU_0\t\tLIN_ACC_Z_IMU_0\t\tORINT_X_IMU_0\t\tORINT_Y_IMU_0\t\tORINT_Z_IMU_0\t\tLIN_ACC_X_IMU_1\t\tLIN_ACC_Y_IMU_1\t\tLIN_ACC_Z_IMU_1\t\tORINT_X_IMU_1\t\tORINT_Y_IMU_1\t\tORINT_Z_IMU_1\t\tLIN_ACC_X_IMU_2\t\tLIN_ACC_Y_IMU_2\t\tLIN_ACC_Z_IMU_2\t\tORINT_X_IMU_2\t\tORINT_Y_IMU_2\t\tORINT_Z_IMU_2\t\t");
    myFile.print("\n");
  }
  else {
    Serial.print("\n failed to open file");
  }
  */

    Serial.print("\n FILENAME: "); Serial.print(filename_buf); 
}

void loop() {


/*

  File myFile = SD.open("MICHAEL.txt", FILE_WRITE);
  
  if (myFile) {
    Serial.print("\n FILE OPEN SUCCESS");
    //myFile.print("LIN_ACC_X_IMU_0\t\tLIN_ACC_Y_IMU_0\t\tLIN_ACC_Z_IMU_0\t\tORINT_X_IMU_0\t\tORINT_Y_IMU_0\t\tORINT_Z_IMU_0\t\tLIN_ACC_X_IMU_1\t\tLIN_ACC_Y_IMU_1\t\tLIN_ACC_Z_IMU_1\t\tORINT_X_IMU_1\t\tORINT_Y_IMU_1\t\tORINT_Z_IMU_1\t\tLIN_ACC_X_IMU_2\t\tLIN_ACC_Y_IMU_2\t\tLIN_ACC_Z_IMU_2\t\tORINT_X_IMU_2\t\tORINT_Y_IMU_2\t\tORINT_Z_IMU_2\t\t");
    //myFile.print("\n");
  }
  else {
    Serial.print("\n failed to open file");
    while(1);
  }

  int imu_num = 0;

  for (imu_num; imu_num < 6; imu_num++) {

    
    tcaselect(imu_num);
    
    double lin_acc[3]; double oritnt[3];
    
    get_data(&bno_arr[imu_num], imu_num, "LINEAR_ACCEL", lin_acc);
    get_data(&bno_arr[imu_num], imu_num, "ORIENTATION", oritnt);
  
    //Serial.print("\n"); Serial.print("main lin acc "); Serial.print(lin_acc[0]); Serial.print(" "); Serial.print(lin_acc[1]); Serial.print(" "); Serial.print(lin_acc[2]);
  
    //imu_data[0] = *(lin_acc + 0); imu_data[1] = *(lin_acc + 1); imu_data[2] = *(lin_acc + 2);
    
    //imu_data[3] = *(oritnt + 0); imu_data[4] = *(oritnt + 1); imu_data[5] = *(oritnt + 2);
  
    myFile.print(*(lin_acc + 0)); myFile.print(","); myFile.print(*(lin_acc + 1)); myFile.print(","); myFile.print(*(lin_acc + 2)); myFile.print(",");
    myFile.print(*(oritnt + 0)); myFile.print(","); myFile.print(*(oritnt + 1)); myFile.print(","); myFile.print(*(oritnt + 2)); myFile.print(",");

  }

  
  myFile.print("\n");

  myFile.close();

 */
  

}

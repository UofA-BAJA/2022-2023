#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
  
Adafruit_BNO055 bno = Adafruit_BNO055(55);

struct imu_thing{
  int8_t gyro_x, gyro_y, gyro_z;
  byte acc_x, acc_y, acc_z;
};

void setup(void) 
{
  Serial.begin(9600);
  
  while(!bno.begin())
  {
    bno.begin();
    delay(10);
  }
  
  delay(10);
    
  bno.setExtCrystalUse(true);
}


void loop(void) 
{ 
  sensors_event_t event; 
  bno.getEvent(&event);
  
  imu::Vector<3> accel = bno.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER);
  imu_thing new_event = {event.orientation.x, event.orientation.y, event.orientation.z, accel.x() * 100, accel.y() * 100, accel.z()};

  send(&new_event);
  delay(1000);
}


void send (const imu_thing* new_event) {
  Serial.write((const char*)new_event, sizeof(imu_thing));
}

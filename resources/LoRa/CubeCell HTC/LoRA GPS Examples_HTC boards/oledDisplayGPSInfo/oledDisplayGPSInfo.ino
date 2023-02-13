// Importing Arduino Library
#include "Arduino.h"
// Importing I2C Library
#include <Wire.h>  
// Importing GPS Library required for board
#include "GPS_Air530Z.h"
// Importing OLED Screen 128x64 Library
#include "HT_SSD1306Wire.h"

#define MASTER_ADDRESS 0x04

// Defining OLED Screen address, frequency, SDA, SCL, resolution and reset pin
SSD1306Wire  display(0x3c, 500000, SDA, SCL, GEOMETRY_128_64, GPIO10); // addr , freq , SDA, SCL, resolution , rst

// Defining GPS
Air530ZClass GPS;


void setup() {
  /*
  This function is run when the processor initializes and only runs once.
  Use this function to initialize all of the sensors and communication methods.
  Args:
    None
  Return Value:
    None
  */

  // Run VextON Function; enables Vext as output and set LOW
  VextON();
  delay(10);
  
  // Begin OLED Screen Communication
  display.init();
  display.clear(); 
  display.display();  
  display.drawString(0, 0, "Initializing");
  display.drawProgressBar(10, 32, 100, 10, 10);
  display.display();

  // Begin Serial Communication; 115200 BAUD Rate
  Serial.begin(115200);

  // Begin GPS Communication
  GPS.begin();

  // Begin I2C Comunication; assign address 2
  Wire.begin(MASTER_ADDRESS);
  Wire.onReceive(receiveEvent);
  //Wire.onRequest(requestEvent);

  // Progress Bar Animation
  int progress = 20;
  while (progress <= 100) {
    display.drawProgressBar(10, 32, 100, 10, progress);
    display.display();
    progress += 5;
    delay(10);
  }
  
  delay(100);
}


void loop() {
  /*
  This function runs after the setup() function adn runs continuously.
  Use this function to collect sensor data and send data over LoRa / I2C.
  Args:
    None
  Return Value:
    None
  */

  // Loop which take GPS readings every second
  uint32_t starttime = millis();
  while ((millis()-starttime) < 1000) {
    while (GPS.available() > 0)
    {
      GPS.encode(GPS.read());
    }
  }
  
  // Display GPS Data on OLED Screen
  char str[30];
  display.clear();
  display.setFont(ArialMT_Plain_10);
  int index = sprintf(str,"%02d-%02d-%02d",GPS.date.year(),GPS.date.day(),GPS.date.month());
  str[index] = 0;
  display.setTextAlignment(TEXT_ALIGN_LEFT);
  display.drawString(0, 0, str);
  
  index = sprintf(str,"%02d:%02d:%02d",GPS.time.hour(),GPS.time.minute(),GPS.time.second(),GPS.time.centisecond());
  str[index] = 0;
  display.drawString(60, 0, str);

  if (GPS.location.age() < 1000) {
    display.drawString(120, 0, "A");
  } else {
    display.drawString(120, 0, "V");
  }

  display.drawString(0, 12, "UofA BAJA Racing");
  
  index = sprintf(str,"alt: %d.%dm",(int)GPS.altitude.meters(),fracPart(GPS.altitude.meters(),2));
  str[index] = 0;
  display.drawString(0, 24, str);
   
  index = sprintf(str,"sats: %d.%d",(int)GPS.satellites.value(), fracPart(GPS.location.lat(),0));
  str[index] = 0;
  display.drawString(0, 36, str); 
 
  index = sprintf(str,"lat :  %d.%d",(int)GPS.location.lat(),fracPart(GPS.location.lat(),4));
  str[index] = 0;
  display.drawString(60, 24, str);   
  
  index = sprintf(str,"lon:%d.%d",(int)GPS.location.lng(),fracPart(GPS.location.lng(),4));
  str[index] = 0;
  display.drawString(60, 36, str);

  index = sprintf(str,"speed: %d.%d mph",(int)GPS.speed.mph(),fracPart(GPS.speed.mph(),3));
  str[index] = 0;
  display.drawString(0, 48, str);
  display.display();
}


void receiveEvent(int bytes) {
  Wire.read();
}


void requestEvent() {
  /*
  This function takes compiled GPS data and sends it over I2C.
  When requested from the Master board, this function will execute.
  Args:
    data = structure representing compiles sensor data
  Return Value:
    None
  */
  Wire.write("TEST");
}


int fracPart(double val, int n) {
  /*
  This function...
  Args:
    val = 
    n = 
  Return Value:
    value = integer representing...
  */
  return (int)((val - (int)(val))*pow(10,n));
}


void VextON(void) {
  /*
  This function enables Vext as output and sets LOW
  Use to turn Vext LOW
  Args:
    None
  Return Value:
    None
  */
  pinMode(Vext, OUTPUT);
  digitalWrite(Vext, LOW);
}


//Vext default OFF
void VextOFF(void) {
  /*
  This function enables Vext as output and sets HIGH
  Use to turn Vext HIGH
  Args:
    None
  Return Value:
    None
  */
  pinMode(Vext, OUTPUT);
  digitalWrite(Vext, HIGH);
}
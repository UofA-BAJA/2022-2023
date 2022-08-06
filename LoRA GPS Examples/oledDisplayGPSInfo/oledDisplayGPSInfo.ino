//the GPS module used is GPS.
#include "Arduino.h"
#include "GPS_Air530Z.h"
#include <Wire.h>  
#include "HT_SSD1306Wire.h"

SSD1306Wire  display(0x3c, 500000, SDA, SCL, GEOMETRY_128_64, GPIO10); // addr , freq , SDA, SCL, resolution , rst

//if GPS module is Air530Z, use this
Air530ZClass GPS;

int fracPart(double val, int n)
{
  return (int)((val - (int)(val))*pow(10,n));
}

void VextON(void)
{
  pinMode(Vext,OUTPUT);
  digitalWrite(Vext, LOW);
}

void VextOFF(void) //Vext default OFF
{
  pinMode(Vext,OUTPUT);
  digitalWrite(Vext, HIGH);
}

void setup() {
  VextON();
  delay(10);
  
  display.init();
  display.clear();
  display.display();
  
  display.drawString(0, 0, "Initializing");
  display.drawProgressBar(10, 32, 100, 10, 10);
  display.display();

  Serial.begin(115200);
  GPS.begin();
  
  //display.setTextAlignment(TEXT_ALIGN_CENTER);
  //display.setFont(ArialMT_Plain_16);
  //display.drawString(64, 32-16/2, "GPS initing...");
  //display.display();
  
  int progress = 20;
  while (progress <= 100) {
    display.drawProgressBar(10, 32, 100, 10, progress);
    display.display();
    progress += 5;
    delay(10);
  }
  
  delay(100);
}

void loop()
{
  uint32_t starttime = millis();
  while( (millis()-starttime) < 1000 )
  {
    while (GPS.available() > 0)
    {
      GPS.encode(GPS.read());
    }
  }
  
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

  if( GPS.location.age() < 1000 )
  {
    display.drawString(120, 0, "A");
  }
  else
  {
    display.drawString(120, 0, "V");
  }

  display.drawString(0, 16, "UofA BAJA Racing");
  
  index = sprintf(str,"alt: %d.%d m",(int)GPS.altitude.meters(),fracPart(GPS.altitude.meters(),2));
  str[index] = 0;
  display.drawString(0, 32, str);
   
  index = sprintf(str,"sats: %d.%d",(int)GPS.satellites.value(), fracPart(GPS.location.lat(),0));
  str[index] = 0;
  display.drawString(0, 48, str); 
 
  index = sprintf(str,"lat :  %d.%d",(int)GPS.location.lat(),fracPart(GPS.location.lat(),4));
  str[index] = 0;
  display.drawString(60, 32, str);   
  
  index = sprintf(str,"lon:%d.%d",(int)GPS.location.lng(),fracPart(GPS.location.lng(),4));
  str[index] = 0;
  display.drawString(60, 48, str);

  index = sprintf(str,"speed: %d.%d mph",(int)GPS.speed.mph(),fracPart(GPS.speed.mph(),3));
  str[index] = 0;
  display.drawString(0, 64, str);
  display.display();
}

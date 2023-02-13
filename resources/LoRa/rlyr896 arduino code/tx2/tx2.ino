#include <SoftwareSerial.h>
SoftwareSerial lora(2,3);
 
void setup()
{
  // put your setup code here, to run once: this is for the receiver
  Serial.begin(115200);
  lora.begin(115200);
 
}
 
void loop()
{
  String inString;
  //Serial.println("enter loop");
  while (lora.available())
  {
      //Serial.println("entering while loop");
    if(lora.available()){
      //Serial.println("enter available loop");

      inString += String(char(lora.read()));
    }
  }
  if(inString.length()>0)
  {
      Serial.println("result: ");
      Serial.println(inString);
      inString.remove(0);
      
  }
  

}

#include <SoftwareSerial.h>
SoftwareSerial lora(0,1);
 
void setup()
{
  // put your setup code here, to run once:
  Serial.begin(115200);
  lora.begin(115200);
//  lora.println("AT+FACTORY");
//  Serial.println("AT+FACTORY");
  lora.println("AT+PARAMETER=11,9,4,12");
  Serial.println("AT+PARAMETER=11,9,4,12");
  lora.println("AT+BAND=470000000");
  Serial.println("AT+BAND=470000000");
 
}
 
void loop()
{

  String inString;
  while (lora.available())
  {
    if(lora.available()){
    inString += String(char(lora.read()));
    }
  }
  if(inString.length()>0)
  {
      Serial.println(inString);
      inString.remove(0);
  }
}

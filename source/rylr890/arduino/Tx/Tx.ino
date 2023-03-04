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
  String values = "poop";
  String cmd = "AT+SEND=0,"+String(values.length())+","+values;
  lora.println(cmd);
//   while(lora.available())
//  {
//    Serial.write(lora.read());
//  }
  Serial.println(cmd);
  lora.println(cmd);
  delay(5);
}

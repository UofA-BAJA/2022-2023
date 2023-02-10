String myString; 
String garbage;
char data; 
void setup() {
  // put your setup code here, to run once:
Serial.begin(115200); 
Serial.print("AT\r\n");
delay(100); 
}

void loop() {
  // put your main code here, to run repeatedly:
if ( Serial.available() > 0 )
{
 
  garbage = Serial.readString(); // consists of the +ERR=2 ERROR. 
  
  myString = Serial.readString(); 
  Serial.println(myString); 

  //Serial.println("Garbage:");
  //Serial.println(garbage);
}
}

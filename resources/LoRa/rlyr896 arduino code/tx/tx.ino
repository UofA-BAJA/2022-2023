int vresistor = A1; 
int vrdata = 0; 
int data_length; 
String vresistordata;
void setup() {
  // put your setup code here, to run once:

Serial.begin(115200); 
pinMode(vresistor,INPUT); 
}

void loop() {
  // put your main code here, to run repeatedly:
send_data(vrdata , data_length); 
delay(100); 

}


void send_data(int sensorvalue, int valuelength)
{

String mymessage; 
mymessage = mymessage + "AT+SEND=0" + "," + 0 + "," + 1 + "\r"; 
Serial.println(mymessage); 
  //Serial.println("AT+SEND=0,6,Hello!\r");
}

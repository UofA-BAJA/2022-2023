#include <SoftwareSerial.h>

#define startMarker 250
#define endMarker 251
#define specialByte 252
#define maxMessage 200

const byte rxPin = 2;

const byte txPin = 3;

SoftwareSerial mySerial (rxPin, txPin);

char temp[100];

byte bytesRecvd = 0;
byte dataRecvCount = 0;

byte dataRecvd[maxMessage]; 
byte tempBuffer[maxMessage];

boolean allReceived = false;
boolean inProgress = false;


union ArrayToInteger {
  byte byteArray[2];
  uint16_t integer;
};

ArrayToInteger converters[4];


void setup() {
    Serial.begin(57600);
    Serial.println("<Arduino is ready>");

    mySerial.begin(57600);

    pinMode(7, OUTPUT);
    digitalWrite(7, HIGH);
}

void loop() {
    
    recvBytesWithStartEndMarkers();
    
    showNewData();

}

void recvBytesWithStartEndMarkers() {
  
  
  digitalWrite(7, LOW);
  //Serial.println("start recieving");

   if(mySerial.available() > 0) {

    byte x = mySerial.read();
    if (x == startMarker) {
      //Serial.println("message start"); 
      bytesRecvd = 0; 
      inProgress = true;
      // blinkLED(2);
      // debugToPC("start received");
    }
      
    if(inProgress) {
      tempBuffer[bytesRecvd] = x;
      bytesRecvd ++;
    }

    if (x == endMarker) {
      //Serial.println("message end"); 
      digitalWrite(7, HIGH);
      inProgress = false;
      allReceived = true;
      
        // save the number of bytes that were sent  
      decodeHighBytes();
    }
  }
   
}

void decodeHighBytes() {

  //  copies to dataRecvd[] only the data bytes i.e. excluding the marker bytes and the count byte
  //  and converts any bytes of 253 etc into the intended numbers
  //  Note that bytesRecvd is the total of all the bytes including the markers
  dataRecvCount = 0;
  for (byte n = 1; n < bytesRecvd - 1 ; n++) { // 2 skips the start marker and the count byte, -1 omits the end marker
   
    byte x = tempBuffer[n];
    if (x == specialByte) {
        Serial.print("special byte recieved");
       n++;
       x = tempBuffer[n] ^ 0xA5;
    }
    dataRecvd[dataRecvCount] = x;
    dataRecvCount ++;
  }

  Serial.print("recieved ");
  Serial.print(dataRecvCount);
  Serial.print("bytes of data");
  Serial.println();

}

void showNewData() {
    if (allReceived) {
        
        sprintf(temp, "DATAPACKET 0::");
        for (int i = 0; i < 4; i++) {
          
          converters[i].byteArray[0] = dataRecvd[2*i];
          converters[i].byteArray[1] = dataRecvd[(2*i)+1];
          
          sprintf(temp + strlen(temp), " %d,", converters[i].integer);
          }

        Serial.println(temp);
        allReceived = false; 
    }
}

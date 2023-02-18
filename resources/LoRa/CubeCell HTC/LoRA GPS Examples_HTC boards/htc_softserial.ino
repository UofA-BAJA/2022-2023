#define TIMEOUT 30//time in ms

uint8_t serialBuffer[256];
int size;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial1.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  size = Serial1.read(serialBuffer,TIMEOUT);
  if(size)
  {
    Serial.printf("rev data size %d : ",size);
    Serial.write(serialBuffer,size);
  }
  //else {Serial.println("size is 0");}
}

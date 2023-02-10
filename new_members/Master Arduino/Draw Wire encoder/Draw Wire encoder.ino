#include <EnableInterrupt.h> //insufficient number of standard Interrupt pins on the Arduino Uno

#include <digitalWriteFast.h>


#define encoderA 2
#define encoderB 3
#define encoderZ 4

volatile int countA = 0;
volatile int countB = 0;
volatile int countZ = 0;
volatile int cumulativeCountA = 0;
volatile int cumulativeCountB = 0;
int pulsesPerRev = 10000;     //This variable will is unique to the type of encoder
int Dir = 0;  // 1 = CW
              // 0 = Stationary
              // -1 = CCW

void setup() {
  Serial.begin(38400);
  pinMode(encoderA, INPUT);
  pinModeFast(encoderB, INPUT);
  pinMode(encoderZ, INPUT);  
  enableInterrupt(encoderA, pulseA, RISING);
  enableInterrupt(encoderB, pulseB, RISING);
  enableInterrupt(encoderZ, pulseZ, RISING);
}

void loop() {
  Serial.print(countA);
  Serial.print('\t');
  Serial.print(countB);
  Serial.print('\t');
  Serial.print(cumulativeCountA);
  Serial.print('\t');
  Serial.print(cumulativeCountB);
  Serial.print('\t');
  Serial.print(Dir);
  Serial.print('\t') ;
  Serial.println(countZ);
}

void checkDirection(){
  if((bool) digitalReadFast(encoderB) ==  HIGH){                             //digitalReadFast() is faster than digitalRead()
    Dir = 1;  
  }
  else if ((bool) digitalReadFast(encoderB) ==  LOW){
    Dir = -1;
  }
  else{
    Dir = 0;
  }
}

void pulseA(){  
  checkDirection();
  countA += Dir;
  cumulativeCountA += Dir;
}

void pulseB(){  
  countB += Dir;
  cumulativeCountB += Dir;  
}

void pulseZ(){
  checkDirection();
  if(Dir == 1){
  countZ ++;
  }
  else if (Dir == -1) {
    countZ --;
  }
  countA = 0;   //reset counters at "home" reference point
  countB = 0;
}
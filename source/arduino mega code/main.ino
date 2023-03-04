/*
  AnalogReadSerial

  Reads an analog input on pin 0, prints the result to the Serial Monitor.
  Graphical representation is available using Serial Plotter (Tools > Serial Plotter menu).
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.

  https://www.arduino.cc/en/Tutorial/BuiltInExamples/AnalogReadSerial
*/

long randNumber[4];
// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(115200);

  randomSeed(analogRead(0));
}

// the loop routine runs over and over again forever:
void loop() {
  
  //START MESSAGE
  Serial.print("<");
  

  //SUSPENSION DATA
  Serial.print("S");
  for (int i = 0; i < 4; ++i) {
    Serial.print(random(300, 700));
    if (i != 3) { Serial.print(","); }
    }
  Serial.print("S");

  //RPM DATA
  Serial.print("R");
  for (int i = 0; i < 3; ++i) {
    int rnum = random(100, 999);
    double dec = rnum / 100.00;
    Serial.print(rnum + dec);
    
    if (i != 2) { Serial.print(","); }
    }
  Serial.print("R");

  Serial.print(sensorValue1);
  Serial.print(",");
  Serial.print(sensorValue2);
  Serial.print(",");
  Serial.print(sensorValue3);
  Serial.print(",");
  Serial.println(sensorValue4);

  Serial2.print("<");
  Serial2.print(sensorValue1);
  Serial2.print(",");
  Serial2.print(sensorValue2);
  Serial2.print(",");
  Serial2.print(sensorValue3);
  Serial2.print(",");
  Serial2.print(sensorValue4);
  Serial2.println(">");
  // wait 2 milliseconds before the next loop for the analog-to-digital
  // converter to settle after the last reading:
  delay(50);
}
/*
  AnalogReadSerial

  Reads an analog input on pin 0, prints the result to the Serial Monitor.
  Graphical representation is available using Serial Plotter (Tools > Serial Plotter menu).
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.

  https://www.arduino.cc/en/Tutorial/BuiltInExamples/AnalogReadSerial
*/

long randNumber[4];
// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(115200);

  randomSeed(analogRead(0));
}

// the loop routine runs over and over again forever:
void loop() {
  
  //START MESSAGE
  Serial.print("<");
  

  //SUSPENSION DATA
  Serial.print("S");
  for (int i = 0; i < 4; ++i) {
    Serial.print(random(300, 700));
    if (i != 3) { Serial.print(","); }
    }
  Serial.print("S");

  //RPM DATA
  Serial.print("R");
  for (int i = 0; i < 3; ++i) {
    int rnum = random(100, 999);
    double dec = rnum / 100.00;
    Serial.print(rnum + dec);
    
    if (i != 2) { Serial.print(","); }
    }
  Serial.print("R");

  Serial.print(sensorValue1);
  Serial.print(",");
  Serial.print(sensorValue2);
  Serial.print(",");
  Serial.print(sensorValue3);
  Serial.print(",");
  Serial.println(sensorValue4);

  Serial2.print("<");
  Serial2.print(sensorValue1);
  Serial2.print(",");
  Serial2.print(sensorValue2);
  Serial2.print(",");
  Serial2.print(sensorValue3);
  Serial2.print(",");
  Serial2.print(sensorValue4);
  Serial2.println(">");
  // wait 2 milliseconds before the next loop for the analog-to-digital
  // converter to settle after the last reading:
  delay(50);
}

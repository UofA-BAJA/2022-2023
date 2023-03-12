//asdasdasd

int c = 0;
int char_index = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:

  char temp[100];

  c == 0;
  while (Serial.available()) 
  {
    byte b = Serial.read();//Forward what Serial received to Software Serial Port
    //Serial.println(b);
    if (b == '<') {
      
      c++;
      //Serial.println("Start of message");
      }
      
    if (c == 2) {
      
      temp[char_index] = b;
      char_index++;

      if (b == '>') {
        break;
        }
      }
  }

  if (char_index > 0) {

    temp [char_index + 1] = '/0';

    //char new_temp[200];
    
    //sprintf(new_temp, "%s", temp);
    

    //int first_number = atoi(temp[1]) * 10 + atoi(temp[2]);
    //int first_number = 2;


    //sprintf(new_temp + strlen(new_temp), "\nFIRST NUMBER IS: %d \n", char_index);

    char_index = 0;

    Serial.print(temp[0]);
  }

  

  
 
  
}

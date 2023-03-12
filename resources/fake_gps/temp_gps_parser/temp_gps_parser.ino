//asdasdasd

int c = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:

  char temp[100];
  int char_index = 0;
  while (Serial.available()) 
  {
    char b = Serial.read();//Forward what Serial received to Software Serial Port

    if (b == "<") {
      
      c++;
      }
    

      
    if (c == 2) {
      
      temp[char_index] = b;
      char_index++;

      if (b == ">") {
        break;
        }
      }
  }

  if (char_index > 0) {

    char new_temp[200];
    
    sprintf(new_temp, "\n%s\n", temp);
    

    //int first_number = atoi(temp[1]) * 10 + atoi(temp[2]);
    int first_number = 2;


    //sprintf(new_temp + strlen(new_temp), "\nFIRST NUMBER IS: %d \n", char_index);

    

    Serial.print(new_temp);
  }

  
 
  
}

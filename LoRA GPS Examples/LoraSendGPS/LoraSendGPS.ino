
#include "GPS_Air530.h"
#include "GPS_Air530Z.h"

//if GPS module is Air530, use this
//Air530Class GPS;

//if GPS module is Air530Z, use this
Air530ZClass GPS;

#include "LoRaWan_APP.h"
#include "Arduino.h"

/*
 * set LoraWan_RGB to 1,the RGB active in loraWan
 * RGB red means sending;
 * RGB green means received done;
 */
#ifndef LoraWan_RGB
#define LoraWan_RGB 0
#endif

#define RF_FREQUENCY                                915000000 // Hz

#define TX_OUTPUT_POWER                             14        // dBm

#define LORA_BANDWIDTH                              0         // [0: 125 kHz,
                                                              //  1: 250 kHz,
                                                              //  2: 500 kHz,
                                                              //  3: Reserved]
#define LORA_SPREADING_FACTOR                       7         // [SF7..SF12]
#define LORA_CODINGRATE                             1         // [1: 4/5,
                                                              //  2: 4/6,
                                                              //  3: 4/7,
                                                              //  4: 4/8]
#define LORA_PREAMBLE_LENGTH                        8         // Same for Tx and Rx
#define LORA_SYMBOL_TIMEOUT                         0         // Symbols
#define LORA_FIX_LENGTH_PAYLOAD_ON                  false
#define LORA_IQ_INVERSION_ON                        false


#define RX_TIMEOUT_VALUE                            1000
#define BUFFER_SIZE                                 50 // Define the payload size here

char txpacket[BUFFER_SIZE];
char rxpacket[BUFFER_SIZE];

static RadioEvents_t RadioEvents;

char message[BUFFER_SIZE];
String message_string;

double txNumber;

int16_t rssi,rxSize;
void  DoubleToString( char *str, double double_num,unsigned int len);

void setup() {
    Serial.begin(115200);
    GPS.begin();

    txNumber=0;
    rssi=0;

    Radio.Init( &RadioEvents );
    Radio.SetChannel( RF_FREQUENCY );
    Radio.SetTxConfig( MODEM_LORA, TX_OUTPUT_POWER, 0, LORA_BANDWIDTH,
                                   LORA_SPREADING_FACTOR, LORA_CODINGRATE,
                                   LORA_PREAMBLE_LENGTH, LORA_FIX_LENGTH_PAYLOAD_ON,
                                   true, 0, 0, LORA_IQ_INVERSION_ON, 3000 ); 
   }


void loop()
{
  delay(1000);
  GPS_TEST();
  LORA();
}


void GPS_TEST() {
  uint32_t starttime = millis();
  while( (millis()-starttime) < 1000 )
  {
    while (GPS.available() > 0)
    {
      GPS.encode(GPS.read());
    }
  }

  //gps string
  String message_string = GPS.time.hour() + String(":") + GPS.time.minute() + String(":") + GPS.time.second() + String(":") + GPS.time.centisecond() + String(",lat ") + GPS.location.lat() + String(",lon ") + GPS.location.lng() + String(",alt ") + GPS.altitude.meters() + String(",speed ") + GPS.speed.kmph();
  message_string.toCharArray(message, BUFFER_SIZE);
}


void LORA() {
  txNumber += 0.01;
  sprintf(txpacket,"%s",message);  //start a package
  sprintf(txpacket+strlen(txpacket),"%d",txNumber); //add to the end of package
  
  DoubleToString(txpacket,txNumber,3);     //add to the end of package

  Serial.printf("\r\nsending packet \"%s\" , length %d\r\n",message, strlen(txpacket));

  Radio.Send( (uint8_t *)txpacket, strlen(txpacket) ); //send the package out 
}

/**
  * @brief  Double To String
  * @param  str: Array or pointer for storing strings
  * @param  double_num: Number to be converted
  * @param  len: Fractional length to keep
  * @retval None
  */
  
void  DoubleToString( char *str, double double_num,unsigned int len) { 
  double fractpart, intpart;
  fractpart = modf(double_num, &intpart);
  fractpart = fractpart * (pow(10,len));
  sprintf(str + strlen(str),"%d", (int)(intpart)); //Integer part
  sprintf(str + strlen(str), ".%d", (int)(fractpart)); //Decimal part
}

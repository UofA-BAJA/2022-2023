/* Heltec Automation Ping Pong communication test example
 *
 * Function:
 * 1. Ping Pong communication in two CubeCell device.
 * 
 * Description:
 * 1. Only hardware layer communicate, no LoRaWAN protocol support;
 * 2. Download the same code into two CubeCell devices, then they will begin Ping Pong test each other;
 * 3. This example is for CubeCell hardware basic test.
 *
 * HelTec AutoMation, Chengdu, China
 * 成都惠利特自动化科技有限公司
 * www.heltec.org
 *
 * this project also realess in GitHub:
 * https://github.com/HelTecAutomation/ASR650x-Arduino
 * */

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

#define TX_OUTPUT_POWER                             20        // dBm

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
#define BUFFER_SIZE                                 200 // Define the payload size here

#define BUSY_PIN 7

char txpacket[BUFFER_SIZE];
char rxpacket[BUFFER_SIZE];

static RadioEvents_t RadioEvents;
void OnTxDone( void );
void OnTxTimeout( void );
void OnRxDone( uint8_t *payload, uint16_t size, int16_t rssi, int8_t snr );

typedef enum
{
    LOWPOWER,
    RX,
    TX
}States_t;

int16_t txNumber;
States_t state;
bool sleepMode = false;
int16_t Rssi,rxSize;

//SERIAL COMMUNICATIONS
#define startMarker 250
#define endMarker 251
#define specialByte 252
#define maxMessage 200

byte bytesRecvd = 0;
byte dataRecvCount = 0;

byte dataRecvd[maxMessage]; 
byte tempBuffer[maxMessage];

boolean allReceived = false;
boolean inProgress = false;
//---------------------

void recvBytesWithStartEndMarkers();

void setup() {
    Serial1.begin(57600);//serial port
    pinMode(BUSY_PIN, OUTPUT);
    digitalWrite(BUSY_PIN, LOW);
    
    Serial.begin(115200);

    txNumber=0;
    Rssi=0;

    RadioEvents.TxDone = OnTxDone;
    RadioEvents.TxTimeout = OnTxTimeout;
    RadioEvents.RxDone = OnRxDone;

    Radio.Init( &RadioEvents );
    Radio.SetChannel( RF_FREQUENCY );
    Radio.SetTxConfig( MODEM_LORA, TX_OUTPUT_POWER, 0, LORA_BANDWIDTH,
                                   LORA_SPREADING_FACTOR, LORA_CODINGRATE,
                                   LORA_PREAMBLE_LENGTH, LORA_FIX_LENGTH_PAYLOAD_ON,
                                   true, 0, 0, LORA_IQ_INVERSION_ON, 3000 );

    Radio.SetRxConfig( MODEM_LORA, LORA_BANDWIDTH, LORA_SPREADING_FACTOR,
                                   LORA_CODINGRATE, 0, LORA_PREAMBLE_LENGTH,
                                   LORA_SYMBOL_TIMEOUT, LORA_FIX_LENGTH_PAYLOAD_ON,
                                   0, true, 0, 0, LORA_IQ_INVERSION_ON, true );
    state=RX;
}



void loop()
{
  switch(state)
  {
    case TX:
      turnOnRGB(COLOR_SEND,0);
 
      delay(1);
      
      bytesRecvd = 0;
      digitalWrite(BUSY_PIN, HIGH);
      turnOnRGB(COLOR_JOINED,0); 
      while (bytesRecvd <= 9) {
        Serial.printf("\r\nentering serial function");
        recvBytesWithStartEndMarkers();
        }
      digitalWrite(BUSY_PIN, LOW);

      Serial.printf("\r\nread in %d bytes", bytesRecvd);
      turnOnRGB(COLOR_SEND,0);

      Serial.printf("\r\nsending packet");

      Radio.Send(tempBuffer, bytesRecvd);
      state=LOWPOWER;
      break;
    case RX:
      Serial.println("into RX mode");
      turnOnRGB(COLOR_RECEIVED,0);
        Radio.Rx( 0 );
        state=LOWPOWER;
        break;
    case LOWPOWER:
      lowPowerHandler();
        break;
        default:
            break;
  }
    Radio.IrqProcess( );
}

void OnTxDone( void )
{
  Serial.print("TX done......");
  turnOnRGB(0,0);
  state=RX;
}

void OnTxTimeout( void )
{
    Radio.Sleep( );
    Serial.print("TX Timeout......");
    state=TX;
}
void OnRxDone( uint8_t *payload, uint16_t size, int16_t rssi, int8_t snr )
{
    Rssi=rssi;
    rxSize=size;
    memcpy(rxpacket, payload, size );
    rxpacket[size]='\0';
    turnOnRGB(COLOR_RECEIVED,0);
    Radio.Sleep( );

    Serial.printf("\r\nreceived packet \"%s\" with Rssi %d , length %d\r\n",rxpacket,Rssi,rxSize);
    Serial.println("wait to send next packet");

    state=TX;
}

void recvBytesWithStartEndMarkers() {
  
  
  
  //Serial.println("start recieving");
  allReceived = false;
  
  
  while(allReceived == false) {
    if (Serial1.available() > 0) {
    //Serial.println("reading message");
    byte x = Serial1.read();
    if (x == startMarker) {
      //Serial.println("message start"); 
      bytesRecvd = 0; 
      inProgress = true;
      // blinkLED(2);
      // debugToPC("start received");
      }
      
    if(inProgress) {
      //Serial.println("reading message");
      tempBuffer[bytesRecvd] = x;
      bytesRecvd ++;
      }

    if (x == endMarker) {
      //Serial.println("message end"); 
      
      inProgress = false;
      allReceived = true;
      
        // save the number of bytes that were sent  
     
      }
     }
    }
} 

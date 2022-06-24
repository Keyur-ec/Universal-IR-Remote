#include <IRremote.h>

// Define sensor pin
const int RECV_PIN = D5;

// Define IR Receiver and Results Objects
IRrecv irrecv(RECV_PIN);
decode_results results;

int flag = HIGH;

void setup(){
  // Serial Monitor @ 9600 baud
  Serial.begin(9600);
  // Enable the IR Receiver
  irrecv.enableIRIn();
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, flag);
}

void loop(){
  if (irrecv.decode(&results)){
      Serial.print("        message from loop:: Hex code is recived from remote ");
      Serial.println(results.value, HEX); 
      irrecv.resume();

      switch(results.value){
        case 0x1FE48B7:
          digitalWrite(LED_BUILTIN, flag);
          flag = !flag;
          break;
      }
  }
}

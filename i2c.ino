#include <Wire.h>

#define LED_PIN1 13
#define LED_PIN2 10

void receiveEvent(int numBytes);

void setup() {
  Wire.begin(0x8);
  Wire.onReceive(receiveEvent);
  pinMode(LED_PIN1, OUTPUT);
  pinMode(LED_PIN2, OUTPUT);
  Serial.begin(9600);
}

void loop() {
}

void receiveEvent(int numBytes) {
  while (Wire.available()) {
    byte c = Wire.read();
    Serial.println(c);
    if (c == 1) {
      digitalWrite(LED_PIN1, HIGH);
      digitalWrite(LED_PIN2, HIGH);
    } else {
      digitalWrite(LED_PIN1, LOW)
      digitalWrite(LED_PIN2, LOW);
    }
  }
}

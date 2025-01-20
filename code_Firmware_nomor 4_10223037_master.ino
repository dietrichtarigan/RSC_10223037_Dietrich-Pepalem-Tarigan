// Arduino Master I2C

#include <Wire.h>

#define ledPin 9
#define slaveAddress 0x14

byte receivedData;
int potValue;

void setup() {
  Wire.begin(); // Inisialisasi sebagai Master
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // Baca nilai Potentiometer
  potValue = analogRead(A0);
  potValue = map(potValue, 0, 1023, 0, 255);

  // Kirim nilai PWM ke Slave
  Wire.beginTransmission(slaveAddress);
  Wire.write(potValue);
  Wire.endTransmission();

  // Minta nilai PWM dari Slave
  Wire.requestFrom(slaveAddress, 1);
  if (Wire.available()) {
    receivedData = Wire.read();
    analogWrite(ledPin, receivedData);
    Serial.print("Received from Slave: ");
    Serial.println(receivedData);
  }

  delay(100); // Delay sedikit sebelum iterasi berikutnya
}
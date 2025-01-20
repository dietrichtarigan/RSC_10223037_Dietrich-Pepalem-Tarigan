// Arduino Slave I2C

#include <Wire.h>

#define ledPin 9
#define potPin A0
#define slaveAddress 0x14

byte receivedData;
int potValue;

void setup() {
  Wire.begin(slaveAddress); // Inisialisasi sebagai Slave dengan alamat 0x14
  Wire.onReceive(receiveEvent); // Handler untuk menerima data
  Wire.onRequest(requestEvent); // Handler untuk mengirim data
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // Baca nilai Potentiometer
  potValue = analogRead(potPin);
  potValue = map(potValue, 0, 1023, 0, 255);

  // Atur LED sesuai data yang diterima
  analogWrite(ledPin, receivedData);

  delay(100); // Delay sedikit sebelum iterasi berikutnya
}

// Fungsi untuk menerima data dari Master
void receiveEvent(int numBytes) {
  while (Wire.available()) {
    receivedData = Wire.read();
    Serial.print("Received from Master: ");
    Serial.println(receivedData);
  }
}

// Fungsi untuk mengirim data ke Master saat diminta
void requestEvent() {
  Wire.write(potValue);
  Serial.print("Sent to Master: ");
  Serial.println(potValue);
}
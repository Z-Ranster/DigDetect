#include <Arduino.h>
#include <Encoder.h>
#include <TinyGPSPlus.h>
#include <SoftwareSerial.h>

// Encoder Definitions
// Rotary Encoder 1 models Boom Cylinder (reference Parts of an Excavator Arm image)
//i.e. up and down (y-axis) motion
#define inputCLK1 2
#define inputDT1 4
//Rotary Encoder 2 models Stick Cylinder (reference Parts of an Excavator Arm image)
//i.e. forward and back (x-axis) motion
#define inputCLK2 3
#define inputDT2 5
//Rotary Encoder 3 models Bucket Cylinder (reference Parts of an Excavator Arm image)
//i.e. bucket angle (loading/dumping) use x-axis and y-axis on a 45 degree angle
// Rotary encoder 3 is broken because we do not have enough interrupt pins on the Arduino Uno.
#define inputCLK3 7
#define inputDT3 6
// Encoder Definition
Encoder myEnc1(inputCLK1,inputDT1);
Encoder myEnc2(inputCLK2,inputDT2);
Encoder myEnc3(inputCLK3,inputDT3);
// Encoder Variables
float angleIncrement = 360/60;
long previousStateCLK1 = -999;
long previousStateCLK2 = -999;
long previousStateCLK3 = -999;

//LED Outputs
#define ledCW 8
#define ledCCW 9 

// GPS Definition
TinyGPSPlus gps;
// Software Serial Definition
#define rxPin 10
#define txPin 11
// Set up a new SoftwareSerial object
SoftwareSerial gpsSerial =  SoftwareSerial(rxPin, txPin);
float lati, longi, alti;

// Function to check the encoder values
long checkEncoder(Encoder encoderNum, long oldPosition, int encoderID){
  long newPosition = encoderNum.read();
  if (newPosition != oldPosition) {
    if (newPosition < oldPosition) {
      // CW
      digitalWrite(ledCW, HIGH);
      digitalWrite(ledCCW, LOW);
    } else { 
      // CCW
      digitalWrite(ledCW, LOW);
      digitalWrite(ledCCW, HIGH);
    }
    oldPosition = newPosition;

    return oldPosition;
  }
}

void setup() {
  // Set LED pins as outputs
  pinMode (ledCW, OUTPUT);
  pinMode (ledCCW, OUTPUT);

  // Define pin modes for TX and RX
  pinMode(rxPin, INPUT);
  pinMode(txPin, OUTPUT);

  // Setup Serial Monitor
  Serial.begin(9600);
  gpsSerial.begin(9600);

}

void loop() {
  // Initalize variables
  String serialStream = "$DDT";
  String dataValues[9];

  // Check Sensors
  previousStateCLK1 = checkEncoder(myEnc1, previousStateCLK1, 1);
  previousStateCLK2 = checkEncoder(myEnc2, previousStateCLK2, 2);
  previousStateCLK3 = checkEncoder(myEnc3, previousStateCLK3, 3);

  //Serial.println(gpsSerial.read());

  /*
  gpsSerial.listen();
  if (gpsSerial.available()){
    Serial.println("ReadingSerial");
    int s = gpsSerial.read();
    if (gps.encode(s)){
      //gps.f_get_position(&lati, &longi);
    }
  }
  */

  // Build Serial Data
  dataValues[0] = previousStateCLK1*angleIncrement;
  dataValues[1] = previousStateCLK2*angleIncrement;
  dataValues[2] = previousStateCLK3*angleIncrement;
  dataValues[3] = "3546.12574";
  dataValues[4] = "N";
  dataValues[5] = "07840.59113";
  dataValues[6] = "W";
  dataValues[7] = "225736.00";
  dataValues[8] = "A";

  // Convert data and build serial stream
  for (int i = 0; i < 9; i++){
    serialStream += "," + dataValues[i];
  }

  // Transmit Serial Data
  Serial.println(serialStream);

  delay(10);
}
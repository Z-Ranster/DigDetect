#include <Arduino.h>
#include <Encoder.h>

// Encoder Definitions
// Rotary Encoder 0 models rotation of the device (reference Parts of an Excavator Arm image)
// I am not sure if I can implement this due to the lack of interrupts. Only 2, 3, 18, 19, 20, 21 are available
// #define inputCLK3 17
// #define inputDT3 6
// Rotary Encoder 1 models Boom Cylinder (reference Parts of an Excavator Arm image)
// i.e. up and down (y-axis) motion
#define inputCLK1 2
#define inputDT1 3
// Rotary Encoder 2 models Stick Cylinder (reference Parts of an Excavator Arm image)
// i.e. forward and back (x-axis) motion
#define inputCLK2 20
#define inputDT2 21
// Rotary Encoder 3 models Bucket Cylinder (reference Parts of an Excavator Arm image)
// i.e. bucket angle (loading/dumping) use x-axis and y-axis on a 45 degree angle
#define inputCLK3 18
#define inputDT3 19
//  Encoder Variables
int resolution = 40;
float angleIncrement = 360 / resolution;
// Encoder Definition
Encoder myEnc1(inputCLK1, inputDT1);
float enc1ZeroDeg = 81;
float enc1Zero = enc1ZeroDeg / angleIncrement;
Encoder myEnc2(inputCLK2, inputDT2);
float enc2ZeroDeg = 45;
float enc2Zero = enc2ZeroDeg / angleIncrement;
Encoder myEnc3(inputCLK3, inputDT3);
float enc3ZeroDeg = 126;
float enc3Zero = enc3ZeroDeg / angleIncrement;

// Measured in degrees
long previousStateCLK1 = enc1ZeroDeg;
long previousStateCLK2 = enc2ZeroDeg;
long previousStateCLK3 = enc3ZeroDeg;
bool zeroButtonPressed = false;

// Zero-Button
#define zeroButton 11

void setup()
{
  // Define pin modes for zero button
  pinMode(zeroButton, INPUT);

  // Setup Serial Monitor
  Serial.begin(9600);

  // Set Encoder Zero Values
  myEnc1.write(enc1Zero);
  myEnc2.write(enc2Zero);
  myEnc3.write(enc3Zero);
}

void loop()
{
  // Initalize variables
  String serialStream = "DDT";
  String dataValues[4];
  float currentStateCLK1 = 0.0;
  float currentStateCLK2 = 0.0;
  float currentStateCLK3 = 0.0;

  // Check to See if Zero Button is Pressed
  if (digitalRead(zeroButton) == HIGH and zeroButtonPressed == false)
  {
    zeroButtonPressed = true;
    Serial.println("Zero Button Pressed");
    // Set values below for each encoder to the "Zero Location". Remember that the values will be multiplied by 6.
    currentStateCLK1 = enc1ZeroDeg;
    myEnc1.write(enc1Zero);
    currentStateCLK2 = enc2ZeroDeg;
    myEnc2.write(enc2Zero);
    currentStateCLK3 = enc3ZeroDeg;
    myEnc3.write(enc3Zero);
  }
  else if (digitalRead(zeroButton) == LOW and zeroButtonPressed == true)
  {
    zeroButtonPressed = false;
  }

  // Read Encoder Values
  // If the encoder values are different than zero then update the current state
  if (myEnc1.read() != 0)
  {
    currentStateCLK1 = myEnc1.read();
    currentStateCLK2 = myEnc2.read();
    currentStateCLK3 = myEnc3.read();
  }
  else
  {
    currentStateCLK1 = previousStateCLK1;
    currentStateCLK2 = previousStateCLK2;
    currentStateCLK3 = previousStateCLK3;
  }

  // Build Serial Data
  dataValues[0] = 0 * angleIncrement; // No Z-Rotation At This Time
  dataValues[1] = (currentStateCLK1 / resolution) * 360;
  dataValues[2] = (currentStateCLK2 / resolution) * 360;
  dataValues[3] = (currentStateCLK3 / resolution) * 360;

  // Update Previous State
  previousStateCLK1 = currentStateCLK1;
  previousStateCLK2 = currentStateCLK2;
  previousStateCLK3 = currentStateCLK3;

  // Convert data and build serial stream
  for (int i = 0; i < 4; i++)
  {
    serialStream += "," + dataValues[i];
  }

  // Transmit Serial Data
  Serial.println(serialStream);

  delay(10);
}
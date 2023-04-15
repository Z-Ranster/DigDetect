#include <Arduino.h>
#include <Encoder.h>

// Encoder Definitions
// Rotary Encoder 0 models rotation of the device (reference Parts of an Excavator Arm image)
// I am not sure if I can implement this due to the lack of interrupts. Only 2, 3, 18, 19, 20, 21 are available
// #define inputCLK3 17
// #define inputDT3 6
// Rotary Encoder 1 models Boom Cylinder (reference Parts of an Excavator Arm image)
// i.e. up and down (y-axis) motion
#define inputCLK1 3
#define inputDT1 2
// Rotary Encoder 2 models Stick Cylinder (reference Parts of an Excavator Arm image)
// i.e. forward and back (x-axis) motion
#define inputCLK2 20
#define inputDT2 21
// Rotary Encoder 3 models Bucket Cylinder (reference Parts of an Excavator Arm image)
// i.e. bucket angle (loading/dumping) use x-axis and y-axis on a 45 degree angle
#define inputCLK3 18
#define inputDT3 19
// Encoder Definition
Encoder myEnc1(inputCLK1, inputDT1);
Encoder myEnc2(inputCLK2, inputDT2);
Encoder myEnc3(inputCLK3, inputDT3);
//  Encoder Variables
float angleIncrement = 360 / 60;
long previousStateCLK1 = -999;
long previousStateCLK2 = -999;
long previousStateCLK3 = -999;
bool zeroButtonPressed = false;

// Zero-Button
#define zeroButton 11

// Function to check the encoder values
long checkEncoder(Encoder encoderNum, long oldPosition, int encoderID)
{
  long newPosition = encoderNum.read();
  if (newPosition != oldPosition)
  {

    // if (newPosition < oldPosition)
    // {
    //   // CW
    //   digitalWrite(ledCW, HIGH);
    //   digitalWrite(ledCCW, LOW);
    // }
    // else
    // {
    //   // CCW
    //   digitalWrite(ledCW, LOW);
    //   digitalWrite(ledCCW, HIGH);
    // }
    oldPosition = newPosition;
    return oldPosition;
  }
}

void setup()
{
  // Define pin modes for zero button
  pinMode(zeroButton, INPUT);

  // Setup Serial Monitor
  Serial.begin(9600);
}

void loop()
{
  // Initalize variables
  String serialStream = "DDT";
  String dataValues[3];
  float currentStateCLK1 = 0.0;
  float currentStateCLK2 = 0.0;
  float currentStateCLK3 = 0.0;

  // Check Sensors
  currentStateCLK1 = checkEncoder(myEnc1, previousStateCLK1, 1);
  currentStateCLK2 = checkEncoder(myEnc2, previousStateCLK2, 2);
  currentStateCLK3 = checkEncoder(myEnc3, previousStateCLK3, 3);

  // Check to See if Zero Button is Pressed
  if (digitalRead(zeroButton) == HIGH and zeroButtonPressed == false)
  {
    zeroButtonPressed = true;
    Serial.println("Zero Button Pressed");
    // previousStateCLK1 = -999;
    // previousStateCLK2 = -999;
    // previousStateCLK3 = -999;
    // myEnc1.write(0);
    // myEnc2.write(0);
    // myEnc3.write(0);
    // Set values below for each encoder to the "Zero Location". Remember that the values will be multiplied by 6.
    currentStateCLK1 = 70 / 6;
    myEnc1.write(70 / 6);
    currentStateCLK2 = 90 / 6;
    myEnc2.write(90 / 6);
    currentStateCLK3 = 60 / 6;
    myEnc3.write(60 / 6);
  }
  else if (digitalRead(zeroButton) == LOW and zeroButtonPressed == true)
  {
    zeroButtonPressed = false;
  }

  // Build Serial Data
  dataValues[0] = 0 * angleIncrement;
  dataValues[1] = currentStateCLK1 * angleIncrement;
  dataValues[2] = currentStateCLK2 * angleIncrement;
  dataValues[3] = currentStateCLK3 * angleIncrement;

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
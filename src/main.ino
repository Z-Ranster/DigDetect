// Include Arduino and Encoder Libraries
#include <Arduino.h>
#include <Encoder.h>

// Rotary Encoder Definitions
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

// Encoder Variables
int resolution = 40;                     // Number of detents (clicks) per revolution of the encoder
float angleIncrement = 360 / resolution; // Increment of rotation in degrees

// Encoder Definitions
Encoder myEnc1(inputCLK1, inputDT1);           // Boom Cylinder Encoder
float enc1ZeroDeg = 81;                        // Zero degree offset of Boom Cylinder
float enc1Zero = enc1ZeroDeg / angleIncrement; // Encoder value at zero degree offset
Encoder myEnc2(inputCLK2, inputDT2);           // Stick Cylinder Encoder
float enc2ZeroDeg = 45;                        // Zero degree offset of Stick Cylinder
float enc2Zero = enc2ZeroDeg / angleIncrement; // Encoder value at zero degree offset
Encoder myEnc3(inputCLK3, inputDT3);           // Bucket Cylinder Encoder
float enc3ZeroDeg = 126;                       // Zero degree offset of Bucket Cylinder
float enc3Zero = enc3ZeroDeg / angleIncrement; // Encoder value at zero degree offset

// Measured in degrees
long previousStateCLK1 = enc1ZeroDeg; // Previous state of Boom Cylinder Encoder
long previousStateCLK2 = enc2ZeroDeg; // Previous state of Stick Cylinder Encoder
long previousStateCLK3 = enc3ZeroDeg; // Previous state of Bucket Cylinder Encoder
bool zeroButtonPressed = false;       // Boolean to check if zero button is pressed

// Zero-Button
#define zeroButton 11 // Pin for Zero button

void setup()
{
  // Define pin modes for zero button
  pinMode(zeroButton, INPUT);

  // Setup Serial Monitor
  Serial.begin(9600);

  // Set Encoder Zero Values
  myEnc1.write(enc1Zero); // Set the Boom Cylinder Encoder to zero offset value
  myEnc2.write(enc2Zero); // Set the Stick Cylinder Encoder to zero offset value
  myEnc3.write(enc3Zero); // Set the Bucket Cylinder Encoder to zero offset value
}

void loop()
{
  // Initialize variables
  String serialStream = "DDT"; // Start building serial data with a header
  String dataValues[4];        // Array to store data values
  float currentStateCLK1 = 0.0;
  float currentStateCLK2 = 0.0;
  float currentStateCLK3 = 0.0;

  // Check to see if zero button is pressed
  if (digitalRead(zeroButton) == HIGH and zeroButtonPressed == false)
  {
    zeroButtonPressed = true; // Set boolean to true to prevent multiple presses
    // Set values below for each encoder to the "Zero Location". Remember that the values will be multiplied by 6.
    currentStateCLK1 = enc1ZeroDeg; // Set current state to encoder zero degrees
    myEnc1.write(enc1Zero);         // Write encoder zero value to encoder
    currentStateCLK2 = enc2ZeroDeg;
    myEnc2.write(enc2Zero);
    currentStateCLK3 = enc3ZeroDeg;
    myEnc3.write(enc3Zero);
  }
  else if (digitalRead(zeroButton) == LOW and zeroButtonPressed == true) // Zero button is released
  {
    zeroButtonPressed = false;
  }

  // Read Encoder Values
  // If the encoder values are different than zero then update the current state
  if (myEnc1.read() != 0) // Read the encoder value and check if it is not zero
  {
    currentStateCLK1 = myEnc1.read();
    currentStateCLK2 = myEnc2.read();
    currentStateCLK3 = myEnc3.read();
  }
  else // If encoder value is zero, then use the previous value
  {
    currentStateCLK1 = previousStateCLK1;
    currentStateCLK2 = previousStateCLK2;
    currentStateCLK3 = previousStateCLK3;
  }

  // Build Serial Data
  dataValues[0] = 0 * angleIncrement;                    // No Z-Rotation at this time
  dataValues[1] = (currentStateCLK1 / resolution) * 360; // Calculate the angle using the encoder value, resolution, and 360 degrees
  dataValues[2] = (currentStateCLK2 / resolution) * 360;
  dataValues[3] = (currentStateCLK3 / resolution) * 360;

  // Update Previous State
  previousStateCLK1 = currentStateCLK1; // Store the current state as previous state for the next loop
  previousStateCLK2 = currentStateCLK2;
  previousStateCLK3 = currentStateCLK3;

  // Convert data and build serial stream
  for (int i = 0; i < 4; i++) // Loop through each data value
  {
    serialStream += "," + dataValues[i]; // Add the data value to the serial stream separated by a comma
  }

  // Transmit Serial Data
  Serial.println(serialStream); // Print the serial stream to the Serial Monitor

  delay(10); // Delay for 10ms to avoid overloading the serial communication
}
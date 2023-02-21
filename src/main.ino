//Rotary Encoder inputs

// Rotary Encoder 1 models Boom Cylinder (reference Parts of an Excavator Arm image)
//i.e. up and down (y-axis) motion
#define inputCLK1 2
#define inputDT1 3 //Pin 3 allows Pulse Width Modulation (PWM)

//Rotary Encoder 2 models Stick Cylinder (reference Parts of an Excavator Arm image)
//i.e. forward and back (x-axis) motion
#define inputCLK2 4
#define inputDT2 5 //Pin 5 allows PWM

//Rotary Encoder 3 models Bucket Cylinder (reference Parts of an Excavator Arm image)
//i.e. bucket angle (loading/dumping) use x-axis and y-axis on a 45 degree angle
#define inputCLK3 7
#define inputDT3 6 //Pin 6 allows PWM

//LED Outputs
#define ledCW 8
#define ledCCW 9 

// Update the 20 value to be the number of increments per 360 dgree rotation
float angleIncrement = 360/40;

float counter1 = 0;
float currentStateCLK1;
float previousStateCLK1;

float counter2 = 0;
float currentStateCLK2; 
float previousStateCLK2;

float counter3 = 0;
float currentStateCLK3;
float previousStateCLK3;

String encdir1 = "";
String encdir2 = "";
String encdir3 = "";

void setup() {
  // Set encoder pins as inputs 
  // Encoder 1
  pinMode (inputCLK1, INPUT);
  pinMode (inputDT1, INPUT);

  // Encoder 2
  pinMode (inputCLK2, INPUT);
  pinMode (inputDT2, INPUT);

  // Encoder 3
  pinMode (inputCLK3, INPUT);
  pinMode (inputDT3, INPUT);

  // Set LED pins as outputs
  pinMode (ledCW, OUTPUT);
  pinMode (ledCCW, OUTPUT);

  // Setup Serial Monitor
  Serial.begin (9600);

  // Read the initial state of inputCLK1
  // Assign to previousStateCLK1 variable
  previousStateCLK1 = digitalRead(inputCLK1);

  // Read the initial state of inputCLK2
  // Assign to previousStateCLK2 variable
  previousStateCLK2 = digitalRead(inputCLK2);

  // Read the initial state of inputCLK3
  //Assign to previousStateCLK3 variable
  previousStateCLK3 = digitalRead(inputCLK3);

}

void loop() {
  // Initalize variables
  String serialStream = "$DDT,";
  float dataValues[6];

  // Check sensors
  dataValues[0] = checkEncoder1();
  dataValues[1] = checkEncoder2();
  dataValues[2] = checkEncoder3();

  // Convert data and build serial stream
  //Serial.println("TEST");
  // Fix code below
  Serial.println(sizeof(dataValues));
  //for (int i = 0; i <= sizeof(dataValues); i++){
  //  char tmpChr[6];
  //  dtostrf(dataValues[i], 6, 3, tmpChr);
  //  serialStream += "," + String(tmpChr);
  //}

  // Transmit Serial Data
  Serial.println(serialStream);
}

float checkEncoder1(){
  // Rotary Encoder 1

  // Read the current state of inputCLK1
  currentStateCLK1 = digitalRead(inputCLK1);

  // If the previous and the current state of the inputCLK2 are different then a 
  // pulse has occured
  if (currentStateCLK1 != previousStateCLK1) { 

    // If the inputDT1 state is different than the inputCLK2 state then the encoder
    // is rotating clockwise
    if (digitalRead(inputDT1) != currentStateCLK1) {
      counter1 += counter1*angleIncrement;
      //encdir1 = "CW";
      digitalWrite(ledCW, HIGH);
      digitalWrite(ledCCW, LOW);

    } else { 

      // Encoder is rotating counterclockwise
      counter1 -= counter1*angleIncrement;
      //encdir1 = "CCW";
      digitalWrite(ledCW, LOW);
      digitalWrite(ledCCW, HIGH);

    }
    // Removed to implement structured serial communication
    /*
    Serial.print("Direction Encoder 1: ");
    Serial.print(encdir1);
    Serial.print(" -- Value: ");
    Serial.println(counter1);
    Serial.println();   //Prints an empty line
    */

  }
  //Update previousStateCLK1 with the current state
  previousStateCLK1 = currentStateCLK1;

  return counter1;
}

float checkEncoder2(){
  // Rotary Encoder 2

  // Read the current state of inputCLK2
  currentStateCLK2 = digitalRead(inputCLK2);

  // If the previous and the current state of the inputCLK2 are different then a 
  // pulse has occured
  if (currentStateCLK2 != previousStateCLK2)  {

    // If the inputDT2 state is different than the inputCLK2 state then the encoder
    // is rotating clockwise
    if (digitalRead(inputDT2) != currentStateCLK2)  { 
      counter2 += counter2*angleIncrement;
      //encdir2 = "CW";
      digitalWrite(ledCW, HIGH);
      digitalWrite(ledCCW, LOW);

    } else  {

      // Encoder is rotating counterclockwise
      counter2 -= counter2*angleIncrement;
      //encdir2 = "CCW";
      digitalWrite(ledCW, LOW);
      digitalWrite(ledCCW, HIGH);

    }
    // Removed to implement structured serial communication
    /*
    Serial.print("Direction Encoder 2: ");
    Serial.print(encdir2);
    Serial.print(" -- Value: ");
    Serial.println(counter2);    
    Serial.println();   // Prints an empty line
    */
  }
  // Update previousStateCLK2 with the current state
  previousStateCLK2 = currentStateCLK2;

  return counter2;
}

float checkEncoder3(){
  // Rotary Encoder 3

  //Read the current state of inputCLK3
  currentStateCLK3 = digitalRead(inputCLK3);

  // If the previous and the current state of the inputCLK3 are different then a 
  // pulse has occured
  if (currentStateCLK3 != previousStateCLK3) {

    // If the inputDT3 state is different than the inputCLK3 state then the encoder
    // is rotating clockwise
    if (digitalRead(inputDT3) != currentStateCLK3) {
      counter3 += counter3*angleIncrement;
      //encdir3 = "CW";
      digitalWrite(ledCW, HIGH);
      digitalWrite(ledCCW, LOW);

    } else {

      //Encoder is rotating counterclockwise
      counter3 -= counter3*angleIncrement;
      //encdir3 = "CCW";
      digitalWrite(ledCW, LOW);
      digitalWrite(ledCCW, HIGH);

    }
    // Removed to implement structured serial communication
    /*
    Serial.print("Direction Encoder 3: ");
    Serial.print(encdir3);
    Serial.print(" -- Value: ");
    Serial.println(counter3);
    Serial.println();   //Prints an empty line
    */
  }
  //Update previousStateCLK3 with the current state
  previousStateCLK3 = currentStateCLK3;

  return counter3;
}
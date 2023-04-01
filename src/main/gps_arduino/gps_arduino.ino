#include <NMEAGPS.h> // include the NeoGPS library

// define the RX and TX pins for Serial3
#define SERIAL3_RX 14
#define SERIAL3_TX 15

NMEAGPS gps; // create a new NMEAGPS object to parse the GPS data

void setup()
{
  Serial.begin(9600);  // initialize the primary serial port at 9600 baud
  Serial3.begin(9600); // initialize Serial3 at 9600 baud
}

void loop()
{
  while (Serial3.available())
  { // check if there is any GPS data available
    if (gps.decode(Serial3.read()))
    {                             // if there is data available, decode it
      Serial.print("Latitude: "); // print the latitude
      // Serial.print(gps.latitude(), 6);    // use the latitude() function from the NMEAGPS library to get the latitude
      Serial.print(", Longitude: "); // print the longitude
      // Serial.println(gps.longitude(), 6); // use the longitude() function from the NMEAGPS library to get the longitude
    }
    else
    {
      Serial.println("No GPS data available");
    }
  }
}

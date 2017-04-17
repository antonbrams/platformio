


#include "Arduino.h"

#define PIN 4
#define INTERVAL 500

void setup () {
	pinMode(PIN, OUTPUT);
}

void loop () {
	digitalWrite(PIN, HIGH); delay(INTERVAL);
	digitalWrite(PIN,  LOW); delay(INTERVAL);
}



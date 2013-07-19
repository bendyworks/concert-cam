/*
 * Button.pde
 */

#include <Bounce.h>
// Create Bounce objects for each button.  The Bounce object
// automatically deals with contact chatter or "bounce", and
// it makes detecting changes very simple.
Bounce button = Bounce(10, 10);


void setup() {
  Serial.begin(9600);
  pinMode(10, INPUT_PULLUP);
  delay(1000);
}

void loop() {
  // Update the button.  There should not be any long
  // delays in loop(), so this runs repetitively at a rate
  // faster than the buttons could be pressed and released.
  button.update();

  if (button.fallingEdge()) {
    Keyboard.println("press");
  }
}


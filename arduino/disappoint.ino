//Function: Display disappointed facial expression on 16×8 LED matrix + sky-blue color on 12-LED RGB strip.
//Hardware: LED matrix (I2C addr:0x70), RGB NeoPixel strip (pin 3)

#include <Wire.h>
#include "Adafruit_LEDBackpack.h"
Adafruit_8x16matrix ematrix = Adafruit_8x16matrix();
#include <Adafruit_NeoPixel.h>

Adafruit_NeoPixel pixel = Adafruit_NeoPixel(12, 3, NEO_GRB + NEO_KHZ800);
uint8_t eyesm_bmp[16];

//Show disappointed face: sky-blue strip + disappointed bitmap on matrix
void showDisappointFace() {
  pixel.clear();
  pixel.fill(pixel.Color(51, 204, 255));
  pixel.show();

  //Matrix: assign disappointed face bitmap data
  eyesm_bmp[0] = B00000000;eyesm_bmp[1] = B00100000;eyesm_bmp[2] = B00100000;eyesm_bmp[3] = B00110000;eyesm_bmp[4] = B00011000;eyesm_bmp[5] = B00001110;eyesm_bmp[6] = B00000000;eyesm_bmp[7] = B00000000;eyesm_bmp[8] = B00000000;eyesm_bmp[9] = B00000000;eyesm_bmp[10] = B00001110;eyesm_bmp[11] = B00011000;eyesm_bmp[12] = B00110000;eyesm_bmp[13] = B00100000;eyesm_bmp[14] = B00100000;eyesm_bmp[15] = B00000000;
  ematrix.clear();
  ematrix.setRotation(0);
  ematrix.drawBitmap(0, 0, eyesm_bmp, 8, 16, 1);
  ematrix.writeDisplay();
}

//Initialize hardware: LED matrix + RGB strip
void setup() {
  ematrix.begin(0x70);
  pixel.begin();
  pixel.setBrightness(99);
  pixel.clear();
}

//continuously show disappointed face
void loop() {
  showDisappointFace(); 
  delay(1000);
}



# otto-bear

## Code Structure
- `python/`:
   `config.py`: Defines experiment stages and emotion actions
   `core.py`: Main state machine， controls emotion switching
- `arduino/`: Hardware code (4 emotions: neutral/sad/happy/disappoint + RGB strip)

## Hardware Details
- Controller: Arduino Nano
- 16×8 LED matrix: I2C address 0x70
- RGB strip: 12 LEDs, connected to pin 3
- RGB strip color：sky-blue  (RGB: 51, 204, 255)

## How to Integrate
Send `next_action` (from Python state machine) to Arduino via serial (triggers the emotion)

## Next Steps
Add voice interaction (audio clips) next week

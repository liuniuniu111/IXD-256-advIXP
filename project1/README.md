# Project 1 Stress Detect Bun  
## Introduction
This is a stress detection installation. As students, we often experience stress, and recently, squishy toys have become incredibly popular for their stress-relieving properties. This project aims to use the M5 stack as a tool to measure people’s stress levels.
<img src="annotated-IMG_3492.JPG" alt="idea" width="300"/>

## State Diagram
The process begins by checking for input. If input is detected and the count is less than 30, one light on the LED strip will illuminate green. When the input count reaches 30, it triggers a stress emergency status, causing the LED strip to display a red blinking animation. Finally, if the count exceeds 30, it will reset the count and start the process over.  

<img src="flowchart.jpg" alt="flowchart" width="300"/>

## Hardware
- M5 S3 Lite
- LED Strip

## Firmware

[Project1 Code link](stresscount.py)    


**1. Initialization**
```Python
M5.begin()
rgb2 = RGB(io=38, n=30, type="SK6812")
rgb2.set_brightness(30)
rgb2.fill_color(0x000000)
```

- Purpose: This initializes the M5 stack and sets up the RGB LED strip.    

- Inputs:
    - io=38: Defines the GPIO pin used for controlling the LED strip.
    - n=30: Specifies the number of LEDs in the strip.
    - type="SK6812": Indicates the type of RGB LED being used.    

- Outputs:
    - Sets the brightness of the LEDs to 30.
    - Fills the strip with the color black (turns off all LEDs).    

- Behavior: This setup prepares the RGB LED strip for use, allowing for color changes based on user input.

**2. Input Pin Configuration**
```Python
input_pin = Pin(6, mode=Pin.IN, pull=Pin.PULL_UP)
input_pin_val = input_pin.value()
```
- Purpose: This configures a digital input pin to read button presses.    

- Inputs:
    - Pin(6): Uses GPIO pin 6 as the input pin.
    - mode=Pin.IN: Sets the pin as an input.
    - pull=Pin.PULL_UP: Activates the internal pull-up resistor, ensuring the pin reads high when not pressed.    

- Outputs:
    - The initial value of the input pin is stored in input_pin_val.    

- Behavior: This configuration allows the prototype to detect button presses by monitoring the state of the pin.

**3. Toggle Function**
```Python
def output_toggle():
    global toggle_count, emergency_mode

    print('Button toggled. Current count:', toggle_count)

    if toggle_count < 30:
        set_led_color(toggle_count, 0, 255, 0)  
        toggle_count += 1

        if toggle_count == 30:
            print("Emergency mode triggered!")
            emergency_mode = True
            emergency_red_flash()
            toggle_count = 0 
```
- Purpose: This function handles the logic when the button is toggled (pressed).
  
- Inputs:
    - toggle_count: Keeps track of how many times the button has been pressed.
    
- Outputs:
    - TSets the corresponding LED on the strip to green (0, 255, 0) for each press until it reaches 30.   

- Behavior: When the button is pressed, it increments the toggle_count, visually indicates the count with green LEDs, and triggers emergency mode upon reaching 30 presses.   

**4. Emergency Mode Activation**
```Python
def emergency_red_flash():
    for _ in range(5):  
        for i in range(30):
            set_led_color(i, 255, 0, 0)  
        time.sleep(0.5)  
        rgb2.fill_color(0x000000)  
        time.sleep(0.5)  
    rgb2.fill_color(0x000000)  
```
- Purpose: This function creates a flashing red light sequence when emergency mode is triggered.  
  
- Inputs: No direct inputs, but it is called when toggle_count reaches 30.    
    
- Outputs:
    - Sets all LEDs to red (255, 0, 0) and then turns them off in a flashing sequence.    

- Behavior: This visually indicates an emergency status through a series of red flashes, alerting the user that emergency mode has been activated.

**5. Main Loop**
```Python
while True:  
    M5.update()  

    if input_pin_val == True:
        if input_pin.value() == False: 
            print('Input pin changed from high to low')
            output_toggle()

    input_pin_val = input_pin.value()  
    time.sleep_ms(100) 
```
- Purpose: This loop continuously checks for button presses.    
  
- Inputs:
    - input_pin.value(): Reads the current state of the input pin.

- Outputs:
    - Calls output_toggle() if a change in the pin state is detected (from high to low).    

- Behavior: The loop facilitates the real-time detection of button presses, allowing the prototype to respond to user input promptly.

## Physical Components
- 3d print base
- Squishy  

<img src="base.jpg" alt="base" width="300"/>

## Project outcome

<img src="IMG_9919.jpg" alt="final" width="300"/>  


Click [here](./video.mp4) to download or view the video.

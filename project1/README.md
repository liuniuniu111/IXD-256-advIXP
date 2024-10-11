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

## Physical Components
- 3d print base
- Squishy  

<img src="base.jpg" alt="base" width="300"/>

## Project outcome

<img src="IMG_9919.jpg" alt="final" width="300"/>  


Click [here](./video.mp4) to download or view the video.

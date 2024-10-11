# Project 1 Stress Detect Bun  
## Introduction
This is a stress detection installation. As students, we often experience stress, and recently, squishy toys have become incredibly popular for their stress-relieving properties. This project aims to use the M5 stack as a tool to measure people’s stress levels.
<img src="annotated-IMG_3492.JPG" alt="idea" width="300"/>

## State Diagram
The process begins by checking for input. If input is detected and the count is less than 30, one light on the LED strip will illuminate green. When the input count reaches 30, it triggers a stress emergency status, causing the LED strip to display a red blinking animation. Finally, if the count exceeds 30, it will reset the count and start the process over.  

Here is a flowchart:
<img src="flowchart.jpg" alt="flowchart" width="300"/>

## Hardware
- M5 S3 Lite
- LED Strip

## Firmware

[Project1 Code link](stresscount.py)

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

## Physical Components
- 3d print base
- Squishy
Here is the base image:
<img src="base.jpg" alt="base" width="300"/>

## Project outcome
Here is the final image:  
<img src="IMG_9919.jpg" alt="final" width="300"/>  


<video width="600" controls>
  <source src="video.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

#hardware
led_red = LED(24)
led_blue = LED(14)
led_green = LED(15)

#GUI DEFINITIONS
box = Tk()
box.title("blinking lights")
box.geometry("400x240")
Font = tkinter.font.Font(family= "Helvetica", size = 10)
button_frame = Frame(box)
button_frame.pack()


#EVENT FUNCTION
def ledToggle1():
    if led_red.is_lit:
        led_red.off()
        ledButton1["text"] = "Turn RED_LED On"
    else:
        led_red.on()
        ledButton1["text"] = "Turn RED_LED Off"
        
def ledToggle2():
    if led_blue.is_lit:
        led_blue.off()
        ledButton2["text"] = "Turn BLUE_LED On"
    else:
        led_blue.on()
        ledButton2["text"] = "Turn BLUE_LED Off"
        
def ledToggle3():
    if led_green.is_lit:
        led_green.off()
        ledButton3["text"] = "Turn GREEN_LED On"
    else:
        led_green.on()
        ledButton3["text"] = "Turn GREEN_LED Off"
        
def exit():
    RPi.GPIO.cleanup()
    button_frame.destroy()
    
    
#WIDGETS
ledButton1 = Button(button_frame, text = 'Turn RED_LED On',  command = ledToggle1, bg = 'red', height = 1, width = 24)
ledButton1.grid(row=1,column=1)

ledButton2 = Button(button_frame, text = 'Turn BLUE_LED On',  command = ledToggle2, bg = 'blue', height = 1, width = 24)
ledButton2.grid(row=2,column=1)

ledButton3 = Button(button_frame, text = 'Turn GREEN_LED On', command = ledToggle3, bg = 'green', height = 1, width = 24)
ledButton3.grid(row=3,column=1)

blink_button = Button(button_frame,text="EXIT", command= exit,bg = 'white',height=1,width=24)
blink_button.grid(row=4,column=1)

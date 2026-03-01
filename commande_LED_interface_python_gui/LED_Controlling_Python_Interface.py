import serial 
import tkinter 

arduinoData = serial.Serial('COM6', 9600)

def led_on():
    arduinoData.write(b'1')
def led_off():
    arduinoData.write(b'0')
led_controlm_window = tkinter.Tk()
led_controlm_window.title("LED Control")

button= tkinter.Button
btn1 = button(led_controlm_window, text="LED ON", command=led_on)

btn2 = button(led_controlm_window, text="LED OFF", command=led_off)

btn1.grid(row=0, column=1)
btn2.grid(row=1, column=1)
led_controlm_window.mainloop()
input("Press Enter to exit")
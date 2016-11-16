import mido
from array import*
from mido import Message
import rtmidi

midiin=rtmidi.MidiIn
available_ports=midiin.get_ports()
'''
arr=[]
with input as mido.open_input('HDA Intel HDMI: 0'):
        for message in input:
            print(message)
	    arr.append(message.note) 	

'''
'''
with input as mido.open_input('ZynAddSubFX'): #give input port in the quotes
	for message in input:
		print(message)
		arr.append(message.note) 
'''


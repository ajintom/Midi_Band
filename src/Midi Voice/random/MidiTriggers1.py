import rtmidi_python as rtmidi
import time

c4=0x30
d4=0x32
e4=0x34
f4=0x35
g4=0x37
b4=0x3B
c5=0x3C
d5=0x3E
e5=0x40
f5=0x41
g5=0x43
a5=0x45
b5=0x47
c6=0x48

on=0x90
off=0x80

vel=100

def msg (note):
    midi_out.send_message([on,note,vel])
    time.sleep(0.2)
    midi_out.send_message([off,note,vel])



midi_out = rtmidi.MidiOut()
midi_out.open_port(0)


h=[c4,c4,d4,c4,f4,e4]

for x in range(0,6):
    a=input('hit 1')
    if (a==1):
        msg(h[x])




#midi_out.send_message([0x80, 48, 100])




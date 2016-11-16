import pyaudio
import numpy
import matplotlib.pyplot as plt
from threading import Thread

print "11111111"

import rtmidi_python as rtmidi
import time

c4=0x30
cs4=0x31
d4=0x32
ds4=0x33
e4=0x34
f4=0x35
fs4=0x36
g4=0x37
gs4=0x38
a4=0x39
as4=0x3A
b4=0x3B
c5=0x3C
cs5=0x3D
d5=0x3E
ds5=0x3F
e5=0x40
f5=0x41
fs5=0x42
g5=0x43
gs5=0x44
a5=0x45
as5=0x46
b5=0x47
c6=0x48
cs6=0x49
d6=0x4A
ds6=0x4B
e6=0x4C
f6=0x4D
fs6=0x4E
g6=0x4F
gs6=0x50
a6=0x51
as6=0x52
b6=0x53
c7=0x54
cs7=0x55
d7=0x56
ds7=0x57
e7=0x58
f7=0x59
fs7=0x5A
g7=0x5B
gs7=0x5C
a7=0x5D
as7=0x5E
b7=0x5F

on=0x90
off=0x80

vel=100

def msg (note):
    midi_out.send_message([on,note,vel])
    time.sleep(0.5)
    midi_out.send_message([off,note,vel])



midi_out = rtmidi.MidiOut()
midi_out.open_port(0)
h=[b4,c5,f5,e5,b4,c5,e5,d5,b4,c5,f5,e5,d5,e5,c5,f4,c6,c6,g6,g6,a6,a6,g6,f6,f6,e6,e6,d6,d6,c6,c6,g6,c7,c6,as6,a6,c6,g6,c7,c6,as6,g6,f6,e6,c6,c6,d6,c6,f6,e6,c6,c6,d6,c6,g6,f6,c6,f6,f6,e6,d6,c6,g6,g6,f6,e6,c6,d6,c6,c6,d6,c6,c6,d6,c6,c6,b4,c5,f5,e5,b4,c5,e5,d5,b4,c5,f5,e5,d5,e5,c5,f4,e4,d4,c4,c4,d4,c4,f4,e4,c4,c4,d4,c4,g4,f4,c4,c4,c4,g4,c5,c4,f4,e4,c5,c5,g5,f4,e4,d4,c4,c4,d4,c4,f4,e4,c4,c4,d4,c4,g4,f4,c4,c4,c4,g4,c5,c4,f4,e4,c5,c5,g5,f4,e4,d4]

#h=[c4,d4,e4,f4,g4,a4,b4,c4,c4,g4,g4,a4,a4,g4,f4,f4,e4,e4,d4,d4,c4,c4,g4,c5,c4,as4,a4,c4,g4,c5,c4,as4,g4,f4,e4,c4,c4,d4,c4,f4,e4,c4,c4,d4,c4,g4,f4,c4,f4,f4,e4,c4,d4,c4,c5,c5,g5,f4,e4,d4,c4,c4,d4,c4,f4,e4,c4,c4,d4,c4,g4,f4,c4,c4,c4,g4,c5,c4,f4,e4,c5,c5,g5,f4,e4,d4,c4,c4,d4,c4,f4,e4,c4,c4,d4,c4,g4,f4,c4,c4,c4,g4,c5,c4,f4,e4,c5,c5,g5,f4,e4,d4,c4,c4,d4,c4,f4,e4,c4,c4,d4,c4,g4,f4,c4,c4,c4,g4,c5,c4,f4,e4,c5,c5,g5,f4,e4,d4]b6,e7,d7,d7,c7,c7,b6,a6,g6,a6,c7,b6,b6,a6,a6,g6,a6,a6,g6,fs6,d6,d6,e6,c6






#midi_out.send_message([0x80, 48, 100])





RATE=16000
RECORD_SECONDS = 600
CHUNKSIZE = 1024
peakinfo = 0;
flag = 0;
triggger = 0;
# initialize portaudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNKSIZE, input_device_index=3)

envelope = [] # A python-list of chunks(numpy.ndarray)
recording = []
mem = []

peakinfo=0
flag=0
trigger=0

for num in range(0, int(RATE / CHUNKSIZE * RECORD_SECONDS)):
    data = stream.read(CHUNKSIZE)
    chunk=numpy.fromstring(data, dtype=numpy.int16)
    frame=chunk.tolist();
    if (num==0):
        for i in range(0,50):
            recording.append(abs(frame[i]));
        for i in range(50,1024):
            for k in range(i-50,i):
                mem.append(abs(frame[k]))
            recording.append(max(mem))
            if(max(mem)>20000):
                peakinfo=peakinfo+1;
                print peakinfo
            if((peakinfo>30)and(flag==0)):
                flag=1;
                trigger=trigger+1;
                #msg(h[trigger-1])
                
                msgthread=Thread(target=msg,args=(h[trigger-1],))
                msgthread.start()
                print h[trigger-1];
            if(max(mem)<5000):
                peakinfo=0
                flag=0
            del mem[:]
        mem=frame[974:1024];
        for i in range(len(mem)-1):
            mem[i]=abs(mem[i]);
    else:
        for i in range(0,1024):
            recording.append(max(mem));
            if(max(mem)>20000):
                peakinfo=peakinfo+1;
            if((peakinfo>30)and(flag==0)):
                flag=1;
                trigger=trigger+1;
                #msg(h[trigger-1])
                
                msgthread=Thread(target=msg,args=(h[trigger-1],))
                msgthread.start()
                print h[trigger-1];
            if(max(mem)<5000):
                peakinfo=0
                flag=0
            del mem[0]
            mem.append(abs(chunk[i]))

#Convert the list of numpy-arrays into a 1D array (column-wise)
#numpydata = numpy.hstack(frames)
plt.plot(recording);
plt.show();
# close stream
stream.stop_stream()
stream.close()
p.terminate()

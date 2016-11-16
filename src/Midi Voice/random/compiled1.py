import pyaudio
import numpy
import matplotlib.pyplot as plt
from threading import Thread
import matplotlib.animation as animation

print "11111111"

import rtmidi_python as rtmidi
import time

fig = plt.figure();
ax1 = fig.add_subplot(1,1,1)
xar = [];
yar = [];

def update(y):
    xar.append(time.time());
    yar.append(y);
    ax1.plot(xar,yar);

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
    time.sleep(0.5)
    midi_out.send_message([off,note,vel])



midi_out = rtmidi.MidiOut()
midi_out.open_port(0)


h=[c4,c4,d4,c4,f4,e4,c4,c4,d4,c4,g4,f4,c4,c4]

#midi_out.send_message([0x80, 48, 100])

RATE=16000
RECORD_SECONDS = 10
CHUNKSIZE = 1024
peakinfo = 0;
flag = 0;
triggger = 0;
    # initialize portaudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNKSIZE, input_device_index=0)

envelope = [] # A python-list of chunks(numpy.ndarray)
recording = []
mem = []

peakinfo=0
flag=0
trigger=0
update(0);
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
                #print peakinfo
            if((peakinfo>30)and(flag==0)):
                flag=1;
                trigger=trigger+1;
                #msg(h[trigger-1])
                update(max(mem));
                msgthread=Thread(target=msg,args=(h[trigger-1],))
                msgthread.start()
                print trigger;
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
                update(max(mem));
                msgthread=Thread(target=msg,args=(h[trigger-1],))
                msgthread.start()
                print trigger;
            if(max(mem)<5000):
                peakinfo=0
                flag=0
            del mem[0]
            mem.append(abs(chunk[i]))
#Convert the list of numpy-arrays into a 1D array (column-wise)
#numpydata = numpy.hstack(frames)
#plt.plot(recording);
#plt.show();
# close stream
stream.stop_stream()
stream.close()
p.terminate()

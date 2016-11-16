import pyaudio
import numpy
import matplotlib.pyplot as plt

RATE=16000
RECORD_SECONDS = 10
CHUNKSIZE = 1024
peakinfo = 0;
flag = 0;
triggger = 0;
# initialize portaudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNKSIZE)

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
                print trigger;
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

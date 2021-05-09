import pickle
from record import record
import librosa
import numpy as np

path = '__path of averages pickle file__'

#function to find closest match
def matchit(one, two):
    diff = [x-y for (x, y) in zip(one, two)]
    s=0
    for x in diff:
        s=s+(x*x)
    return s

def filt(l):
    c = [0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1]
    for j in c:
        l.pop(j)
    l.pop(2)
    l.pop(2)
    l.pop(-1)
    return l

#getting the recorded features
open_file = open(path, "rb")
features = pickle.load(open_file)
open_file.close()
op = features[0]
op.pop(0)
cl = features[1]
cl.pop(0)

#obtaining audio sample fv
arr = record()
arr = arr.astype(np.float32)
mfcc = librosa.feature.mfcc(y=arr, sr=8000)
fv = []
for x in (mfcc):
    s = int(sum(x)/len(x))
    fv.append(s)
fv = filt(fv)
# print(fv)
# print(op)
# print(cl)

errop = matchit(fv, op)
errcl = matchit(fv, cl)

if errop<errcl:
    print('OPEN')
else:
    print('CLOSE')

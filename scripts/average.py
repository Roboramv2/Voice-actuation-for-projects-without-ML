from matplotlib import pyplot as plt
import pickle
path1 = '__path of pickle of mfcc vectors of 6 recordings of command 1__'
path2 = '__path of pickle of mfcc vectors of 6 recordings of command 2__'
path = '__path to save averages for both commands__'

#get recorded command1 fvs
open_file = open(path1, "rb")
openfvs = pickle.load(open_file)
open_file.close()

#get recorded command2 fvs
open_file = open(path2, "rb")
closefvs = pickle.load(open_file)
open_file.close()

#filter that removes redundant data, this is in my case for open vs close. varies per command word choice
def filt(l):
    c = [0, 0, 0, -1, -1, -1, -1, -1, -1, -1]
    for i in l:
        for j in c:
            i.pop(j)
        i.pop(2)
        i.pop(2)
        i.pop(-1)
    return l

#removing unwanted elements
openfvs = filt(openfvs)
closefvs = filt(closefvs)

#averaging
openfvs = [int(sum(x)/len(x)) for x in zip(*openfvs)]
closefvs = [int(sum(x)/len(x)) for x in zip(*closefvs)]

#creating indices
x = [i for i in range(7)]

#saving pickle
fvs = [openfvs, closefvs]
open_file = open('averages', "wb")
pickle.dump(fvs, open_file)
open_file.close()

#plotting command 1
plt.plot(x, openfvs, color= 'lightblue')
#plotting command 2
plt.plot(x, closefvs, color= 'darkgreen')

plt.show()
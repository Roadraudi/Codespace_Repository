import numpy as np

temp = [-1.5, -1.2, 0.0, 24.2]      #zufällige Temperatur
np_temp = np.array(temp)    #wird jetzt als Vektor gespeichert
print(np_temp)
print(np_temp*2)

print(np.array([42, 127], np.int8))     #begrenzung auf 8Bit
print(np.array([42, 128], np.int8))     # erstes Bit ist vorzeichen also größtmögliche Zahl 01111111 = 127

#numpy array indexing
print(temp[0])
print(temp[0] + temp[1])    #-1.5+(-1.2)

#numpy array slicing
print(temp[1:3])
print(temp[2:])







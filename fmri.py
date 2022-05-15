import numpy as np


original = np.random.randint(0,100, size = (20,100))

noise = np.random.normal(size=9)

participants = np.zeros((10, 20, 100))
participants[0] = original

for i in range(len(noise)):
    participants[i+1] = original + noise[i]

print(participants.shape)


    

#RDMS
import numpy as np
import torch
import torchvision
import matplotlib.pyplot as plt
import seaborn as sns

network = Net()

#make a loop for each img


def show_activation_layer_rdm(activation_layers, layer_name):
    df = pd.DataFrame(activation_layers[layer_name])

    corr = df.corr()
    rdm = 1-corr

    d = sn.heatmap(dement, annot=True)
    d.set_title(layern_name)
    plt.savefig(layer_name + ".png")
    plt.show()

for param_tensor in model.state_dict():
    show_activation_layer_rdm(activation_layers, param_tensor)

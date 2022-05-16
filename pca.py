import numpy as np
from sklearn.decomposition import PCA

def pca(array):
    pca = PCA(n_components=1)
    pca.fit(array)
    return(pca.components_)

#train_models.py
import os
import cPickle
import numpy as np
from scipy.io.wavfile import read
from sklearn.mixture import GaussianMixture as GMM 
import python_speech_features as mfcc
from sklearn import preprocessing
import warnings
warnings.filterwarnings("ignore")


def get_MFCC(sr,audio):
    features = mfcc.mfcc(audio,sr,0.025, 0.02, 13,appendEnergy = False)
    # python_speech_features.base.mfcc(signal, samplerate=16000, winlen=0.025, winstep=0.01, numcep=13, nfilt=26, nfft=512, lowfreq=0, highfreq=None, preemph=0.97, ceplifter=22, appendEnergy=True, winfunc=<function <lambda>>)
    print(features.shape)
    features = preprocessing.scale(features)
    print(features)
    return features



source   = "Dataset/Sad"
dest     = "Model/"         
files    = [os.path.join(source,f) for f in os.listdir(source) if 
             f.endswith('.wav')] 
features = np.asarray(());

for f in files:
    sr,audio = read(f)
    vector   = get_MFCC(sr,audio)
    if features.size == 0:
        features = vector
    else:
        features = np.vstack((features, vector))

gmm = GMM(n_components = 8, max_iter = 200, covariance_type='diag',n_init = 3)
gmm.fit(features)
picklefile = f.split("/")[-2].split(".wav")[0]+".gmm"

# model saved as male.gmm
cPickle.dump(gmm,open(dest + picklefile,'w'))
print 'modeling completed for gender:',picklefile

# test_gender.py
import os
import cPickle
import numpy as np
from scipy.io.wavfile import read
import python_speech_features as mfcc
from sklearn import preprocessing
import warnings

warnings.filterwarnings("ignore")


def get_MFCC(sr, audio):
    features = mfcc.mfcc(audio, sr, 0.025, 0.01, 13, nfft=1024,appendEnergy=False)
    feat = np.asarray(())

    for i in range(features.shape[0]):
        temp = features[i, :]
        if np.isnan(np.min(temp)):
            continue
        else:
            if feat.size == 0:
                feat = temp
            else:
                feat = np.vstack((feat, temp))
    features = feat;
    features = preprocessing.scale(features)
    return features


# path to testing data
sourcepath = "Test/"
# path to saved models
modelpath = "Model/"

gmm_files = [os.path.join(modelpath, fname) for fname in
             os.listdir(modelpath) if fname.endswith('.gmm')]
models = [cPickle.load(open(fname, 'r')) for fname in gmm_files]
genders = [fname.split("/")[-1].split(".gmm")[0] for fname
           in gmm_files]
files = [os.path.join(sourcepath, f) for f in os.listdir(sourcepath)
         if f.endswith(".wav")]

for f in files:
    print f.split("/")[-1]
    sr, audio = read(f)
    features = get_MFCC(sr, audio)
    scores = None
    log_likelihood = np.zeros(len(models))
    #print(len(models))
    for i in range(len(models)):
        gmm = models[i]  # checking with each model one by one
        scores = np.array(gmm.score(features))
        log_likelihood[i] = scores.sum()
    winner = np.argmax(log_likelihood)
    print "\tdetected as - ", genders[winner],"\n\tscores:Neutral ", log_likelihood[0], ",Fear ", log_likelihood[1],",Angry ", log_likelihood[2],",Disgust ", log_likelihood[3],",PleasantSurprise ", log_likelihood[4],",Sad ", log_likelihood[5],",Happy ", log_likelihood[6], "\n"

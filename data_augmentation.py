from deepspeech import Model
import scipy.io.wavfile as wav
import os

import sox
import random
import os
import numpy as np
import pandas as pd
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="path to train.csv file (i.e., directory of txt chua content)")
ap.add_argument("-o", "--output", required=True,
	help="path to output csv")
ap.add_argument("-w", "--wav", required=True,
help="path to wav folder")
args = ap.parse_args()

dir_path = args.wav
# files = [os.path.join(dir_path,f) for f in os.listdir(dir_path)]
data = pd.read_csv(args.input)
data_augment = []

for i in range(len(data)):
    data_augment.append({'wav_filename': data.iloc[i]['wav_filename'], 'wav_filesize': data.iloc[i]['wav_filesize'], 'transcript': data.iloc[i]['transcript']})


for i in range(len(data)):
    file_name = data.iloc[i]['wav_filename'].split('/')[-1]
    if np.random.rand() < 0.7:
        r = random.randint(1,6)
        tfm = sox.Transformer()
        if r == 1:
            tfm.chorus()
            out_path = dir_path + '/' + file_name.split('.')[0] + '_chorus.wav'
            tfm.build(data.iloc[i]['wav_filename'], out_path)
            data_augment.append({'wav_filename': out_path, 'wav_filesize': data.iloc[i]['wav_filesize'], 'transcript': data.iloc[i]['transcript']})
        if r == 2:
            tfm.echo()
            out_path = dir_path + '/' + file_name.split('.')[0] + '_echo.wav'
            tfm.build(data.iloc[i]['wav_filename'], out_path)
            data_augment.append({'wav_filename': out_path, 'wav_filesize': data.iloc[i]['wav_filesize'], 'transcript': data.iloc[i]['transcript']})
        if r == 3:
            tfm.pitch(2)
            out_path = dir_path + '/' + file_name.split('.')[0] + '_pitch.wav'
            tfm.build(data.iloc[i]['wav_filename'], out_path)
            data_augment.append({'wav_filename': out_path, 'wav_filesize': data.iloc[i]['wav_filesize'], 'transcript': data.iloc[i]['transcript']})
        if r == 4:
            tfm.reverb()
            out_path = dir_path + '/' + file_name.split('.')[0] + '_reverb.wav'
            tfm.build(data.iloc[i]['wav_filename'], out_path)
            data_augment.append({'wav_filename': out_path, 'wav_filesize': data.iloc[i]['wav_filesize'], 'transcript': data.iloc[i]['transcript']})
        if r == 5:
            tfm.speed(1.3)
            out_path = dir_path + '/' + file_name.split('.')[0] + '_speed.wav'
            tfm.build(data.iloc[i]['wav_filename'], out_path)
            data_augment.append({'wav_filename': out_path, 'wav_filesize': data.iloc[i]['wav_filesize'], 'transcript': data.iloc[i]['transcript']})
        if r == 6:
            tfm.tempo(1.4)
            out_path = dir_path + '/' + file_name.split('.')[0] + '_tempo.wav'
            tfm.build(data.iloc[i]['wav_filename'], out_path)
            data_augment.append({'wav_filename': out_path, 'wav_filesize': data.iloc[i]['wav_filesize'], 'transcript': data.iloc[i]['transcript']})

df = pd.DataFrame(data_augment)
path_train_augment = args.output + '/train_augment.csv'
df.to_csv(path_train_augment,index = False)
# create transformer

# tfm.chorus()

# tfm.echo()

# tfm.pitch(2)

# tfm.reverb()

# tfm.speed(1.3)

# tfm.tempo(1.4)
# create the output file.
# tfm.build('/home/nhatnt/Documents/speech2text/VIVOSDEV01_R002.wav', '/home/nhatnt/Documents/speech2text/VIVOSDEV01_R002_tempo.wav')
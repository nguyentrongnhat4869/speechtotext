import numpy as np 
import pickle
import os
import pandas as pd 
import scipy.io.wavfile
import wave
import random
import argparse

# Khai bao cac list 
data_dict = []
train_dict = []
dev_dict = []
test_dict = []

# Doc file txt
# lines = open("/home/nhatnt/Documents/speech2text/tughi/tughi.txt").read().splitlines()

# # Doc file text theo tung dong
# for line in lines:
#     items = line.split() # Cat dong text theo ' ' thanh 1 list cac tu        
#     fileid = items[0] # Lay phan tu dau tien cua list là ten file wav khong duoi
#     text = " ".join(items[1:]).lower() # Lay phan label cho file wav bang cac them cac khoang trang va chuyen thanh chu thuong
#     text = text.replace(":", "") # Bo dau :
#     text = text.replace("\n", "")
#     text = text.replace("?", " ")
#     text = text.replace(",", " ")
#     text = text.replace("'", " ")
#     text = text.replace(".", " ")
#     text = text.replace("ǀ", " ")

#     wav_name = items[0] + '.wav' # Them duoi cho file wav
#     wav_folder = wav_name.split('_')[0] # Cat wave name theo '_' lay phan dau do la ten folder  
#     wav_path = '/home/nhatnt/Documents/speech2text/vivos/train/waves/' + wav_folder + '/' + wav_name # Full path cua file wav

#     wav_sig = wave.open(wav_path) # Doc file wav
#     wav_size = wav_sig.getnframes() # Lay length file wav

#     data_dict.append({'wav_filename': wav_path, 'wav_filesize': wav_size, 'transcript': text}) # Them vao list data_dict cac dictionary dang {key: value}, o dang nay se dua duoc ve csv nhu ben duoi 

# lines_ = open("/home/nhatnt/Documents/speech2text/vivos/test/prompts.txt").read().splitlines()

# for line_ in lines_:
#     items = line_.split()             
#     fileid = items[0]
#     text = " ".join(items[1:]).lower()
#     text = text.replace(":", "")
#     text = text.replace("?", " ")
#     text = text.replace(",", " ")
#     text = text.replace("'", " ")
#     text = text.replace(".", " ")
#     text = text.replace("ǀ", " ")
#     text = text.replace("\n", "")
    
#     wav_name = items[0] + '.wav'
#     wav_folder = wav_name.split('_')[0]
#     wav_path = '/home/nhatnt/Documents/speech2text/vivos/test/waves/' + wav_folder + '/' + wav_name

#     wav_sig = wave.open(wav_path)
#     wav_size = wav_sig.getnframes()

#     test_dict.append({'wav_filename': wav_path, 'wav_filesize': wav_size, 'transcript': text})

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="path to input text")
ap.add_argument("-p", "--path", required=True,
	help="path to wav file")
ap.add_argument("-o", "--output", required=True,
help="path to output")
args = ap.parse_args()

lines = open(args.input).read().splitlines()
# lines_fpt = open("/home/nhatnt/Downloads/FPTOpenSpeechData_Set001_V0.1/fpt_open_set001_v1.txt").read().splitlines()

for line in lines:
    items = line.split()             
    text = " ".join(items[1:]).lower()
    text = text.replace(":", "")
    text = text.replace("?", " ")
    text = text.replace(",", " ")
    text = text.replace("'", " ")
    text = text.replace(".", " ")
    text = text.replace("ǀ", " ")
    text = text.replace("\n", "")
    
    wav_name = items[0].split('/')[-1] + '.wav'

    wav_path = args.path + '/' + wav_name
    
    wav_sig = wave.open(wav_path)
    wav_size = wav_sig.getnframes()

    data_dict.append({'wav_filename': wav_path, 'wav_filesize': wav_size, 'transcript': text})

# random.shuffle(data_dict)
train_dict = data_dict
dev_dict   = data_dict[4:6]
test_dict   = data_dict[5:7]
print(len(train_dict), len(dev_dict), len(test_dict))

############### Tao file csv ###############################
df_train = pd.DataFrame(train_dict)
train_path = args.output + '/train.csv'
df_train.to_csv(train_path, index = False)

df_dev = pd.DataFrame(dev_dict)
dev_path = args.output + '/dev.csv'
df_dev.to_csv(dev_path, index = False)

df_test = pd.DataFrame(test_dict)
test_path = args.output + '/test.csv'
df_test.to_csv(test_path, index = False)

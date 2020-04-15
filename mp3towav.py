import os 
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="path to mp3 folfer")
ap.add_argument("-o", "--output", required=True,
	help="path to wav folder")
args = ap.parse_args()

dir_path = args.input

files = [os.path.join(dir_path, f) for f in os.listdir(dir_path)]

for file in files:
    file_name = file.split('/')[-1]
    wav_path = args.output + '/' + file_name.split('.')[0] + '.wav'  
    os.system('ffmpeg -i {} -acodec pcm_s16le -ac 1 -ar 16000 {}'.format(file, wav_path))
    
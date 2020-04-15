import re
import argparse
# code nay dung de tien xu ly text truoc khi build language model, chuyen sang dang UNICODE
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="path to input text (i.e., directory of txt chua content)")
ap.add_argument("-o", "--output", required=True,
	help="path to output text")
args = ap.parse_args()

# infile = "/home/nhatnt/Documents/speech2text/vietnamese_model/vocabulary_pre.txt"
# outfile = "/home/nhatnt/Documents/speech2text/vietnamese_model/vocabulary_lm.txt"

infile = args.input
outfile = args.output

j = 0
with open(infile, 'r') as fr, open(outfile, 'w') as fw:
    for line in fr:
        line = ' '.join(re.findall(r"\w+|[^\w\s]", line.strip().lower(), re.UNICODE))

        fw.write(line)
        fw.write('\n')

        j += 1
        if j % 100000 == 0:
            print(str(j) + ' ' + line)
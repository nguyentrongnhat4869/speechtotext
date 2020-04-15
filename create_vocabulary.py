import numpy as np

content = open("/home/nhatnt/Documents/speech2text/vietnamese_model/vocabulary.txt").read()
content = content.replace(":", "")
lines = content.splitlines()
output = []
for line in lines:
    items = line.split()
    fileid = items[0]
    text = " ".join(items[1:]).lower()
    text = text.replace("?", " ")
    text = text.replace(",", " ")
    text = text.replace("'", " ")
    text = text.replace(".", " ")
    text = text.replace("ǀ", " ")
    content = text
    output.append(content)
text = "\n".join(output)
open("/home/nhatnt/Documents/speech2text/vietnamese_model/vocabulary_pre.txt", "w").write(text)
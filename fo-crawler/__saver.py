# Saver for save

import os

def load_saver(fp):
    if os.path.isfile(fp):
        with open(fp,'r') as f:
            return int(f.read())
    else:
        return 0

def save_saver(fp,line):
    with open(fp,'w') as f:
        f.write(str(line))

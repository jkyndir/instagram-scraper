import os
def add_prefix(fldr_path, prefix):
    fnms = os.listdir(fldr_path)
    for fn in fnms:
        os.rename(os.path.join(fldr_path, fn), os.path.join(fldr_path, prefix+fn))

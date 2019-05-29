from __future__ import print_function

import os
import sys
import shutil
import random


def move_data(folder, data_folder):

    if os.path.isdir(os.path.join(folder, "train")):
        print("Train folder already exists, Exiting")
        return
    shutil.move(data_folder, os.path.join(folder, "train"))

    val_path = os.path.join(folder, "val")
    train_path = os.path.join(folder, "train")
    if not os.path.isdir(val_path):
        os.makedirs(val_path)

    dir = os.listdir(train_path)
    for i in range(20):
        tt = random.choice(dir)
        shutil.move(os.path.join(train_path, tt), val_path)

if __name__ == '__main__':
    move_data(sys.argv[1], sys.argv[2])

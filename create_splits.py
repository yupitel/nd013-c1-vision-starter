import argparse
import glob
import os
import random

import numpy as np

from utils import get_module_logger
import shutil


def split(source, destination):
    """
    Create three splits from the processed records. The files should be moved to new folders in the
    same directory. This folder should be named train, val and test.

    args:
        - source [str]: source data directory, contains the processed tf records
        - destination [str]: destination data directory, contains 3 sub folders: train / val / test
    """
    # TODO: Implement function
    logger.info(source)
    logger.info(destination)

    # get data
    files = [filename for filename in glob.glob(f'{source}/*.tfrecord')]

    filelen = len(files)
    np.random.shuffle(files)
    # split files
    # train and val / test  8 : 2
    # train / test 8 : 2
    val_idx = int(0.8 * 0.8 * filelen)
    test_idx = int(0.8 * filelen)
    train_src, val_src, test_src = np.split(files, [val_idx, test_idx])

    # create directory
    train_dir = os.path.join(destination, 'train')
    val_dir   = os.path.join(destination, 'val')
    test_dir  = os.path.join(destination, 'test')

    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    # copy file
    for file in train_src:
        shutil.move(file, train_dir)
    for file in val_src:
        shutil.move(file, val_dir)
    for file in test_src:
        shutil.move(file, test_dir)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--source', required=True,
                        help='source data directory')
    parser.add_argument('--destination', required=True,
                        help='destination data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.source, args.destination)
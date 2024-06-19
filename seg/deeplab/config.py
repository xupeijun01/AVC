# ----------------------------------------
# Written by Yude Wang
# ----------------------------------------
import torch
import argparse
import os
import sys
import cv2
import time

config_dict = {
    'EXP_NAME': 'deeplabv1',
    'GPUS': 1,
    'DATA_NAME': 'VOCDataset',
    'DATA_YEAR': 2012,
    'DATA_AUG': True,
    'DATA_WORKERS': 0,
    'DATA_MEAN': [0.485, 0.456, 0.406],
    'DATA_STD': [0.229, 0.224, 0.225],
    'DATA_RANDOMCROP': 448,
    'DATA_RANDOMSCALE': [0.5, 1.5],
    'DATA_RANDOM_H': 10,
    'DATA_RANDOM_S': 10,
    'DATA_RANDOM_V': 10,
    'DATA_RANDOMFLIP': 0.5,
    'DATA_PSEUDO_GT': '../data/out_rw',
    'DATA_FEATURE_DIR': None,

    'MODEL_NAME': 'deeplabv1',
    'MODEL_BACKBONE': 'resnet38',
    'MODEL_BACKBONE_PRETRAIN': True,
    'MODEL_NUM_CLASSES': 21,
    'MODEL_FREEZEBN': False,
    'MODEL_BACKBONE_DILATED': True,
    'MODEL_BACKBONE_MULTIGRID': False,
    'MODEL_BACKBONE_DEEPBASE': True,

    'TRAIN_LR': 0.001,
    'TRAIN_MOMENTUM': 0.9,
    'TRAIN_WEIGHT_DECAY': 0.0005,
    'TRAIN_BN_MOM': 0.0003,
    'TRAIN_POWER': 0.9,
    'TRAIN_BATCHES': 5,
    'TRAIN_SHUFFLE': True,
    'TRAIN_MINEPOCH': 0,
    'TRAIN_ITERATION': 45000,
    'TRAIN_TBLOG': True,

    'TEST_MULTISCALE': [0.5, 0.75, 1.0, 1.25, 1.5],
    'TEST_FLIP': True,
    'TEST_CRF': True,
    'TEST_BATCHES': 1,
}

config_dict['ROOT_DIR'] = os.path.abspath('../')
config_dict['MODEL_SAVE_DIR'] = os.path.join(config_dict['ROOT_DIR'], 'data')
config_dict['TRAIN_CKPT'] = None
config_dict['LOG_DIR'] = os.path.join(config_dict['ROOT_DIR'], 'log', config_dict['EXP_NAME'])
config_dict['TEST_CKPT'] = os.path.join(config_dict['ROOT_DIR'],
                                        'data/deeplabv1_resnet38_VOCDataset_epoch20.pth')

sys.path.insert(0, os.path.join(config_dict['ROOT_DIR'], 'lib'))

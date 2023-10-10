# -*- coding: utf-8 -*-

import pathlib, shutil, os, sys
import prepare_folders as pf
import subprocess
if not pf.is_colab:
  # If running locally, there's a good chance your env will need this in order to not crash upon np.matmul() or similar operations.
  os.environ['KMP_DUPLICATE_LIB_OK']='TRUE'

PROJECT_DIR = os.path.abspath(os.getcwd())
USE_ADABINS = True

if pf.is_colab:
  if pf.google_drive is not True:
    root_path = f'/content'
    model_path = '/content/models' 
else:
  root_path = os.getcwd()
  model_path = f'{root_path}/models'

model_256_downloaded = False
model_512_downloaded = False
model_secondary_downloaded = False

multipip_res = subprocess.run(['pip', 'install', 'lpips', 'datetime', 'timm', 'ftfy', 'einops', 'pytorch-lightning', 'omegaconf'], stdout=subprocess.PIPE).stdout.decode('utf-8')
print(multipip_res)

if pf.is_colab:
  subprocess.run(['apt', 'install', 'imagemagick'], stdout=subprocess.PIPE).stdout.decode('utf-8')

try:
  from CLIP import clip
except:
  if not os.path.exists("CLIP"):
    pf.gitclone("https://github.com/openai/CLIP")
  sys.path.append(f'{PROJECT_DIR}/CLIP')

try:
  from guided_diffusion.script_util import create_model_and_diffusion
except:
  if not os.path.exists("guided-diffusion"):
    pf.gitclone("https://github.com/crowsonkb/guided-diffusion")
  sys.path.append(f'{PROJECT_DIR}/guided-diffusion')

try:
  from resize_right import resize
except:
  if not os.path.exists("ResizeRight"):
    pf.gitclone("https://github.com/assafshocher/ResizeRight.git")
  sys.path.append(f'{PROJECT_DIR}/ResizeRight')

try:
  import py3d_tools
except:
  if not os.path.exists('pytorch3d-lite'):
    pf.gitclone("https://github.com/MSFTserver/pytorch3d-lite.git")
  sys.path.append(f'{PROJECT_DIR}/pytorch3d-lite')

try:
  from midas.dpt_depth import DPTDepthModel
except:
  if not os.path.exists('MiDaS'):
    gitclone("https://github.com/isl-org/MiDaS.git")
  if not os.path.exists('MiDaS/midas_utils.py'):
    shutil.move('MiDaS/utils.py', 'MiDaS/midas_utils.py')
  if not os.path.exists(f'{model_path}/dpt_large-midas-2f21e586.pt'):
    wget("https://github.com/intel-isl/DPT/releases/download/1_0/dpt_large-midas-2f21e586.pt", model_path)
  sys.path.append(f'{PROJECT_DIR}/MiDaS')

try:
  sys.path.append(PROJECT_DIR)
  import disco_xform_utils as dxf
except:
  if not os.path.exists("disco-diffusion"):
    gitclone("https://github.com/alembics/disco-diffusion.git")
  if os.path.exists('disco_xform_utils.py') is not True:
    shutil.move('disco-diffusion/disco_xform_utils.py', 'disco_xform_utils.py')
  sys.path.append(PROJECT_DIR)

import torch
from dataclasses import dataclass
from functools import partial
import cv2
import pandas as pd
import gc
import io
import math
import timm
from IPython import display
import lpips
from PIL import Image, ImageOps
import requests
from glob import glob
import json
from types import SimpleNamespace
from torch import nn
from torch.nn import functional as F
import torchvision.transforms as T
import torchvision.transforms.functional as TF
from tqdm.notebook import tqdm
from CLIP import clip
from resize_right import resize
from guided_diffusion.script_util import create_model_and_diffusion, model_and_diffusion_defaults
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import random
from ipywidgets import Output
import hashlib
from functools import partial
if is_colab:
  os.chdir('/content')
  from google.colab import files
else:
  os.chdir(f'{PROJECT_DIR}')
from IPython.display import Image as ipyimg
from numpy import asarray
from einops import rearrange, repeat
import torch, torchvision
import time
from omegaconf import OmegaConf
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# AdaBins stuff
if USE_ADABINS:
  try:
    from infer import InferenceHelper
  except:
    if os.path.exists("AdaBins") is not True:
      gitclone("https://github.com/shariqfarooq123/AdaBins.git")
    if not os.path.exists(f'{PROJECT_DIR}/pretrained/AdaBins_nyu.pt'):
      createPath(f'{PROJECT_DIR}/pretrained')
      wget("https://cloudflare-ipfs.com/ipfs/Qmd2mMnDLWePKmgfS8m6ntAg4nhV5VkUyAydYBp8cWWeB7/AdaBins_nyu.pt", f'{PROJECT_DIR}/pretrained')
    sys.path.append(f'{PROJECT_DIR}/AdaBins')
  from infer import InferenceHelper
  MAX_ADABINS_AREA = 500000

import torch
DEVICE = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print('Using device:', DEVICE)
device = DEVICE # At least one of the modules expects this name..

if torch.cuda.get_device_capability(DEVICE) == (8,0): ## A100 fix thanks to Emad
  print('Disabling CUDNN for A100 gpu', file=sys.stderr)
  torch.backends.cudnn.enabled = False
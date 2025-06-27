# clip_dinoiser/resources.py
import torch
from omegaconf import OmegaConf
import importlib.resources as pkg_resources

def load_config(cfg_name='clip_dinoiser.yaml'):
    with pkg_resources.path('clip_dinoiser.configs', cfg_name) as cfg_path:
        return OmegaConf.load(cfg_path)

def load_checkpoint(checkpoint_name='last.pt'):
    with pkg_resources.path('clip_dinoiser.checkpoints', checkpoint_name) as ckpt_path:
        return torch.load(ckpt_path, map_location='cpu')
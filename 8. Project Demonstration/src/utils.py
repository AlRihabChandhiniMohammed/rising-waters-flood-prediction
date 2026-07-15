import os
import random
import numpy as np

def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)


def ensure_directory(path):
    os.makedirs(path, exist_ok=True)


def save_plot(fig, filepath):
    ensure_directory(os.path.dirname(filepath))
    fig.savefig(filepath, bbox_inches='tight')


def load_config(path="config.yaml"):
    if os.path.exists(path):
        import yaml
        with open(path, 'r') as f:
            return yaml.safe_load(f)
    return {}



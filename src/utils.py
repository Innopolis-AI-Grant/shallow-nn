"""Basic Utilities"""

import os
import random
import shutil
from pathlib import Path

import numpy as np
import orjson
import torch


def from_current_file(path: str) -> Path:
    """Makes path relative to the current file

    Args:
        path (str): filesystem path

    Returns:
        Path: path relative to the current file
    """
    dirname = os.path.dirname(__file__)
    return Path(os.path.join(dirname, path)).absolute()


def set_seed(seed: int = 420):
    """Sets random, seed for torch and numpy

    Args:
        seed (int, optional). Defaults to 420.
    """
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
    if torch.backends.mps.is_available():
        torch.mps.manual_seed(seed)


def remove_dir(path: str | Path):
    """Removes directory recursively

    Args:
        path (str): path to directory
    """
    shutil.rmtree(path, ignore_errors=True)


def load_json(path: str | Path, return_empty_if_not_found: bool = False) -> dict:
    if return_empty_if_not_found and not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return orjson.loads(f.read())


def save_json(path: str | Path, data: dict):
    with open(path, "wb") as f:
        f.write(
            orjson.dumps(
                data,
                option=orjson.OPT_SORT_KEYS
                + orjson.OPT_SERIALIZE_NUMPY
                + orjson.OPT_INDENT_2,
            )
        )

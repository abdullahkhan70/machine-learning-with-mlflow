import os
from box.exceptions import BoxValueError
import yaml
from ml_project import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

# 26:16


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """ reads yaml file and returns.

      Args:
          path_to_yaml (str): path like input

      Raises:
          ValueError: if yaml file i sempty
          e: empty file

      Returns:
          ConfigBox: Configure type.
      """
    try:
        with open(path_to_yaml) as yaml_f:
            content = yaml.safe_load(yaml_f)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        return e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """ Create a list of directories

    Args:
        path_to_directories (list): listnof path of directories.
        ignore_log (bool, optional): ignore if multiple_dirs is to be created. Defaults to False 
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """ Save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved to json file.
    """
    with open(path, "w") as file:
        json.dump(data, file, indent=4)
    logger.info(f"Json file save at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """ Load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfiigBox: data as class attributes instead of dict
    """
    with open(path) as file:
        content = json.load(file)

    logger.info(f"Json file loaded successfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path) -> Any:
    """ Save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file.    
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """ Load binary file.

    Args:
        path (path): path to binary file.

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file.

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"

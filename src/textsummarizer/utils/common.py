import os
from box.exceptions import BoxValueError
import yaml
from textsummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@emsure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns 
    
    Args:
        path_to_yaml (Path): path like input
        
    Raises:
        ValueError: if the path does not exist or is not a file
        e: empty file
        
    Returns:
        ConfigBox: ConfigBox type
    """
    
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"Path {path_to_yaml} does not exist or is not a file.")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """Creates list of directories.
    
    Args:
        path_to_directories (list): List of directory paths to create.
        ignore_log (bool): ignore if multiple dirs is to be created. Default is False.
    """
    
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory {path} created successfully or already exists.")
            
@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB
    
    Args:
        path (Path): path to file or directory
    
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB"    


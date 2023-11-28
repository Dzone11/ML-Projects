import os
import sys

import numpy as np
import pandas as pd
from src.exception import CustomException
import dill




def save_object(file_path, obj):
    """
    This function saves the object in the file path provided
    :param file_path: str
    :param obj: object
    :return: None
    """
    try:
        dir_path = os.path.dirname(file_path)
        
        os.makedirs(dir_path, exist_ok = True)
        
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
            
    except Exception as e:
        raise CustomException(e, sys)
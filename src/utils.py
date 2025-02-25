import os
import sys 
from src.logger import logging 
from src.exception import CustomException
import numpy as np
import pandas as pd
import dill 
from sklearn.metrics import r2_score


def evaluate_model(X_train, y_train,X_test,y_test,models):
    try:
        report = {}

        for i in range(len(list(models))-1):

            model = list(models.values())[i]

            model.fit(X_train, y_train)

            y_pred = model.predict(X_test)

            train_model_score = r2_score(y_test,y_pred)

            test_model_score = r2_score(y_test,y_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        CustomException(e,sys)

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok = True)
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        CustomException(e,sys)

def load_object(file_path): 
    try:
        with open(file_path,'rb') as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e,sys)

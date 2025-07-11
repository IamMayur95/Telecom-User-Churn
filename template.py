import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    "src/__init__.py",
    "src/helper.py",    
    "src/data_ingestion.py",
    "src/data_transformation.py",
    "src/data_validation.py",
    "src/model_trainer.py",
    "src/model_evaluation.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "app.py"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir!="":
        os.makedirs(filedir, exist_ok= True)
        logging.info(f"Creating directory {filedir} for the files {filename}")


    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath , "w") as f:
            pass 
            logging.info(f"Creating empty file : {filepath}")

    else:
        logging.info(f"{filename} is already exists")

        

    
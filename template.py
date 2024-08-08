import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    "logs",
    f"src/__init__.py",
    f"src/docRag/__init__.py",
    f"src/docRag/config/__init__.py", 
    f"src/docRag/config/configuration.py", 
    f"src/docRag/data_ingestion/__init__.py", 
    f"src/docRag/data_ingestion/data_insert.py", 
    f"src/docRag/data_preprocess/__init__.py",
    f"src/docRag/data_preprocess/embed.py", 
    f"src/docRag/data_preprocess/index.py", 
    f"src/docRag/data_ingestion/finetune.py", 
    f"src/docRag/data_ingestion/preprocess.py", 
    f"src/docRag/finetune/__init__.py", 
    f"src/docRag/finetune/finetune.py",  
    f"src/docRag/qna/__init__.py",
    f"src/docRag/qna/generate_answers.py",
    f"src/docRag/qna/question_answers.py",
    f"src/docRag/utils/__init__.py",
    f"src/docRag/utils/common.py",
    ".gitignore", 
    "Dockerfile",
    "README.md",
    "app.py", 
    "requirements.txt"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")
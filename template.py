# for end to end projects we need lots of files  and folders and we need to manage our code, so instead of creatig those file maunally , we will creat one python script and and write one logic here

# Import some libraries
import os #operating system
from pathlib import Path #path 
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')   #time the code is executed and the error message


project_name = "mlProject"

#first it will create a src folder which will contain the project files    
list_of_files = [
    ".github/workflows/.gitkeep", # we need this for cicd deplyoment using github action
    f"src/{project_name}/__init__.py", #all the constructors will be insde the  src folder
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml", # all of the configuration of the project
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    #"test.py"             #to create another file just write here


]




for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath) #separating directory/folder from filesystem/path

#checking if folder exsits or not, if not then create a new directory and log the information
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

#chekcing if file exists or not, if not then create a new file and log the information
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

#if everything is right, just pass the infor, that it exists
    else:
        logging.info(f"{filename} is already exists")

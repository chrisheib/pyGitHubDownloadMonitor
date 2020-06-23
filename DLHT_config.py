import configparser
import os

def ExePath(file):
    if file:
        return os.path.dirname(os.path.abspath(__file__))+'/'+file
    else:
        return os.path.dirname(os.path.abspath(__file__))+'/'

def configRead(section, key, default=''):
    try:
        config = configparser.ConfigParser()
        config.read(ExePath('conf.ini'))
        return config[section][key]
    except:
        return default

def configReadBool(section, key, default=False):
    if configRead(section, key, str(default)).lower() == "true":
        return True
    else:
        return False

def getRepoData():
    return configRead("GitHub","Username"), configRead("GitHub","RepositoryName")

def ShowPicture():
    return configReadBool("Settings","OpenPictureOnRun")

def CropToOneMonth():
    return configReadBool("Settings","CropToOneMonth")

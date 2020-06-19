import configparser
import os

def ExePath(file):
    if file:
        return os.path.dirname(os.path.abspath(__file__))+'/'+file
    else:
        return os.path.dirname(os.path.abspath(__file__))+'/'

def getApiKey():
    config = configparser.ConfigParser()
    config.read(ExePath('conf.ini'))
    return config["GitHub"]["APIKey"]

def getRepoData():
    config = configparser.ConfigParser()
    config.read(ExePath('conf.ini'))
    data = config["GitHub"]
    return data["Username"], data["RepositoryName"]

def ShowPicture():
    config = configparser.ConfigParser()
    config.read(ExePath('conf.ini'))
    data = config["Settings"]
    return data["OpenPictureOnRun"] == "True"

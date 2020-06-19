import configparser
import os

def getApiKey():
    config = configparser.ConfigParser()
    config.read(os.path.dirname(os.path.abspath(__file__))+'/conf.ini')
    return config["GitHub"]["APIKey"]

def getRepoData():
    config = configparser.ConfigParser()
    print(os.path.dirname(os.path.abspath(__file__)))
    config.read(os.path.dirname(os.path.abspath(__file__))+'/conf.ini')
    data = config["GitHub"]
    return data["Username"], data["RepositoryName"]

def ShowPicture():
    config = configparser.ConfigParser()
    config.read(os.path.dirname(os.path.abspath(__file__))+'/conf.ini')
    data = config["Settings"]
    return data["OpenPictureOnRun"] == "True"

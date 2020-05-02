import configparser

def getApiKey():
    config = configparser.ConfigParser()
    config.read('conf.ini')
    return config["GitHub"]["APIKey"]

def getRepoData():
    config = configparser.ConfigParser()
    config.read('conf.ini')
    data = config["GitHub"]
    return data["Username"], data["RepositoryName"]
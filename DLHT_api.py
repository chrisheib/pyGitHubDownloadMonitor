import requests
import DLHT_config as conf

def getReleaseList():
    name, repo = conf.getRepoData()
    request = requests.get('https://api.github.com/repos/'+name+'/'+repo+'/releases')
    return request.json()

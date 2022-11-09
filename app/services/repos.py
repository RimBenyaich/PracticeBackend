from datetime import datetime
import requests
from ..utils import functions

async def getLanguagesInformation(date: datetime):
    query = "https://api.github.com/search/repositories?q=created:<"+ date.isoformat()+"Z&sort=stars&order=desc"

    json_repos = requests.get(query)
    repos_dict = json_repos.json()
    arr = []

    for key, value in repos_dict.items():
        if key == "items":
            arr = value

    occurences = functions.getLanguagesInfo(arr)

    return occurences

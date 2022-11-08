from datetime import datetime
import requests

async def getRepos(date: datetime):
    query = "https://api.github.com/search/repositories?q=created:<"+ date.isoformat()+"Z&sort=stars&order=desc"

    r = requests.get(query)

    return r.json()
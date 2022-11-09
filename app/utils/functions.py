
def getAllLanguages(repos_list: list):
    languages = []
    for repo in repos_list:
        if repo["language"]:
            languages.append(repo["language"])

    languages_list = list(dict.fromkeys(languages))

    return languages_list

def getLanguagesInfo(repos_list: list):
    languages_list = getAllLanguages(repos_list)
    languages_infos = {}
    for language in languages_list:
        languages_infos.update({language: {"occurences": 0, "list": []}})
    
    for repo in repos_list:
        if repo["language"]:
            languages_infos[repo["language"]]["occurences"] += 1
            languages_infos[repo["language"]]["list"].append(repo["url"])
    
    return languages_infos
    
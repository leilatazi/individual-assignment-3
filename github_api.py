# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 19:24:24 2018

@author: Leila
"""
#%%

#Using Github’s API, create a function that:
#• takes all repositories from your account
#• prints a short description of each repository, with its name, number
#of stars, main language, and url

#GET /users/:username/repos 

def get_repos(username):
    
    import requests

    url = "https://api.github.com/users/" + username + "/repos"
    
    response = requests.get(url)
    
    repos = response.json()
    
    repos_list = []
    
    for repo in repos :
        d = {"name":repo["name"],"stargazers_count": repo["stargazers_count"],"language":repo["language"]}
        repos_list.append(d)
        
    return repos_list
    
get_repos("leilatazi")
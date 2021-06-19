# 09/14/2020
import git, os
from os.path import *
from BashColors import C

class GithubRepos:
    def __init__(self):
        self.gr = GithubRepos
        self.repoList = []
        
    def getCurrentProjectRepo(self):
        currentProjectURL = 'https://github.com/iypc-team/CurrentProject'
        
        localURL = os.path.join(os.curdir, basename(currentProjectURL))
        print(basename(currentProjectURL))
        if not exists(localURL):
            currentProjectRepo = git.Repo.clone_from(currentProjectURL, localURL)
            self.repoList.append(currentProjectRepo)
        else: print(f'{C.HEADER}{basename(localURL)} already exists')
    
    def getCoLabRepo(self):
        thisRepo = None
        colabURL = 'https://github.com/iypc-team/CoLab'
        self.updateRepoList(name=colabURL)
        localURL = os.path.join(os.path.curdir, basename(colabURL))
        if not exists(localURL):
            thisRepo = git.Repo.clone_from(colabURL, localURL)
            self.repoList.append(thisRepo)
            print(f'{C.Green}{thisRepo}')
        else: print(f'{C.Red}{thisRepo}')

    def listRemotes(self):
        print(f'{C.Blue}Remotes:')
        for rpo in self.repoList:
            print(rpo)
            print(f'{rpo}')

    def updateRepoList(self, name):
        if not name in self.repoList:
            self.repoList.append(name)
            
gr = GithubRepos()
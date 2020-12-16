import git
from git import Repo
from time import sleep

# repo = Repo("/home/drinosan/Documents/Git/titanic/titanic-own")

repo = git.Repo("/home/drinosan/Documents/Git/titanic/titanic-own")

while True:
    current = repo.head.commit
    repo.remotes.origin.pull()
    if current != repo.head.commit:
        repo.remotes.origin.pull()
    else:
        print("Nothing new")

    sleep(3600)

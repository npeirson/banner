# Collects and reports the data to our github repository
# Probably going to keep the math functions separate (for getting avgs, etc)

# imports
import urllib2
import getpass
from github import Github # http://pygithub.readthedocs.io/en/latest/introduction.html

# check for internet connection
def netCheck():
    try:
        urllib2.urlopen('http://google.com', timeout=5) # timeout high cuz forest etc
        print('- Internet Connection GOOD')
        return True
    except urllib2.URLError as err:
        print('- No internet connection!')
        return False

def loginGit():
    user = input('Username: ')
    password = getpass.getpass()
    g = Github("user", "password") # create github instance
    for repo in g.get_user().get_repos():
        print('- Now in repository:' + repo.name)

# pulls most recent log data into a markdown file
# then commits and pushes it to github
# done in command line becaus PyGit and PyGitHub documentation is shit

# imports
import urllib2
import getpass
import os
import time

def netCheck():
    print('- Looking for internet connection...')
    try:
        urllib2.urlopen('http://google.com', timeout=5) # timeout high cuz forest etc
        print('- Internet Connection GOOD')
        return True
    except urllib2.URLError as err:
        print('- No internet connection!')
        return False

def doGit():
    os.system('git add '+file_name)
    os.system('git commit -m "latest flight summary"')
    os.system('git push origin parachuteTest')
    username = raw_input('- Enter GitHub Username: ')
    os.system(str(username))
    password = getpass.getpass()
    os.system(password)

if netCheck() == True:
    doGit()

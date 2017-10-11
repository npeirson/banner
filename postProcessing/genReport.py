# pulls most recent log data into a markdown file
# then commits and pushes it to github
# done in command line becaus PyGit and PyGitHub documentation is shit

# imports
import datetime
import urllib2
import getpass
import os
import time

now = datetime.datetime.now()
prefix = now.strftime("%Y-%m-%d")
file_name = ('scribble/'+str(prefix)+'-flight-log.md')
commit_message = 'latest flight log'

with open(file_name, 'w') as text_file:
    text_file.write('---\nlayout: post\ntitle: First Post\n---\n\n')
    text_file.write('# Test Log\n\n')
    text_file.write('This is a test of the automatic message posting system.')

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

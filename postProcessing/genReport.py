# Parses APRS data into push-ready MD layout

# import things
import sys
import datetime
import csv

# initialize variables
rows = []
fields = []

# check args
fileIn = sys.argv
if len(fileIn) < 2:
    print "\nSpecify a csv file to import!"
    exit()
elif len(fileIn) > 2:
    print "\nToo many arguments!"
    exit()
else:
    parse()

# Parse APRS data
with open(fileIn[1],r) as aprsfile:
    aprsreader = csv.reader(aprsfile)
    fields = aprsreader.next()




# writes file
now = datetime.datetime.now()
prefix = now.strftime("%Y-%m-%d")
fileOut = ('scribble/'+str(prefix)+'-flight-log.md')
commit_message = 'latest flight log'

with open(fileOut, 'w') as text_file:
    text_file.write('---\nlayout: post\ntitle: First Post\n---\n\n')
    text_file.write('# Test Log\n\n')
    text_file.write('This is a test of the automatic message posting system.')

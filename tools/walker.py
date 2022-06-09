import os
from pprint import pprint
import config

# returns {path: filecode} dictionary of all files in FOLDER
# For first run, delete all *.pyc to avoid "magic number error"

def get_all_scrapes(dir):  # needed to direct an API call w/ filename to the location of the file to run it
    print("Walking {}".format(dir))
    d = {}
    for (root, dirs, files) in os.walk(dir):
        for file in files:
            d[file] = root + '/' + file
    return d

if __name__ == '__main__':
    filecodes = get_all_scrapes(dir=config.SCRAPE_SCRIPT_PATH)
    pprint(filecodes)
    print('found %s filecodes' % len(filecodes))

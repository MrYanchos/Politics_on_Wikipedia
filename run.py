import sys
import src.etl.get_anames as gn
import shutil

args = sys.argv[1:]
fname = ""

if "scrape" in args:
    fname = gn.scrape()
    
if "retrieve" in args:
    if fname == "":
        artnames = gn.retrieve()
    else:
        artnames = gn.retrieve(fname)
    print(artnames[:10])

if "clean" in targets:
    shutil.rmtree('src/data/raw', ignore_errors=True)

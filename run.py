import sys
import src.etl.get_anames as gn
import src.etl.get_atexts as gt
import src.models.get_gns_scores as gns

args = sys.argv[1:]
fname = ""

if "scrape_anames" in args:
    fname = gn.scrape()
    
if "retrieve_anames" in args:
    if fname == "":
        artnames = gn.retrieve()
    else:
        artnames = gn.retrieve(fname)
    
if "all" in args:
    # fname = gn.scrape()
    # gt.scrape_atexts()
    nametxt_dict = gt.retrieve_atexts()
    namestat_dict = gns.get_stat_dict(nametxt_dict)
    print(namestat_dict)

if "test" in args:
    




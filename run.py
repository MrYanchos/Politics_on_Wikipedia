import sys
import subprocess
import src.etl.get_anames as gn
import src.etl.get_atexts as gt
import src.etl.get_ibc as gibc
import src.models.get_gns_scores as gns
import src.models.partyembed_ibc as pei

args = sys.argv[1:]
fname = ""

if "scrape_anames" in args:
    fname = gn.scrape()
    
if "retrieve_anames" in args:
    if fname == "":
        artnames = gn.retrieve()
    else:
        artnames = gn.retrieve(fname)
        
if "ibc" in args:
    with open('config/get_ibc_params.json') as fh:
        data_cfg = json.load(fh)
        
    gibc.sample_ibc(**data_cfg)

if "interpret_ibc" in args:
    subprocess.call('git clone https://github.com/lrheault/partyembed.git', shell = True)
    with open('config/interpret_ibc_params.json') as fh:
        data_cfg = json.load(fh)
    
    pei.interpret_ibc(**data_cfg)
    
if "all" in args:
    # fname = gn.scrape()
    # gt.scrape_atexts()
    nametxt_dict = gt.retrieve_atexts()
    namestat_dict = gns.get_stat_dict(nametxt_dict)
#     print(namestat_dict)

if "test" in args:
    subprocess.call('git clone https://github.com/lrheault/partyembed.git', shell = True)
    nametxt_dict = gt.retrieve_atexts(test=True)
    namestat_dict = gns.get_stat_dict(nametxt_dict, test=True)
    print(namestat_dict)
    gibc.sample_ibc("False")
    print("Running model on test data...")
    pei(temp_directory="test/temp", out_directory = 'test/out', agg_func='mean')
    print("Finished, output in test/out/means.csv")
    




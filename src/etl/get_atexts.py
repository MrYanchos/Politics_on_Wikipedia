import wikipediaapi as wp
import os
import time
from src.libcode import txt_to_list, list_to_txt
from src.etl.get_anames import retrieve

def scrape_atexts():
    enwp = wp.Wikipedia("en")
    anames = retrieve()
    num_per_text = len(anames)//10
    wikitxts_dir = "src/data/temp/wiki_txts/"

    # If wiki texts folder does not exist make it
    if not os.path.exists(wikitxts_dir):
        os.makedirs(wikitxts_dir)

    txtlst = []
    for ind, aname in enumerate(anames):
        # Get the page text
    #     print(ind, aname)
        curpg = enwp.page(aname)
        curtit = curpg.title
        curtxt = curpg.text
        txtlst.append(curtit)
        txtlst.append(curtxt)
        # This ensures it saves into 10 txt files
        if (ind+1) % num_per_text == 0:
            print(ind+1)
            curtxt_name = "art_pages" + str((ind+1)//num_per_text) + ".txt"
            list_to_txt(wikitxts_dir+curtxt_name, txtlst)
            txtlst = []
            time.sleep(10)
            
    # Save last set of articles
    if len(txtlst) > 0:
        curtxt_name = "art_pages10" + ".txt"
        list_to_txt(wikitxts_dir+curtxt_name, txtlst)


def retrieve_atexts():
    wikitxts_dir = "src/data/temp/wiki_txts/"
    wiki_txts = ["art_pages" + str(i) + ".txt" for i in range(1,11)]
    nametxt_dict = {}

    cnt = 0
    for txt in wiki_txts:
        # print(cnt)
        txtlst = txt_to_list(wikitxts_dir + txt)
        for item in txtlst:
            if cnt % 2 == 0:
                aname = item
            else:
                nametxt_dict[aname] = item
            cnt += 1
            
    return nametxt_dict

def txt_to_list(fname):
    with open("src/data/" + fname, "r", encoding="utf8") as rfile:
        fullstr = rfile.read()
    lst = fullstr.split("~!~")
    return lst

def list_to_txt(fname, lst):
    with open("src/data/"+fname, "w", encoding="utf8") as wfile:
        for i in lst[:-1]:
#             try:
            wfile.write('%s~!~' % i)
#             except:
#                 print(i + " was not included.") 
         
#         try:
        wfile.write(lst[-1])
#         except:
#             print(lst[-1] + " was not included.")
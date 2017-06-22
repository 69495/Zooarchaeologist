from mastodon import Mastodon
import json
from login import login
from out_json import jsoner
import time

'''
return_typeはjson or list
defaultはlistで返す
'''
'''
現状はMastodon.pyを少し弄る必要があります

'''

def fav(return_type="list", switch=None):
    print(return_type + " is selected!")

    Mastodon = login(switch)
    my_cred = Mastodon.account_verify_credentials()
    id = my_cred['id']
    print("Your id is {0}".format(id))
    #lastestなmax_idを取得
    initial_max_id = Mastodon.fav(None,None,limit=1)
    initial_max_id = initial_max_id[-1]['max_id']
    fav = Mastodon.fav(initial_max_id, None, 40)
    print("Initial max id is {0}".format(initial_max_id))

    try_num = 0

    while True:

        #続きのtootを取得
        next_max_id = fav[-1]['max_id']
        last_fav = Mastodon.fav(next_max_id, None, 40)

        fav.extend(last_fav)
        try_num += 1
        last_length = len(last_fav)

        length = (len(fav) - try_num * 1)
        print("count: {0} ({1})".format(str(length-1),last_length-1))
        time.sleep(3)

        if last_length != 41:
            break

    if return_type == "json":
        filename = str(id) + "_fav"
        jsoner(fav,filename)

    else:
        return fav

    # id = int(input())
    # mining(id)

if __name__ == '__fav__':
    fav()

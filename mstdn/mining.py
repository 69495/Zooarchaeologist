from mastodon import Mastodon
import json
from login import login
from out_json import jsoner

'''
return_typeはjson or list
defaultはlistで返す
'''

def mining(id,return_type="list"):
    print(return_type + " is selected!")

    Mastodon = login()

    #timelineからlastestなmax_idを取得
    tl = Mastodon.timeline_local(limit=1)
    initial_max_id = tl[0]['id']

    toot = Mastodon.account_statuses(id, initial_max_id, None, 40)
    while True:

        last_max_id = toot[len(toot)-1]['id']
        #続きのtootを取得
        last_toot = Mastodon.account_statuses(id, last_max_id, None, 40)

        toot.extend(last_toot)

        # final_max_lenge = len(toot)-1
        final_max_lenge = len(last_toot) -1
        # account = Mastodon.account(id)
        # count = account['statuses_count']


        if final_max_lenge < 39:
            break

    if return_type == "json":
        filename = str(id)
        jsoner(toot,filename)

    else:
        return toot

    # id = int(input())
    # mining(id)

if __name__ == '__mining__':
    mining()

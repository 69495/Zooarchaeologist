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
    initial_max_id = 17350000 #latest toot

    toot = Mastodon.account_statuses(id, max_id=initial_max_id, since_id=None, limit=40)
    while True:
        max_lenge = len(toot) - 1
        last_max_id = toot[max_lenge]['id']
        last_toot = Mastodon.account_statuses(id, last_max_id, None, 40)
        toot.extend(last_toot)
        final_max_lenge = len(last_toot) -1
        print(len(toot))
        print(toot[max_lenge]['id'])
        account = Mastodon.account(id)
        count = account['statuses_count']

        if final_max_lenge < 39:
            break

    if return_type == "json":
        filename = str(id)
        jsoner(toot,filename)
        print("return json!")
    else:
        print("return list!")

        return toot

    # id = int(input())
    # mining(id)

if __name__ == '__mining__':
    mining()

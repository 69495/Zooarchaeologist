from mastodon import Mastodon
import json
from login import login

def mining(id):
    mastodon = login()
    initial_max_id = 17350000 #最新のトゥート付近

    toot = mastodon.account_statuses(id, max_id=initial_max_id, since_id=None, limit=40)
    while True:
        max_lenge = len(toot) - 1
        last_max_id = toot[max_lenge]['id']
        last_toot = mastodon.account_statuses(id,max_id=last_max_id, since_id=None, limit=40)
        toot.extend(last_toot)
        final_max_lenge = len(last_toot) -1
        print(len(toot))
        print(toot[max_lenge]['id'])

        if final_max_lenge < 39:
            break

    filename = str(id) + "_toot.json"
    with open(filename, "w") as fp:
        json.dump(toot,fp)

def main():
    mastodon = login()
    id = int(input())
    mining(id)

if __name__ == '__main__':
    main()

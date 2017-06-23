from mastodon import Mastodon
import json
from login import login
from out_json import jsoner
from pprint import pprint
import time

'''
return_typeはjson or list
defaultはlistで返す
'''

def fav2(return_type="list", switch=None):

    wait_sec = 30
    start = time.time()

    e = lambda a, b : round(a-b)

    print(return_type + " is selected!")

    Mastodon = login(switch)
    my_cred = Mastodon.account_verify_credentials()
    id = my_cred['id']
    limit = 40 #40
    print("Your id is {0}".format(id))

    page = 0
    favourites = Mastodon.favourites(None,None,limit)
    max_id = favourites[-1]['_pagination_next']['max_id']
    print("count: {0} ({1})".format(str(len(favourites)), str(len(favourites))))

    while True:

        latest_favourites = Mastodon.favourites(max_id,None,limit)

        if isinstance(latest_favourites,dict):
            pprint("Error code 429:{0} wait {1} sec...".format(latest_favourites['error'],wait_sec))
            time.sleep(wait_sec)
            latest_favourites = previous_favourites
            continue

        elif len(latest_favourites) < limit:
            favourites.extend(latest_favourites)
            page += 1
            elapsed_time = time.time() - start
            print("End fetch your favourites")
            print("count: {0} time:{1}sec".format(str(len(favourites)), elapsed_time))
            break
        else:
            max_id = favourites[-1]['_pagination_next']['max_id']

            favourites.extend(latest_favourites)
            page += 1
            previous_favourites = latest_favourites

            print("count: {0} ({1}) time:{2}sec".format(str(len(favourites)), str(len(latest_favourites)), e(time.time(),start)))
            time.sleep(3)

    if return_type == "json":
        filename = str(id) + "_fav"
        jsoner(favourtes,filename)

    else:
        return favourites

if __name__ == '__main__':
    main()

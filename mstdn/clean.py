from mastodon import Mastodon
from login import login
from mining import mining

'''
all_destroyするためのコード
'''

def clean(user_id,type=""):
    Mastodon = login()

    user_toot = mining(user_id,type)
    for num in range(len(user_toot)):
        Mastodon.status_delete(user_toot[num]['id'])

if __name__ == '__clean__':
    clean()

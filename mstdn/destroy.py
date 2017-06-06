from mastodon import Mastodon
from login import login
from mining import mining

'''
all_destroyするためのコード
'''

def destroy(user_id,type):
    Mastodon = login()
    Mastodon.mining(user_id)
    while i in range(user_toot):
        print(user_toot[i]['id'])
        print(str(i)+str(range(user_id)))
        i+=1
    # mastodon.delete(user_id)

if __name__ == '__destroy__':
    destroy()

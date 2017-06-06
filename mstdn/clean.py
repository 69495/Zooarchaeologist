from mastodon import Mastodon
from login import login
from mining import mining

'''
all_destroyするためのコード
'''
def clean(user_id,type):
    print("destroy start!")
    Mastodon = login()

    # myaccount = Mastodon.account_verify_credentials()
    # myaccount = Mastodon.account(user_id)
    # print(myaccount['statuses_count'])


    user_toot = mining(user_id,type)
    for num in range(len(user_toot)):
        print(user_toot[num]['id'])

    # print(type(user_toot))
    # for k, v in user_toot.items():
        # print(k,v)
    # mastodon.delete(user_id)

if __name__ == '__clean__':
    clean()

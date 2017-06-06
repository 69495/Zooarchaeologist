from mastodon import Mastodon
from login import login

'''
Boostするためだけのコード
execの方に寄せる予定
'''

def boost(target_id):
    mastodon = login()
    mastodon.status_reblog(target_id)

if __name__ == '__main__':
    boost()

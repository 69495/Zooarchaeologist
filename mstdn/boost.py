from mastodon import Mastodon
from login import login

def boost(target_id):
    mastodon = login()
    mastodon.status_reblog(target_id)

if __name__ == '__main__':
    main()

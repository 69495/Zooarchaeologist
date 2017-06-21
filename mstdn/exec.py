from mastodon import Mastodon
from login import login

def exec(action, target_id=None, switch=None):

    # target_id = int(input())
    mastodon = login(switch)

    #action
    if action == "favourite":
        print("You are favourite "+str(target_id))
        mastodon.status_favourite(target_id)
    elif action == "boost":
        print("You are boost "+str(target_id))
        mastodon.status_reblog(target_id)
    elif action == "status":
        print(mastodon.status_context(target_id))
    elif action == "delete":
        mastodon.status_delete(target_id)
    elif action == "toot":
        mastodon.toot("toot by python")
    else:
        print("action is enpty")

"""
    mastodon.status_reblog(target_id)
    mastodon.status_delete(target_id)
"""

if __name__ == '__main__':
    exec()

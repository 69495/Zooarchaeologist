from mastodon import Mastodon
import json
from login import login
from datetime import datetime

def latest_id():

    mastodon = login()

    timeline = mastodon.timeline_local()
    latest_id = timeline[0]['id']

    return latest_id

if __name__ == '__main__':
    latest()

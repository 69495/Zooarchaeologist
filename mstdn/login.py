from mastodon import Mastodon

def login():
    mastodon = Mastodon(
        client_id= 'my_clientcred_mstdn.txt',
        access_token = 'my_usercred_mstdn.txt',
        api_base_url = 'https://mstdn.jp/'
    )
    return mastodon

if __name__ == '__main__':
    login()

from mastodon import Mastodon

def login(account_switch=None):
    if account_switch == 1:
        mastodon = Mastodon(
        client_id= 'my_clientcred_mstdn_.txt',
        access_token = 'my_usercred_mstdn_.txt',
        api_base_url = 'https://mstdn.jp/'
        )
    elif account_switch == 2:
        mastodon = Mastodon(
        client_id= 'my_clientcred_mstdn_felesitas.txt',
        access_token = 'my_usercred_mstdn_felesitas.txt',
        api_base_url = 'https://felesitas.cloud'
        )
    else:
        mastodon = Mastodon(
        client_id= 'my_clientcred_mstdn.txt',
        access_token = 'my_usercred_mstdn.txt',
        api_base_url = 'https://mstdn.jp/'
        )

    return mastodon

if __name__ == '__login__':
    login()

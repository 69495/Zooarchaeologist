from mastodon import Mastodon
def main():
    Mastodon.create_app("mastdnPy", api_base_url = "https://mstdn.jp", to_file = "my_clientcred_mstdn.txt")
    mastodon = Mastodon(client_id="my_clientcred_mstdn.txt",api_base_url = "https://mstdn.jp")
    mastodon.log_in("yourmail address", "password",to_file = "my_usercred_mstdn.txt")

if __name__ == '__main__':
    main()

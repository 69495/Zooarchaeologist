from mastodon import Mastodon
def main():
    Mastodon.create_app("mastdnPy", api_base_url = "https://felesitas.cloud", to_file = "my_clientcred_mstdn__.txt")
    mastodon = Mastodon(client_id="my_clientcred_mstdn__.txt",api_base_url = "https://felesitas.cloud")
    mastodon.log_in("kimura.yuma@gmail.com", "1w0pM0CDriE2KfXE5ZIt",to_file = "my_usercred_mstdn__.txt")

if __name__ == '__main__':
    main()

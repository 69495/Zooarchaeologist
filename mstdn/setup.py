from mastodon import Mastodon
Mastodon.create_app("mastdnPy", api_base_url = "https://mstdn.jp", to_file = "my_clientcred_mstdn.txt")
mastodon = Mastodon(client_id="my_clientcred_mstdn.txt",api_base_url = "https://mstdn.jp")
mastodon.log_in("mail_address", "password",to_file = "my_usercred_mstdn.txt")

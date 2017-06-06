# Zooarchaeologist
mastodonを掘り返したり傾向を掴むためのツール

のはずだったがjsonで出力する機能と全削除の機能しか無い

一応tootとかfavoriteとかboostとかも出来るがそれはMastodon.pyでも出来る


##使い方
python 3.6


pip3 install Mastodon.py


```python:setup.py
Mastodon.create_app("mastdnPy", api_base_url = "https://mstdn.jp", to_file = "my_clientcred_mstdn.txt")
mastodon = Mastodon(client_id="my_clientcred_mstdn.txt",api_base_url = "https://mstdn.jp")
mastodon.log_in("mail_address", "password",to_file = "my_usercred_mstdn.txt")
```


python hoge.py


```python:hoge.py
from mastodon import Mastodon
from mining import mining
from login import login
from clean import clean

def main():

    Mastodon = login()

    mya = Mastodon.account_verify_credentials()
    print("your account is " + str(mya['id']))

    user_id = input()

    clean(user_id,"")

if __name__ == '__main__':
    main()
```


python hoge.py


```python:fuga.py
from mastodon import Mastodon
from mining import mining
    main()
        user_id = account_id
        mining(user_id,"json")

if __name__ == '__main__':
    main()
```


Mastodon.py
https://github.com/halcy/Mastodon.py


Mastodon.py licence
https://github.com/halcy/Mastodon.py/blob/master/LICENSE


Mastodon api
http://mastodonpy.readthedocs.io/en/latest/

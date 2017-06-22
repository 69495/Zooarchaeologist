# Zooarchaeologist
mastodonを掘り返したり傾向を掴むためのツール

のはずだったがjsonで出力する機能と全削除の機能しか無い

一応tootとかfavoriteとかboostとかも出来るがそれはMastodon.pyでも出来る

技術力が無いせいでMastodon.pyを無茶苦茶な方法で拡張して使うという解決策になってしまった(改変したMastodon.pyは一緒に入ってます)

ここには出来る限り使い方を書こうと思う


##使い方


python 3.6をインストールする(PATHを通す)


pip3 install Mastodon.py


このレポジトリをクローンする(わからなければzipでダウンロードして展開する)


コマンドプロンプトで展開したディレクトリまで行く


python setup.py


と言った具合に実行する


setup.pyを実行後、用途に応じてPythonを書いてそれを実行する(下のコードを丸写しにしても動くのでテキストエディタで書いてそれを実行しよう!)



```python:setup.py
from mastodon import Mastodon
Mastodon.create_app("mastdnPy", api_base_url = "https://mstdn.jp", to_file = "my_clientcred_mstdn.txt")
mastodon = Mastodon(client_id="my_clientcred_mstdn.txt",api_base_url = "https://mstdn.jp")
mastodon.log_in("mail_address", "password",to_file = "my_usercred_mstdn.txt")
```


python hoge.py(tootの全削除)


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


python fuga.py(その人のtootをjsonで保存)


```python:fuga.py
from mastodon import Mastodon
from mining import mining

    main():
        user_id = account_id
        mining(user_id,"json")

if __name__ == '__main__':
    main()
```

python huge.py(お気に入りをjsonで保存/Mastodon.pyの書き換えが必要)


```python:huge.py
from fav import fav
import time

def main():

    start = time.time()

    fav("json",)

    elapsed_time = time.time() - start
    print("Time:{0}".format(elapsed_time) + "{sec}")

if __name__ == '__main__':
    main()
```


Mastodon.py
https://github.com/halcy/Mastodon.py


Mastodon.py licence
https://github.com/halcy/Mastodon.py/blob/master/LICENSE


Mastodon api
http://mastodonpy.readthedocs.io/en/latest/

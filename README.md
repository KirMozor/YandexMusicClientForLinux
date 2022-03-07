# Yamux
Description: This is a client for Yandex Music on Unix

### Install dependencies

My program requires a token from YandexMusic, to get it, follow this link: <a href="https://oauth.yandex.ru/authorize?response_type=token&client_id=ef4bf3db195c43739906b13dd7325e3f">Click*</a>. Then run the program and follow the instructions:

`pip install -U -r reqs.txt`

Also you need to get libmpv.so. It contains in packages `libmpv1`, `mpv-devels` and `mpv-libs`, so install one of them.

Sometimes you need to install the package python-pyqt5 or python3-pyqt5
In ArchLinux I do it like this:

`sudo pacman -S python-pyqt5`

In systems, which using apt, you can install it with this command:

`sudo apt install python3-pyqt5`


### Launch

You need to run the main.py file at the root of the program

`python3 main.py`

### By the way

I have my own Telegram blog, where I talk about the progress and progress of development
There you can contact me as soon as possible.
Link: https://t.me/kirmozor

# Photo Flow
图片展示墙，内容来源于网友的图片链接。
灵感来源于 pure 的一个 Layout
## Features
- 我也不知道也要做什么呀…

## Run it
### FrontEnd
1. clone it git clone https://github.com/tiant167/PhotoFlow
2. cd PhotoFlow && npm install && bower install
3. grunt serve
### BackEnd
We are using Django 1.7, python 2.7 is required.
1. Create Virtual Enviroment with virtualenvwrapper. ( you can easily install by `pip install virtualenvwrapper`)
`source /usr/local/bin/virtualenvwrapper.sh`
        `mkvirtualenv env1`
2. Use pip to install requirements. `pip install -r requirements.txt`
2. Rename settings.py.dev into settings.py, and config your own secret key and mysql and other settings.
3. Syncdb `python manager.py syncdb`
5. Migrate Database `python manager.py migrate`

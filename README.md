# Photo Flow
本来想做一个图片展示墙，内容来源于网友提供的图片链接。
灵感来源于 pure 的一个 Layout。
写着写着就写成博客了，不过无所谓吧，打发点时间。
原来那个想法可能另起炉灶做一个~

原来的服务器拿去做更重要的事情了…所以直接 pull 下来直接看看效果呗~

## Features
- 个人博客，包含 Photo 和 Blog 两块。
- AngularJS 单页面应用
- Prerender.io SEO 处理
- Pure CSS 响应式设计
- Django 1.7 + Restful API (Class-Based-View)
- Django Admin 作为 CMS
- 支持 Markdown，图片自动压缩，首页图片自动排版，Photo Gallery 等

## 没图你说个……
![bigPic](https://raw.githubusercontent.com/tiant167/PhotoFlow/master/readme_pic/big.png 'bigPic')

![smallPic](https://raw.githubusercontent.com/tiant167/PhotoFlow/master/readme_pic/small.png 'smallPic')

![pic_preview](https://raw.githubusercontent.com/tiant167/PhotoFlow/master/readme_pic/pic_preview.png 'pic_preview')

![bloglist](https://raw.githubusercontent.com/tiant167/PhotoFlow/master/readme_pic/bloglist.png 'bloglist')

![article](https://raw.githubusercontent.com/tiant167/PhotoFlow/master/readme_pic/article.png 'article')

![article_small](https://raw.githubusercontent.com/tiant167/PhotoFlow/master/readme_pic/article_small.png 'article_small')

## CMS Admin
使用 Django Admin 来做 CMS 后台。

在后台中可以方便的进行文章的编辑、图片的上传、博客的名字签名等信息的修改等。

文章支持 Markdown 语法，并且能够实时预览效果。

图片上传会自动压缩，生成缩略图和中等图。能自动识别图片尺寸，判断是否是竖图、全景图等。
对全景图的展示和其他的图片不一样，在展示时会使用整屏。

对于博客的名字、描述以及图片首页的签名都是可以随时修改和定制的，没有写死的数据。

此外，在后台中还加上了系统使用情况，包括内存、CPU、硬盘等系统信息。

![sys](https://raw.githubusercontent.com/tiant167/PhotoFlow/master/readme_pic/sys.png 'sys')

![picadmin](https://raw.githubusercontent.com/tiant167/PhotoFlow/master/readme_pic/pic_admin.png 'picadmin')

![blogadmin](https://raw.githubusercontent.com/tiant167/PhotoFlow/master/readme_pic/blog_admin.png 'blogadmin')

![conf](https://raw.githubusercontent.com/tiant167/PhotoFlow/master/readme_pic/conf_admin.png 'conf')


## 开发相关概述

### 前端
前端的文件已经打包在 `dist` 文件夹中，如果做了修改可以重新 build

前端使用的是 [AngularJS](https://angularjs.org/ "AngularJS") 编写，是一个单页面应用。CSS 框架使用了 [PureCSS](https://github.com/yahoo/pure/ "PureCss")

针对 SEO 使用了 Prerender.io，国内访问 prerender 的服务器有点慢，SEO 的效果也不知道好不好，看看吧~

此外使用到了以下开源项目：

- [angular-markdown-directive](https://github.com/btford/angular-markdown-directive "angular-markdown-directive")
- [showdown](https://github.com/showdownjs/showdown "showdown")
- [angular-bootstrap-lightbox](https://github.com/compact/angular-bootstrap-lightbox "angular-bootstrap-lightbox")

项目使用 Yeoman，Grunt，Bower 构建，这块相关的文档麻烦查看 Yeoman 的[帮助文档](http://yeoman.io/learning/index.html "Yeoman")

#### 安装与运行

如果不修改前端代码可以直接使用 dist 文件夹中已经 build 好的文件。

1. clone 项目代码 `git clone https://github.com/tiant167/PhotoFlow`
2. 进入目录安装依赖 `cd PhotoFlow && npm install && bower install`
3. 运行 `grunt serve`

### 后端

项目后端使用 Python 编写，使用 [Django 1.7](https://github.com/django/django "Django") 框架，所以最低的 Python 版本是 2.7

其中项目依赖于以下开源项目：

- [djangorestframework](https://github.com/tomchristie/django-rest-framework/ "https://github.com/tomchristie/django-rest-framework/")
- [Markdown](https://github.com/waylan/Python-Markdown "Markdown")
- [django-markdown](https://github.com/klen/django_markdown "django-markdown")
- [django-system-monitor](https://github.com/hakanzy/django-system-monitor "django-system-monitor")
- [Pillow](https://github.com/python-pillow/Pillow "Pillow")

此外，推荐使用 [virtualenvwrapper](https://github.com/bernardofire/virtualenvwrapper "virtualenvwrapper") 隔离环境，[pip](https://github.com/pypa/pip "pip") 维护依赖包

#### 安装与运行

1. 使用 virtualenvwrapper 创建虚拟环境。 （virtualenvwrapper 的安装方式可以查看它的[文档](https://virtualenvwrapper.readthedocs.org/en/latest/ "virtualenvwrapper")了解）
2. 使用 pip 安装依赖。`pip install -r requirements.txt`
2. 把 settings.py.dev 重命名为 settings.py，然后修改配置，更改 secret key 和数据库连接等。
3. 执行数据库同步（写入）Syncdb `python manager.py syncdb`

### Web Server

后端服务使用 Nginx + uWsgi 的结构。

nginx 用于静态资源的分拣，uWsgi 作为 Python 的应用服务器。

nginx 的配置如下

        server {
            listen   80;
            server_name t.tinkerlab.cn;

            root  /root/cht_django/PhotoFlow/dist;
            index  index.html;
            
            location /api/ {
             include        uwsgi_params;
             uwsgi_pass     127.0.0.1:10001;
            }

            location /static/ {
                alias  /your_path/PhotoFlow/backend/photoflow/static/;
                index  index.html index.htm;
            }

            location /fonts/ {
                alias  /root/cht_django/PhotoFlow/fonts/;
                index  index.html index.htm;
            }

            location / {
                try_files $uri @prerender;
            }

            location @prerender {
                proxy_set_header X-Prerender-Token YOURTOKEN;

                set $prerender 0;
                if ($http_user_agent ~* "baiduspider|twitterbot|facebookexternalhit|rogerbot|linkedinbot|embedly|quora link preview|showyoubot|outbrain|pinterest|slackbot") {
                    set $prerender 1;
                }
                if ($args ~ "_escaped_fragment_") {
                    set $prerender 1;
                }
                if ($http_user_agent ~ "Prerender") {
                    set $prerender 0;
                }
                if ($uri ~ "\.(js|css|xml|less|png|jpg|jpeg|gif|pdf|doc|txt|ico|rss|zip|mp3|rar|exe|wmv|doc|avi|ppt|mpg|mpeg|tif|wav|mov|psd|ai|xls|mp4|m4a|swf|dat|dmg|iso|flv|m4v|torrent)") {
                    set $prerender 0;
                }

                #resolve using Google's DNS server to force DNS resolution and prevent caching of IPs
                resolver 8.8.8.8;

                if ($prerender = 1) {

                    #setting prerender as a variable forces DNS resolution since nginx caches IPs and doesnt play well with load balancing
                    set $prerender "service.prerender.io";
                    rewrite .* /$scheme://$host$request_uri? break;
                    proxy_pass http://$prerender;
                }
                if ($prerender = 0) {
                    rewrite .* /index.html break;
                }
            }
        }

其中的 static 是用来放 admin cms 所需的静态文件的。使用 `python manage.py collectstatic` 自动收集静态文件。

# [bearicc.com](http://www.bearicc.com)

# Deploy Django to Apache
LoadModule wsgi_module modules/mod_wsgi.so

Alias /robots.txt /path/to/mysite.com/static/robots.txt

Alias /favicon.ico /path/to/mysite.com/static/favicon.ico

Alias /media/ /path/to/bearicc.com/media/

Alias /static/ /path/to/bearicc.com/staticfiles/

<Directory /path/to/bearicc.com/staticfiles>

Require all granted

</Directory>

<Directory /path/to/bearicc.com/media>

Require all granted

</Directory>

WSGIScriptAlias / /path/to/bearicc.com/mysite/wsgi.py
WSGIPythonPath /path/to/bearicc.com

<Directory /path/to/bearicc.com/mysite>
<Files wsgi.py>
Require all granted
</Files>
</Directory>

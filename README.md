# [bearicc.com](http://www.bearicc.com)

### How to deploy Django app to Apache web server ?
#####1. Run `python manage.py collectstatic`
#####2. Append the content of `apache.conf` to the config file of Apache (`/etc/httpd/conf/httpd.conf` in Archlinux)

### How to setup PostgreSQL database ?
##### Note: change the content in small brackets as desired. It is recommended to use the regular user name on PC as the username, so you can connect to the database without switching to postgres user.
#####1. > sudo su - postgres
#####2. > psql
#####3. > CREATE USER (username) PASSWORD '(password)';
#####4. > ALTER ROLE (username) CREATEDB;
#####5. > CREATE DATABASE (database name) OWNER (username);

### Reference
1. [README.md markdown ref](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

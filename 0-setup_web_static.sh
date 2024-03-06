#!/usr/bin/env bash
#sets up web servers for the deployment of web_static
sudo apt-get update
sudo apt-get install -y nginx
mkdir -p /data/ /data/web_static/ /data/web_static/releases/  /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html && echo "Hello World!" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
echo "Hello World!" > /var/www/html/index.html
echo "Ceci n'est pas une page" > /var/www/html/404.html
hostname=$(hostname)
sudo echo "server {
    listen 80;
    listen [::]:80;

    add_header X-Served-By $hostname;
    root /var/www/html/;
    index index.html;
    server_name _;

    location /redirect_me {
        return 301 var/www/html/redirect_me.html;
    }

    error_page 404 /404.html;

    location /404.html {
        root /var/www/html/;
        internal;
    }

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html;
    }
}" > /etc/nginx/sites-available/default
sudo service nginx restart

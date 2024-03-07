#!/usr/bin/env bash
# Sets up a web server for deployment

apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
    	alias /data/web_static/current;
	index index.html index.htm;
    }

    location /redirectt_me {
    	return 301 http://cuberule.com/;
    }

    error-page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

service nginx restart

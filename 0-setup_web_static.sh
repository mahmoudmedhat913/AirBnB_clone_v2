#!/usr/bin/env bash
if ! command -v nginx &>/dev/null; then
    apt-get update
    apt-get install nginx
    sudo ufw allow "Nginx HTTP"
fi
folder=("/data" "/data/web_static/" "/data/web_static/releases/" "/data/web_static/shared/" "/data/web_static/releases/test/")

for fol in ${folder[@]}; do
    if [ ! -d $fol ]; then
        mkdir -p $fol
    fi
done

link="/data/web_static/current"
target="/data/web_static/releases/test/"

if [ -L $link ]; then
    rm -f $link
    echo "removed"
fi

ln -s  $target $link
chown $ubuntu:$ubuntu /data/

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
sudo sed -i '/^[^#]*server_name.*;$/a \ \n\t\tlocation \/hbnb_static/ {\n\t\t\t\talias /data/web_static/current/;\n\t\t}' /etc/nginx/sites-available/default
service nginx restart

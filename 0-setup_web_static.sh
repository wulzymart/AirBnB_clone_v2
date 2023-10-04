#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test
sudo mkdir /data/web_static/shared
HTML=\
"<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

echo "$HTML" | sudo tee /data/web_static/releases/test/index.html

sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-enabled/default

sudo ufw allow 'Nginx Full'
sudo service nginx restart

# sets up your web servers for the deployment of web_static
$contents = "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

exec { 'Install and configure nginx':
  command  => "sudo apt-get update -y && 
               sudo apt-get install nginx -y && 
               sudo mkdir -p /data/web_static/releases/test/ && 
               sudo mkdir -p /data/web_static/shared/ && 
               echo '${contents}' > /data/web_static/releases/test/index.html && 
               sudo ln -sf /data/web_static/releases/test/ /data/web_static/current && 
               sudo chown -R ubuntu:ubuntu /data/ &&
               sudo rm -rf /etc/nginx/sites-enabled/default",
  provider => 'shell',
  path     => '/usr/bin:/bin:/usr/sbin:/sbin'
}

file { '/etc/nginx/sites-enabled/default':
  ensure  => present,
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

     root /var/www/html;

    server_name _;
        add_header X-Served-By $hostname;
        rewrite ^/redirect_me / permanent;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location /hbnb_static {
        alias /data/web_static/current/;
    }
}
",
  require => Exec['Install and configure nginx'],
}

exec { 'Restart Nginx':
  command => 'sudo service nginx restart',
  path    => '/usr/bin:/bin:/usr/sbin:/sbin',
  require => [File['/etc/nginx/sites-enabled/default'], Exec['Install and configure nginx']],
}

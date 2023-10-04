# sets up your web servers for the deployment of web_static

$HTML=\
'<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>'

exec {'update system':
  command => '/usr/bin/apt-get update',
}

-> package {'nginx':
  ensure => 'present',
}

-> exec {'create directories':
  command => 'sudo mkdir -p /data/web_static/releases/test',
  path => '/usr/bin:/usr/sbin:/bin'
  provider => 'shell'
}

-> exec {'create directories 2':
  command => 'sudo mkdir /data/web_static/shared',
  path => '/usr/bin:/usr/sbin:/bin'
  provider => 'shell'
}

-> file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => "$HTML"
}

-> exec {'create directories 2':
  command => 'sudo ln -s /data/web_static/releases/test/ /data/web_static/current',
  path => '/usr/bin:/usr/sbin:/bin'
  provider => 'shell'
}

-> exec {'create directories 2':
  command => 'sudo chown -R ubuntu:ubuntu /data/',
  path => '/usr/bin:/usr/sbin:/bin'
  provider => 'shell'
}

-> exec {'create directories 2':
  command => 'sudo chown -R ubuntu:ubuntu /data/',
  path => '/usr/bin:/usr/sbin:/bin'
  provider => 'shell'
}

-> exec {'create directories 2':
  command => "sudo sed -i '/listen 80 default_server/a \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-enabled/default"
  path => '/usr/bin:/usr/sbin:/bin'
  provider => 'shell'
}

-> exec {'create directories 2':
  command => 'sudo ufw allow 'Nginx Full'',
  path => '/usr/bin:/usr/sbin:/bin'
  provider => 'shell'
}

-> exec {'create directories 2':
  command => 'sudo service nginx restart',
  path => '/usr/bin:/usr/sbin:/bin'
  provider => 'shell'
}


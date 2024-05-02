# This script sets up web servers for web_static deployment using puppet

# Install nginx package
package { 'nginx':
  ensure   => 'present',
  provider => 'apt'
}

# Allow HTTP traffic in firewall
firewall { 'Nginx HTTP':
  port   => 80,
  proto  => 'tcp',
  action => 'accept',
}

# Create directories and index.html file
file { '/data/web_static/releases/test':
  ensure => directory,
  recurse => true,
}

file { '/data/web_static/shared':
  ensure => directory,
}

file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>\n",
}

# Create symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
}

# Change ownership of directories
exec { 'chown -R ubuntu:ubuntu /data/':
  command => '/bin/chown -R ubuntu:ubuntu /data/',
  path    => ['/bin', '/usr/bin'],
  onlyif  => '/bin/test ! -e /data/web_static/releases/test/index.html',
}

# Configure nginx
file_line { 'nginx_hbnb_static_alias':
  path    => '/etc/nginx/sites-enabled/default',
  line    => '        location /hbnb_static { alias /data/web_static/current/; }',
  match   => 'listen 80 default_server',
  after   => true,
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
}

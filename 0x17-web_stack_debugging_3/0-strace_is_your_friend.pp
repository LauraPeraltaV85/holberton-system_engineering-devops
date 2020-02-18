# find bug in apache/php and fix it
exec { 'prueba':
command  => 'sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
path     => '/usr/bin:/usr/sbin:/bin',
provider => 'shell',
}

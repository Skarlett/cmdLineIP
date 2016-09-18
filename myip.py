from urllib import urlopen
print('Public IP: '+urlopen('http://ipv4bot.whatismyipaddress.com/').read().replace('\n', ''))

import urllib2

html = urllib2.urlopen('http://api.k780.com:88/?app=weather.today&weaid=94'
                       '&&appkey=10003&sign=b59bc3ef6191eb9f747dd4e83c99f2a4&format=json')
message = html.read()
print message

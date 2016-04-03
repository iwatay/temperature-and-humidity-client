from datetime import datetime
import urllib
import urllib2
import Adafruit_DHT

humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)
tdatetime = datetime.now()
tstr = tdatetime.strftime('%Y-%m-%d %H:%M:%S')

url = ''
params = {'owner' : 'owner', 'date' : tstr, 'temperature' : temperature, 'humidity' : humidity}
params = urllib.urlencode(params)

res = urllib2.urlopen(url + 'post/?' + params)

body = res.read()


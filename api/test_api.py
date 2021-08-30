#from urllib2 import Request, urlopen
#from urllib import urlencode, quote_plus
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus

url = 'http://openapi.animal.go.kr/openapi/service/rest/animalInfoSrvc/animalInfo'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : '서비스키', quote_plus('dog_reg_no') : '410000000414197', quote_plus('rfid_cd') : '410000000414197' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print(response_body)
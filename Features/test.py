import geo

ip = geo.getIP()
print(ip)

country = geo.getCountry(ip, 'plain')
print(country)

country = geo.getCountry(ip, 'json')
print(country)

geoData = geo.getGeoData(ip)
print(geoData)

ptrData = geo.getPTR(ip)
print(ptrData)

geo.showIpDetails('123.23.45.0')

geo.showCountryDetails('123.23.45.0')
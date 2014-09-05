require "json"
require "uri"
require "net/http"

#uri = URI('http://s3.jspenguin.org/ssltest.py')

#routeResult = Net::HTTP.get(uri) # => String

m = Net::HTTP.get(URI('http://www.mapbar.com'))
puts m
#routeResult = JSON.parse(routeResult)

#puts routeResult




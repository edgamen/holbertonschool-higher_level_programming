require 'httpclient'
require 'json'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 3d59bbfb240064a050cb72476c091bd363e5267c'
}

http = HTTPClient.new
response = http.get_content("https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc")

file = File.open("/tmp/18", "w")
file.puts response
file.close

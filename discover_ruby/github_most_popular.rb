require 'httpclient'
require 'json'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 3d59bbfb240064a050cb72476c091bd363e5267c'
}

http = HTTPClient.new

# get the 30 most popular Ruby projects on Github from Github's API
response = http.get_content("https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc")
parsed = JSON.parse(response)

names = parsed["items"].map{|e| e["full_name"]}
# puts(names)     # if you just want to print all of them as elements?

string = names.join("\n")    # if you instead want to combine elements into one string and print on separate lines
puts(string)

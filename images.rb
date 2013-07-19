require 'pry'
require 'watchr'
require 'fsevent'

script = Watchr::Script.new
script.watch('/Users/mathiasx/Pictures/.*') { |m| puts "I would have compiled #{m[0]}" }
handler = Watchr.handler.new
controller = Watchr::Controller.new(script,handler)
controller.run # blocking

def put_photo(md)
  binding.pry
  puts system("echo #{md[0]}")
  puts
end

#watch('/Users/mathiasx/Pictures/.*') { |md| put_photo(md) }

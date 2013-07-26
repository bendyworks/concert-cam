require 'sinatra/base'

require 'koala'

class ConcertCam < Sinatra::Base
  run! if app_file == $0
end

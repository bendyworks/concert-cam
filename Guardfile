require 'guard/guard'
require 'koala'
require 'fileutils'

module ::Guard
  class FacebookUpload < Guard
    def initialize(watchers = [], options = {})
      super
      access_token = ENV['ACCESS_TOKEN']
      raise "No Access Token" unless access_token
      @album_id = ENV['ALBUM_ID']
      raise "No Album Id" unless @album_id
      @graph = Koala::Facebook::API.new(access_token)
    end

    def run_on_additions(paths)
      paths.each do |path|
        add_to_facebook(path)
      end
    end

    def add_to_facebook(path)
      @graph.put_picture(path, {message: "Taken on #{path_to_time(path)}"}, @album_id)
      dest = path.sub('/raw/', '/uploaded/')
      FileUtils.mv(path, dest)
    end

    def path_to_time path
      m = path.match(/[^-]*-(\d{4})-(\d\d)-(\d\d)_(\d\d)-(\d\d)-(\d\d)/)
      year, month, day, hour_mil, min, sec = m[1], m[2], m[3], m[4], m[5], m[6]
      time = Time.new(year, month, day, hour_mil, min, sec)
      time.strftime '%B %e, %Y at %l:%M:%S %p'
    end
  end
end

group :camera do
  guard :facebook_upload do
    watch %r{photos/raw/(.*)}
  end
end

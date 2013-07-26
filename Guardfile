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
      @graph.put_picture(path, {message: "testing: #{Time.now}"}, @album_id)
      dest = path.sub('/raw/', '/uploaded/')
      FileUtils.mv(path, dest)
    end
  end
end

group :camera do
  guard :facebook_upload do
    watch %r{photos/raw/(.*)}
  end
end

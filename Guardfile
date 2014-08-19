require 'guard/guard'
require './uploader'

module ::Guard
  class FacebookUpload < Guard
    def initialize(watchers = [], options = {})
      super
      @uploader = Uploader.new
    end

    def run_on_additions(paths)
      paths.each do |path|
        @uploader.process_photo(path)
      end
    end
  end
end

group :camera do
  guard :facebook_upload do
    watch %r{photos/raw/(.*)}
  end
end

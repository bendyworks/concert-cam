require 'koala'
require 'faraday'
require 'json'
require 'fileutils'

class Uploader
  def initialize
    access_token = ENV['ACCESS_TOKEN']
    raise "No Access Token" unless access_token

    @album_id = ENV['ALBUM_ID']
    raise "No Album Id" unless @album_id

    @graph = Koala::Facebook::API.new(access_token)
  end

  def process_photo(local_path)
    add_to_facebook(local_path)
    archive_photo(local_path)
    post_success_notice
  end

  def post_success_notice
    uri = "https://bendyworks.slack.com/services/hooks/incoming-webhook?token=#{ENV['SLACK_TOKEN']}"

    payload = {
      "username" => "concert_cam",
      "text" => "Uploaded photo!"
    }

    Faraday.post do |req|
      req.url uri
      req.headers['Content-Type'] = 'application/json'
      req.body = JSON.generate(payload)
    end
  end

  def add_to_facebook(local_path)
    @graph.put_picture(local_path, {message: "Taken on #{path_to_time(local_path)}"}, @album_id)
  end

  def archive_photo(local_path)
    dest = local_path.sub('/raw/', '/uploaded/')
    FileUtils.mv(local_path, dest)
  end

  def path_to_time(path)
    m = path.match(/[^-]*-(\d{4})-(\d\d)-(\d\d)_(\d\d)-(\d\d)-(\d\d)/)
    year, month, day, hour_mil, min, sec = m[1], m[2], m[3], m[4], m[5], m[6]
    time = Time.new(year, month, day, hour_mil, min, sec)
    time.strftime '%B %e, %Y at %l:%M:%S %p'
  end
end

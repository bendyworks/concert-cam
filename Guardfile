require 'guard/guard'
require 'koala'
require 'fileutils'
require 'pathname'

module RunOnAdditions
  def on_add(method_name)
    define_method :run_on_additions do |paths|
      paths.each do |path|
        send(method_name, path)
      end
    end
  end
end

module ::Guard
  class Watermarker < Guard
    extend RunOnAdditions
    on_add :do_watermark

    def do_watermark(path)
      pn = Pathname.new(path)
      dest = pn.dirname + "../watermarked/" + pn.basename

      watermark_path = File.expand_path('../watermark.png', __FILE__)
      watermark2_path = File.expand_path('../watermark2.png', __FILE__)
      watermark3_path = File.expand_path('../watermark3.png', __FILE__)
      bendylogo_path = File.expand_path('../photos/bendyworks-logo.png', __FILE__)
      magnet_logo_path = File.expand_path('../magnet_logo.png', __FILE__)

      watermark_size = `identify -format "%G" #{watermark_path}`.split("x").map(&:to_i)
      watermark2_size = `identify -format "%G" #{watermark2_path}`.split("x").map(&:to_i)
      watermark3_size = `identify -format "%G" #{watermark3_path}`.split("x").map(&:to_i)

      logo_size = `identify -format "%G" #{bendylogo_path}`.split("x").map(&:to_i)
      magnet_logo_size = `identify -format "%G" #{magnet_logo_path}`.split("x").map(&:to_i)
      image_size = `identify -format "%G" #{path}`

      watermark_width = (image_size.split("x").last.to_i * 0.2).to_i
      watermark_height = (watermark_width.to_f * watermark_size[1].to_f / watermark_size[0]).to_i

      watermark2_width = (image_size.split("x").last.to_i * 0.2).to_i
      watermark2_height = (watermark2_width.to_f * watermark2_size[1].to_f / watermark2_size[0]).to_i

      watermark3_width = (image_size.split("x").last.to_i * 0.2).to_i
      watermark3_height = (watermark3_width.to_f * watermark3_size[1].to_f / watermark3_size[0]).to_i

      watermark_width = (image_size.split("x").last.to_i * 0.2).to_i
      watermark_height = (watermark_width.to_f * watermark_size[1].to_f / watermark_size[0]).to_i

      logo_width = (image_size.split("x").last.to_i * 0.25).to_i
      logo_height = (logo_width.to_f * logo_size[1].to_f / logo_size[0]).to_i

      magnet_logo_width = (image_size.split("x").last.to_i * 0.25).to_i
      magnet_logo_height = (magnet_logo_width.to_f * magnet_logo_size[1].to_f / magnet_logo_size[0]).to_i

      puts "watermarking #{path} to #{dest}"

      `convert -composite #{path} #{watermark_path} -geometry #{watermark_width}x#{watermark_height}+50+1000 -depth 8 #{path}`
      `convert -composite #{path} #{watermark2_path} -geometry #{watermark2_width}x#{watermark2_height}+825+1150 -depth 8 #{path}`
      `convert -composite #{path} #{watermark3_path} -geometry #{watermark3_width}x#{watermark3_height}+1650+1000 -depth 8 #{path}`
      `convert -composite #{path} #{magnet_logo_path} -geometry #{magnet_logo_width}x#{magnet_logo_height}+25+10 -depth 8 #{path}`
      `convert -composite #{path} #{bendylogo_path} -geometry #{logo_width}x#{logo_height}+1575+40 -depth 8 #{dest}`
    end
  end

  class FacebookUpload < Guard
    extend RunOnAdditions
    on_add :add_to_facebook

    def initialize(watchers = [], options = {})
      super
      access_token = ENV['ACCESS_TOKEN']
      raise "No Access Token" unless access_token
      @album_id = ENV['ALBUM_ID']
      raise "No Album Id" unless @album_id
      @graph = Koala::Facebook::API.new(access_token)
    end

    def add_to_facebook(path)
      puts "adding #{path} to Facebook"
      resp = @graph.put_picture(path, {caption: "Taken by Bendyworks' Big Green Button (#{path_to_time(path)})"}, @album_id)
      puts "got #{resp}"
      dest = path.sub('/watermarked/', '/uploaded/')
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
  guard :watermarker do
    watch %r{photos/raw/(.*)}
  end

  guard :facebook_upload do
    watch %r{photos/watermarked/(.*)}
  end
end

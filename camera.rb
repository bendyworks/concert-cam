class Camera

  class << self
    AUTODETECT_NEEDLE = /Canon EOS 6D/

    def find_attached needle = AUTODETECT_NEEDLE
      puts 'Auto-detecting camera... this may take 10 seconds'
      output = `gphoto2 --auto-detect --quiet`.split("\n")
      line = output.grep(needle).first
      if line
        puts 'Found'
        port = line.match(/(usb:[0-9a-f,]*)/i)[1]
        new(port)
      else
        puts 'ERROR: Camera not found'
        raise 'Camera not found'
      end
    end
  end

  def initialize(port)
    @port = port
  end

  def start
    cmd = "gphoto2 --capture-image-and-download --interval=-1 --filename='loks-%Y-%m-%d_%H-%M-%S-%n.%C' --port=#{@port}"
    IO.popen(cmd) do |cam_proc|
      puts "gphoto2 proc: #{cam_proc.pid}"
      while str = cam_proc.readline.strip
        puts str
      end
    end
    puts 'popen finished'
  end
end

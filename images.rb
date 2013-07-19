require 'pry'
require 'rb-inotify'

notifier = INotify::Notifier.new

notifier.watch('/home/pi/pictures', :create) do |event|
  puts "Caught created image: #{event.absolute_name}"
  system("python /home/pi/dev/concert_cam/camera_board/watcher.py #{event.absolute_name}")
end

notifier.run

require 'pry'
require 'rb-inotify'

notifier = INotify::Notifier.new

notifier.watch('/home/pi/pictures', :create) do |event|
  puts "I would have compiled #{event.name}"
  system("python /home/pi/dev/concert_cam/camera_board/watcher.py #{event.name}")
end

notifier.run

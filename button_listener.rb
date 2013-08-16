require_relative './remote_button'
require_relative './scoreboard'

raise "PID of gphoto process required as parameter" unless ARGV[0]

camera_pid = ARGV[0].to_i

button, scoreboard = RemoteButton.new, Scoreboard.new

button.listen do
  puts "button pressed at #{Time.now}"

  Thread.new do
    scoreboard = Scoreboard.new
    scoreboard.show :three
    sleep 1
    scoreboard.show :two
    sleep 1
    scoreboard.show :one
    sleep 1
    scoreboard.show :all
    Process.kill("USR1", camera_pid)
    sleep 0.25
    scoreboard.show :blank
    puts 'done!'
  end

end

require_relative './remote_button'

raise "PID of gphoto process required as parameter" unless ARGV[0]

camera_pid = ARGV[0].to_i

button = RemoteButton.new
button.listen do
  puts 'button pressed'
  Process.kill("USR1", camera_pid)
end

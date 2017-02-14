pid = ARGV[0]

if pid
  Process.kill("SIGUSR1", pid.to_i)
else
  puts "Usage: take_picture.rb <pid>"
  exit(1)
end
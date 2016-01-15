require_relative './camera'

ptp_camera_pid_line = `ps aux | grep [P]TPCamera`
if ptp_camera_pid_line != ""
  pid = ptp_camera_pid_line.split[1]
  `kill #{pid}`
  sleep 1
end

camera = Camera.find_attached
camera.start

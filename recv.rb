require 'serialport'
require 'stringio'
require_relative './debouncer'

$sp = SerialPort.new('/dev/tty.usbserial-A601EYK8', 9600)

debouncer = Debouncer.new

while str = $sp.readpartial(1024) do
  bytes = str.bytes
  if bytes[0] == 0x7e && bytes[12] == 0x01
    debouncer.trigger do
      puts 'take pic'
    end
  end
end

at_exit do
  $sp.close
end

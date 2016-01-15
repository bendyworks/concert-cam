require 'serialport'
require 'stringio'
require_relative './debouncer'

class RemoteButton
  def initialize
    @port = '/dev/cu.usbserial-A601EYK8'
  end

  def listen &blk
    open_serial_port do |sp|
      read_data_frames(sp) do |bytes|
        if button_pressed?(bytes)
          debouncer.trigger do
            puts "triggered"
            blk.call
          end
        end
      end
    end
  end

  def button_pressed?(bytes)
    bytes[0] == 0x7e && bytes[12] == 0x01
  end

  def read_data_frames sp, &blk
    while frame = sp.readpartial(32) do
      blk.call(frame.bytes)
    end
  end

  def open_serial_port &blk
    SerialPort.open(@port, 9600) do |sp|
      blk.call(sp)
    end
  end

  def debouncer
    @debouncer ||= Debouncer.new
  end
end

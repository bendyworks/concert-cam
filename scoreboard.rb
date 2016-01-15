require 'serialport'

class Scoreboard
  def initialize
    port = '/dev/cu.usbmodemfa1261'
    @sp = SerialPort.open port, 38400
    at_exit do
      @sp.close
    end
  end

  def show sym
    str =
      case sym
      when :three then three
      when :two then two
      when :one then one
      when :all then all_leds
      when :blank then blank
      end
    @sp.print str
  end

  def three
    "C3333000\n"
  end

  def two
    "C2222000\n"
  end

  def one
    "C1111000\n"
  end

  def all_leds
    "C8888111\n"
  end

  def blank
    "C    000\n"
  end

  private

  def wrap_binary four_seg
    ([0x42] + four_seg + [0, 0, 0, 0xFF]).pack('c*')
  end
end

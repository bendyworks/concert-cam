require 'serialport'

class Scoreboard
  def initialize
    port = '/dev/cu.usbmodemfa1321'
    @sp = SerialPort.open port, 38400
    at_exit do
      @sp.close
    end
  end

  def show sym
    str =
      case sym
      when :three then wrap_binary(three)
      when :two then wrap_binary(two)
      when :one then wrap_binary(one)
      when :all then all_leds
      when :blank then blank
      end
    @sp.print str
  end

  def three
    [0x38, 0x08, 0x38, 0x0E]
  end

  def two
    [0x31, 0x01, 0x38, 0x0E]
  end

  def one
    [0x08, 0x08, 0x08, 0x0C]
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

import random
import string
import time

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text
from luma.core.legacy.font import SINCLAIR_FONT


serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=1, block_orientation=180, rotate=0)

for i in range(100):
        slovo = random.choice(string.ascii_uppercase)
        with canvas(device) as draw:
                text(draw, (0, 0), slovo, fill="white", font=SINCLAIR_FONT)
                time.sleep(4)

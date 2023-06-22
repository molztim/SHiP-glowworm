from spi import eMUSIC
import utime as time

EMUSIC = eMUSIC(17,18,16,19)
EMUSIC_CONFIG = [1, 144, 144, 111, 120, 3, 6, 3, 15, 0, 3, 0, 0, 3, 0, 38, 31, 3, 15, 3, 4, 4, 25, 3, 1, 0, 244, 1, 1, 1, 1, 120, 1, 0, 1, 1, 0, 240, 1, 1, 1, 1, 120, 1, 0, 1, 1, 0, 236, 1, 1, 1, 1, 120, 1, 0, 1, 1, 0, 240, 1, 1, 1, 1, 120, 1, 0, 1, 1, 0, 228, 1, 1, 1, 1, 120, 1, 0, 1, 1, 0, 224, 1, 1, 1, 1, 120, 1, 0, 1, 1, 0, 232, 1, 1, 1, 1, 120, 1, 0, 1, 1, 0, 229, 1, 1, 1, 1, 120, 1, 0, 1] 
EMUSIC.write_config(EMUSIC_CONFIG)
time.sleep(1)
print("From eMUSIC: ")
print(*EMUSIC.read_config())
import numpy as np
import freenect

array, _ = freenect.sync_get_video()
array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)

print(array)
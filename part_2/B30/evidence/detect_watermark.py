import cv2
from imwatermark import WatermarkDecoder

wm_text = "FAIYAZ_B30"

# load edited image
img = cv2.imread(r"C:\Users\faiyaz\watermarked.png")

# detect watermark
decoder = WatermarkDecoder("bytes", len(wm_text.encode("utf-8")))
decoded = decoder.decode(img, "dwtDct")

print("Decoded watermark from edited image:", decoded.decode("utf-8", errors="ignore"))
import cv2
from imwatermark import WatermarkEncoder, WatermarkDecoder

# watermark text
wm_text = "C"

# load original image
img = cv2.imread(r"C:\Users\faiyaz\original.png.png")

# create encoder
encoder = WatermarkEncoder()
encoder.set_watermark("bytes", wm_text.encode("utf-8"))

# embed invisible watermark
watermarked = encoder.encode(img, "dwtDct")

# save result
cv2.imwrite(r"C:\Users\faiyaz\watermarked.png", watermarked)

print("Watermark embedded and saved as watermarked.png")

# verify immediately
decoder = WatermarkDecoder("bytes", len(wm_text.encode("utf-8")))
decoded = decoder.decode(watermarked, "dwtDct")
print("Decoded watermark from watermarked image:", decoded.decode("utf-8", errors="ignore"))
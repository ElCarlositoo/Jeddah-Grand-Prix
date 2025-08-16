import qrcode

TARGET_URL = "https://ElCarlositoo.github.io/Jeddah-Corniche-Circuit/"

qr = qrcode.make(TARGET_URL)
qr.save("qr.png")

from PIL import Image, ImageDraw

card = Image.new("RGB", (600, 800), "white")
draw = ImageDraw.Draw(card)
draw.text((50, 50), "Scan to view Jeddah Corniche Circuit in AR", fill="black")
qr_img = qrcode.make(TARGET_URL).resize((400, 400))
card.paste(qr_img, (100, 150))
draw.text((50, 600), f"URL: {TARGET_URL}", fill="black")
card.save("QR_Print_Card.png")

print("QR regenerated for", TARGET_URL)

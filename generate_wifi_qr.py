import qrcode

# Replace these values with your own Wi-Fi details
ssid = "YourWiFiNetworkName"
password = "YourWiFiPassword"
encryption = "WPA"  # Supported types: WEP, WPA, or leave blank for open networks

# Create the WiFi QR Code content in the standard format
# Format: WIFI:T:<encryption>;S:<SSID>;P:<password>;;
wifi_qr_data = f"WIFI:T:{encryption};S:{ssid};P:{password};;"

# Generate the QR code
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code; larger number = bigger code
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(wifi_qr_data)
qr.make(fit=True)

# Create the image of the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code as an image file
img_filename = "wifi_qr.png"
img.save(img_filename)

print(f"QR code generated and saved as {img_filename}. Scan this code to connect to {ssid}.")
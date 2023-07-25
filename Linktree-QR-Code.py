import qrcode
from matplotlib import pyplot as plt

# Define the link
link = 'https://linktr.ee/austinboone'

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(link)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Display the generated QR Code
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.show()

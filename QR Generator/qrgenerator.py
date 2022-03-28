import qrcode

def generate(data, border=3, version=1, background='white', fillcolor="black"):
    qr = qrcode.QRCode(
        version=version,
        box_size=10,
        border=border
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(back_color=background, fill_color=fillcolor)
    img.save('qrcode.png')
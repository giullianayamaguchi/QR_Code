from PIL import Image, ImageDraw
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer,VerticalBarsDrawer,SquareModuleDrawer,CircleModuleDrawer, HorizontalBarsDrawer, GappedSquareModuleDrawer
from qrcode.image.styles.colormasks import HorizontalGradiantColorMask, SolidFillColorMask, RadialGradiantColorMask, SquareGradiantColorMask, VerticalGradiantColorMask, ImageColorMask



def style_eyes(img):
  img_size = img.size[0]
  eye_size = 70 #default
  quiet_zone = 40 #default
  mask = Image.new('L', img.size, 0)
  draw = ImageDraw.Draw(mask)
  draw.rectangle((40, 40, 110, 110), fill=255)
  draw.rectangle((img_size-110, 40, img_size-40, 110), fill=255)
  draw.rectangle((40, img_size-110, 110, img_size-40), fill=255)
  return mask


qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data('http://www.amazon.com')

qr_eyes_img = qr.make_image(image_factory=StyledPilImage,
                            eye_drawer=RoundedModuleDrawer(radius_ratio=1),
                            color_mask=SolidFillColorMask(back_color=(255, 255, 255), front_color=(255, 110, 0)))

qr_img = qr.make_image(image_factory=StyledPilImage,
                       module_drawer=CircleModuleDrawer(),
                       color_mask=SolidFillColorMask(front_color=(59, 89, 152)),
                       embeded_image_path=r"C:\Users\Giulliana Yamaguchi\Documents\Prog\Python\projeto\img\Fc-removebg-preview (1).png")

mask = style_eyes(qr_img)
final_img = Image.composite(qr_eyes_img, qr_img, mask)
final_img

final_img.save('qr_rounded.png')
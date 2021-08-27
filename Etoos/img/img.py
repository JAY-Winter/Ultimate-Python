from PIL import Image, ImageChops





def trim(im) :
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()

    if bbox :
        return im.crop(bbox)

im = Image.open("/Applications/mampstack-8.0.3-1/apache2/htdocs/jay/Git/GIT/Python/Ultimate-Python/Etoos/img/문제1번.PNG")
im = trim(im)
# im.save("저장본.PNG", 'PNG')






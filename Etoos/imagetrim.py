from PIL import Image, ImageChops



def crop(im) :
    
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    
    if bbox:
        return im.crop(bbox)

    else : 
        print("실패")
        return

im = Image.open("/Applications/mampstack-8.0.3-1/apache2/htdocs/jay/Git/GIT/Python/Ultimate-Python/Etoos/img/문제1번.PNG")

print(im.size)

crop(im)

print(im.size)


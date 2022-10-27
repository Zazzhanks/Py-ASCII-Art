from PIL import Image, ImageDraw, ImageFont
import math
import os
import concurrent.futures 
chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
extended_chars = u'ÇüéâäàåçêëèïîìÄÅÉæÆôöòûùÿÖÜø£Ø×ƒáíóúñÑªº¿®¬½¼¡«»░▒▓│┤ÁÂÀ©╣║╗╝¢¥┐└┴┬├─┼ãÃ╚╔╩╦╠═╬¤ðÐÊËÈıÍÎÏ┘┌█▄¦Ì▀ÓßÔÒõÕµþÞÚÛÙýÝ¯´­±‗¾¶§÷¸°¨·¹³²■'

charArray = list(chars)
charLength = len(charArray)
interval = charLength/256

scaleFactor = 0.2
oneCharWidth = 8
oneCharHeight = 16

def getChar(inputInt):
    return charArray[(math.floor(inputInt*interval))]

def picture_to_ascii(picture):
    # print(video_name)
    im = Image.open(f'images/video_images/{picture}')
    fnt = ImageFont.truetype('fonts\SpaceMono-Regular.ttf', 15)
    width, height = im.size
    im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), Image.NEAREST)
    width, height = im.size
    pix = im.load()
    outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color = (0, 0, 0))
    d = ImageDraw.Draw(outputImage)

    for i in range(height):
        for j in range(width):
            r, g, b = pix[j, i]
            h = int(r/3 + g/3 + b/3)
            pix[j, i] = (h, h, h)
            # text_file.write(getChar(h))
            d.text((j*oneCharWidth, i*oneCharHeight), getChar(h), font = fnt, fill = (r, g, b))
    
    outputImage.save(f"images/ascii_images/ascii_{picture}")
    print(f"images/ascii_images/ascii_{picture}")

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(picture_to_ascii, os.listdir('images/video_images'))
            

#!/usr/bin/python3

from PIL import Image

def main():
  pixels = []
  mapImg = Image.open('map1.jpeg')
  print("Pixels:\n")
  print(getCoordinates(mapImg))

def getCoordinates(image):
  pixels = []
  width, height = image.size
  for i, pixel in enumerate(image.getdata()):
    pixels.append(i)
  
  coordinates = [divmod(index, width) for index in pixels]
  return coordinates

if __name__ == '__main__':
  main()
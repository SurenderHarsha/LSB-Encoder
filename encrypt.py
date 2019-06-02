from PIL import *

def asciiToBin(ascii):
	return ''.join(str(bin(ord(byte)))[2:].zfill(8) for byte in ascii)

def hide(img, data, outName):
	header, trailer = 2*"11001100",2*"0101010100000000"
	dataBin = header+asciiToBin(data)+trailer
	pixels, mode = list(img.getdata()), img.mode
	newPixels = []

	for i in range(len(dataBin)):
		newPixel = list(pixels[i])
		newPixel[i%len(mode)] = setLSB(newPixel[i%len(mode)], dataBin[i])
		newPixels.append(tuple(newPixel))

	newData = newPixels + pixels[len(newPixels):]

	img.putdata(newData)
	img.save(outName, "PNG")

def setLSB(target, value):
	binary = str(bin(target))[2:]
	if binary[-1] != value:
		binary = binary[:-1] + value
	return int(binary, 2)



message = input("Enter the message you want to encrypt:")
filename =  input("Enter filename of the image you want to store data in:")
img = Image.open(filename)
outName = input("Enter output filename where your data will be stored(It is an image file):")
hide(img,message,outName)
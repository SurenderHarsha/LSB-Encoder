# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 18:50:44 2019

@author: Surender Harsha
"""
header, trailer = 2*"11001100",2*"0101010100000000"
def extract_bits(img):
    
    pixels, mode = list(img.getdata()), img.mode
    binary_data = ''
    for i in range(len(pixels)):
        newPixel = list(pixels[i])
        binary_data += getLSB(newPixel[i%len(mode)])
    return binary_data
		
        
def getLSB(target):
    binary = str(bin(target))[2:]
    return binary[-1]

def matching(b_data,header,trailer):
    b_data=b_data[len(header):]
    location=0
    for i in range(0,len(b_data)-len(trailer)):
        match = b_data[i:i+len(trailer)]
        if match ==  trailer:
            location = i
            break
    return b_data[:location]

def decode_message(data):
    import textwrap
    data = textwrap.wrap(data,8)
    message=''
    for i in data:
        message += chr(int(i,2))
    return message


filename = input("Name of the imagefile:")
img = Image.open(filename)
bits = extract_bits(img)
information = matching(bits,header,trailer)
message = decode_message(information)


print("The encrypted message is:",message)

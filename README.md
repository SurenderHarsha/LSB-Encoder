# LSB-Encoder


### Encrypt.py 

Takes in an image input file, and a message that you want to hide and then outputs an image file in which your message is encrypted.

### Decrypt.py

Takes in an image in which you have stored some information and extracts it.


## Warnings

Be wary that the number of characters in the message is limited to the image size. If the image size is 50x50 then the maximum number of characters it can store is 2500.

The header and tail used to encode must be the same when used for decoding, this sort of acts like the key.

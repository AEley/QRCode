#!/bin/python3
#Import Library
from asyncio.windows_events import NULL
from contextlib import nullcontext
import qrcode # pip install qrcode
import cv2	# pip install opencv-python


def createQRCode(url, filename, fillColour, backColour):
	# Create the QR code
	qr = qrcode.QRCode(
		version=1,
		error_correction=qrcode.constants.ERROR_CORRECT_L,
		box_size=10,
		border=4,
		)
	qr.add_data(url)
	qr.make(fit=True)
	img = qr.make_image(fill_color=fillColour, back_color=backColour)
	# Save it to the file
	img.save(filename)

	# Confirm that the message has been written
	print(url + ' -> ' + filename)

def decryptQRCode(filename):
	# Read in the file
	image = cv2.imread(filename)
	
	#Check to see if it is a QR code
	detector = cv2.QRCodeDetector()
	message, vertices_array, binary_qrcode = detector.detectAndDecode(image)
	# if there is a QR code
	# print the message
	if vertices_array is not None:
		print("QRCode message:" + message)	
	else:
		print("There was some error")

def main():
	# What colours do we want to use?
	background = 'white'
	qrColour = 'black'

	print("QR Codes")
	print("--------")

	# What do we want to do?
	option = input("Would you like to encrypt (E) or decrypt (D)?")
	print (option)

	# Let's handle creating the QR code
	if (option.lower() == "encrypt" or option.lower() == "e"):
		print("Encrypt selected")
		message = input("Please enter the message or url you wish to encrypt:")
		filename = input("Please enter the file name and path for the QR code file:")
		
		createQRCode(message,  filename+'.png', qrColour, background)
	# Let's handle reading the QR code
	elif (option.lower() == "decrypt" or option.lower() == "d"):
		print("Decrypt selected")
		filename = input("Please enter the file name and path to the QR code file:")
		decryptQRCode(filename)
	# Invalid option selected
	else:
		print("Unknown option, please try again")

main()
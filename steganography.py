from stegano import lsb
import random
import re
import argparse
import sys

#./stego -f <filename.png>, -e "secret_message", -p <Password (Optional)>": To embed a secret message.
#./stego -f <secretfile.png>, -x -p <Password supplied>: To extract the secret message.
parser = argparse.ArgumentParser(description="Image Steganography\n[+] Use .png files only: ")
parser.add_argument('-e',type=str,help="To embed a message in the image")
parser.add_argument('-f',help="To pass .png (Image) file")
parser.add_argument('-x',help="To extract the message from the image.",action="store_true")
parser.add_argument('-p',help="To put in a password.", nargs="?", const="no_password_given")
args = parser.parse_args()


try:
	if not args.f:
		print("Please Enter File Name: ")
		print("------[*] Type -h for help------")
		sys.exit(1)
	
	else:
		if args.f and args.e:
			if (".png" in args.f):
				if not args.p:
					args.p = "no_password_given"
				embed = args.p +" "+ args.e
				secret = lsb.hide(args.f,embed)
				random = random.randint(0,100)
				filename = "secret"+str(random)+".png"
				secret.save(filename)
				print("File Saved as ",filename)
			else:
				print("[-]Enter a .png file")
				sys.exit(1)

		elif args.f and args.x:
			if not args.p:
				print("[-]Enter the Password")
				print("[*] If you do not want to supply the password just type apped -p at the end of the query")
				sys.exit(1)
			else:
				message = lsb.reveal(args.f)
				if (len(re.findall('\\b'+args.p+'\\b',message)) != 0):
					message = message.replace(args.p,"")
					print("The secret Message is ",message) 

				else:
					print("Incorrect Password! Could not reveal the Message with the Password.")
						
		else:
			print("[-]Error Occured","\n[*]Try Again with the correct syntax.")
			print("[*]If you are trying to embed a message, try -e flag.")
			print("[*]If you are trying to extract a message then try -x flag")
			sys.exit(1)

except FileNotFoundError:
	print("[-]File not Found")
	
except KeyboardInterrupt:
	print("[-]Keyboard Interrupt")
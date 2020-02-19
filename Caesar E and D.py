"""
========================================
|Date : 30/12/2018                     |
========================================
This programme is used to encrypt the messgae and decrypt the message with (Caesar Cipher) 
"""
# START
print("1- To encrypt the message")
print("2- To decrypt the message")
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]  #list of alpha to use in encryption and decryption
choose = int(input("choose from the options:"))
if choose == 1:
	# Start to Encryption
	word = str(input("Enter the message:"))  #message that will received from the user
	key = int(input("Enter the key:"))  #key that will received from the user and it will use in the encryption
	cipher = "" # variable to store the message after encryption
	increase = 1
	for i in range(len(word)):
		if word[i] in alpha:
			c = alpha.index(word[i]) + key  # adding the number of index in alpha to the key
			try:	
				cipher = cipher + alpha[c]
			except IndexError:
				increase = increase + 1
				end = alpha * increase
				cipher = cipher + end[c]
		else:
			continue
	print("the cipher is: {}".format(cipher))
	# End the Encryption
elif choose == 2:
	# Start to Decryption
	cipher = str(input("Enter the cipher:"))
	key = int(input("Enter the key:"))
	text = ""
	for i in range(len(cipher)):
		q = alpha.index(cipher[i]) - key
		plantext = alpha[q]
		text = text + plantext
	print("The message is: {}".format(text))
	# End the Decryption
else:
	print("The number that you choose was not in the options")
######################################END#################################

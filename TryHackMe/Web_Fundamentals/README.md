# TryHackMe [Web Fundamentals](https://tryhackme.com/room/webfundamentals)
### References
* DarkSec. (2020). TryHackMe Official Web Fundamentals Walkthrough [YouTube Video]. In YouTube. https://youtu.be/hYMUBaRM0CE
* Mozilla. (2021, May 31). 401 Unauthorized - HTTP. Mozilla. https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401
* Mozilla. (2021, May 31). 418 I’m a teapot - HTTP. Mozilla. https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/418
## How do we load websites?
### What request verb is used to retrieve page content?
* According to the information provided in the reading material:
> Once the browser knows the server's IP address, it can ask the server for the web page. This is done with a HTTP GET request.

**Answer**: `GET`
### What port do web servers normally listen on?
* According to the information provided in the reading material:
> By default, HTTP runs on port 80 and HTTPS runs on port 443.

**Answer**: `80`
### What's responsible for making websites look fancy?
* According to the information provided in the reading material:
> CSS allows you to change how the page looks and make it look fancy. 

**Answer**: `CSS`
## More HTTP - Verbs and request formats
### What verb would be used for a login?
* According to the information provided in the reading material:
> POST requests are used to send data to a web server, like adding a comment or performing a login.

**Answer**: `POST`
### What verb would be used to see your bank balance once you're logged in?
**Answer**: `GET`
### Does the body of a `GET` request matter (Yea/Nay)?
**Answer**: `Nay`
### What's the status code for `I'm a teapot`?
* According to a [Mozilla page](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/418):
> The HTTP **`418 I'm a teapot`** client error response code indicates that the server refuses to brew coffee because it is, permanently, a teapot. A combined coffee/tea pot that is temporarily out of coffee should instead return 503. This error is a reference to Hyper Text Coffee Pot Control Protocol defined in April Fools' jokes in 1998 and 2014.

**Answer**: `418`
### What status code will you get if you need to authenticate to access some content, and you're unauthenticated?
* According to a [Mozilla page](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401):
> The HTTP **`401 Unauthorized`** client error status response code indicates that the request has not been applied because it lacks valid authentication credentials for the target resource.

**Answer**: `401`
## Mini CTF
There's a web server running on `http://<MACHINE_IP>:8081`. Connect to it and get the flags!
* GET request. Make a `GET` request to the web server with path `/ctf/get`
* POST request. Make a `POST` request with the body `flag_please` to `/ctf/post`
* Get a cookie. Make a `GET` request to `/ctf/getcookie` and check the cookie the server gives you
* Set a cookie. Set a cookie with name `flagpls` and value `flagpls` and make a `GET` request to `/ctf/sendcookie`
### What's the `GET` flag?
```bash
$ curl -X GET <MACHINE_IP>:8081/ctf/get
thm{162520bec925bd7979e9ae65a725f99f}
```
**`GET` Flag**: `thm{162520bec925bd7979e9ae65a725f99f}`
### What's the `POST` flag?
```bash
$ curl -X POST -d "flag_please" <MACHINE_IP>:8081/ctf/post
thm{3517c902e22def9c6e09b99a9040ba09}
```
**`POST` Flag**: `thm{3517c902e22def9c6e09b99a9040ba09}`
### What's the "Get a cookie" flag?
```bash
$ curl -X GET -c - <MACHINE_IP>:8081/ctf/getcookie
Check your cookies!# Netscape HTTP Cookie File
# https://curl.se/docs/http-cookies.html
# This file was generated by libcurl! Edit at your own risk.

<MACHINE_IP>   FALSE   /       FALSE   0       flag    thm{91b1ac2606f36b935f465558213d7ebd}
```
**Flag**: `thm{91b1ac2606f36b935f465558213d7ebd}`
### What's the "Set a cookie" flag?
```bash
$ curl -X GET --cookie "flagpls=flagpls" <MACHINE_IP>:8081/ctf/sendcookie 
thm{c10b5cb7546f359d19c747db2d0f47b3}
```
**Flag**: `thm{c10b5cb7546f359d19c747db2d0f47b3}`
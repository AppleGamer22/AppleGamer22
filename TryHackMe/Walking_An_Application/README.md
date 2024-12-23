# TryHackMe [Walking An Application](https://tryhackme.com/room/walkinganapplication)
## Viewing The Page Source
### What is the flag from the HTML comment?

```html
<!--
This page is temporary while we work on the new homepage @ /new-home-beta
-->
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Acme IT Support - Home</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://pro.fontawesome.com/releases/v5.12.0/css/all.css" integrity="sha384-ekOryaXPbeCpWQNxMwSWVvQ0+1VrStoPJq54shlYhR8HzQgig1v5fas6YgOqLoKz" crossorigin="anonymous">
        <link rel="stylesheet" href="/assets/bootstrap.min.css">
    <link rel="stylesheet" href="/assets/style.css">
</head>
<body>
    <nav class="navbar navbar-inverse navbar-fixed-top">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#">Acme IT Support</a>
            </div>
            <div id="navbar" class="collapse navbar-collapse">
                <ul class="nav navbar-nav">
                    <li class="active"><a href="/">Home</a></li>
                    <li><a href="/news">News</a></li>
                    <li><a href="/contact">Contact</a></li>
                    <li><a href="/customers">Customers</a></li>
                </ul>
            </div><!--/.nav-collapse -->
        </div>
    </nav><div class="container" style="padding-top:60px">
    <h1 class="text-center">Acme IT Support</h1>
    <div class="row">
        <div class="col-md-8 col-md-offset-2 text-center">
            <img src="/assets/staff.png">
            <p class="welcome-msg">Our dedicated staff are ready <a href="/secret-page">to</a> assist you with your IT problems.</p>
        </div>
    </div>
</div>
<script src="/assets/jquery.min.js"></script>
<script src="/assets/bootstrap.min.js"></script>
<script src="/assets/site.js"></script>
</body>
</html>
<!--
Page Generated in 0.04653 Seconds using the THM Framework v1.2 ( https://static-labs.tryhackme.cloud/sites/thm-web-framework )
-->
```

**Flag**: `THM{HTML_COMMENTS_ARE_DANGEROUS}`
### What is the flag from the secret link?
* From the home page:
```html
<p class="welcome-msg">Our dedicated staff are ready <a href="/secret-page">to</a> assist you with your IT problems.</p>
```

**Flag**: `THM{NOT_A_SECRET_ANYMORE}`
### What is the directory listing flag?
1. Go to <http://10.10.92.199/assets/>
2. Go to <http://10.10.92.199/assets/flag.txt>

**Flag**: `THM{INVALID_DIRECTORY_PERMISSIONS}`
### What is the framework flag?
1. Go to <https://static-labs.tryhackme.cloud/sites/thm-web-framework/changelog.html>, it hints about a ZIP file.
2. Download and extract the flag from <http://10.10.92.199/tmp.zip>

**Flag**: `THM{KEEP_YOUR_SOFTWARE_UPDATED}`
## Inspector
### What is the flag behind the paywall?
1. Go to <http://10.10.151.240/news/article?id=3>
2. Set `display: none` for the CSS selector `div.premium-customer-blocker`:
![set CSS property from DevTools](display_none.jpg)

**Flag**: `THM{NOT_SO_HIDDEN}`
## Debugger
1. Go to <http://10.10.151.240/contact>
2. Find the `flash.min.js` file under sources and format it.
3. Set a breakpoint on line 48 and refresh the page:
![add JavaScript breakpoint from DevTools](flash_breakpoint.jpg)

**Flag**: `THM{CATCH_ME_IF_YOU_CAN}`
## Network
### What is the flag shown on the `contact-msg` network request?
1. Go to <http://10.10.151.240/contact>
2. Click the Send Message button
3. Find the `contact-msg` network request:
![view network data from DevTools](response_flag.jpg)

**Flag**: `THM{GOT_AJAX_FLAG}`
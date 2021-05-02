# TryHackMe [CC: Pen Testing](https://tryhackme.com/room/ccpentesting) Samba
### References
* Evans, S. (2020, October 3). `ShawnDEvans/smbmap/README.md`. GitHub. https://github.com/ShawnDEvans/smbmap/blob/master/README.md
* Samba Team. (2012). `smbclient`. samba.org. https://www.samba.org/samba/docs/current/man-html/smbclient.1.html
## `smbmap`
### How do you set the username to authenticate with?
**Answer**: `-u`
### What about the password?
**Answer**: `-p`
### How do you set the host?
**Answer**: `-H`
### What flag runs a command on the server (assuming you have permissions that is)?
**Answer**: `-x`
### How do you specify the share to enumerate?
**Answer**: `-s`
### How do you set which domain to enumerate?
**Answer**: `-d`
### What flag downloads a file?
**Answer**: `--download`
### What about uploading one?
**Answer**: `--upload`
### Given the username `"admin"`, the password `"password"`, and the ip `10.10.10.10`, how would you run `"ipconfig"` on that machine?
**Answer**: `smbmap -u "admin" -p "password" -H 10.10.10 -x "ipconfig"`
## `smbclient`
### How do you specify which domain (workgroup) to use when connecting to the host?
**Answer**: `-w`
### How do you specify the ip address of the host?
**Answer**: `-I`
### How do you run the command `"ipconfig"` on the target machine?
**Answer**: `-c "ipconfig"`
### How do you specify the username to authenticate with?
**Answer**: `-u`
### How do you specify the password to authenticate with?
**Answer**: `-p`
### What flag is set to tell `smbclient` to not use a password?
**Answer**: `-N`
### While in the interactive prompt, how would you download the file test, assuming it was in the current directory?
**Answer**: `get test`
### In the interactive prompt, how would you upload your `/etc/hosts` file?
**Answer**: `put /etc/hosts`





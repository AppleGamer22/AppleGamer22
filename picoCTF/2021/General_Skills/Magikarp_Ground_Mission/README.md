# picoCTF 2021 [Magikarp Ground Mission](https://play.picoctf.org/practice/challenge/189)
## Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin.
1. The initial directory contains the first third of the flag and instructions for the second third:
```bash
$ ssh ctf-player@venus.picoctf.net -p 50710
ctf-player@pico-chall$ ls
1of3.flag.txt  instructions-to-2of3.txt
ctf-player@pico-chall$ cat 1of3.flag.txt 
picoCTF{xxsh_
ctf-player@pico-chall$ cat instructions-to-2of3.txt 
Next, go to the root of all things, more succinctly `/`
```
2. The root (`/`) directory contains the second third of the flag and instructions for the last third:
```
ctf-player@pico-chall$ cd /
ctf-player@pico-chall$ ls
2of3.flag.txt  bin  boot  dev  etc  home  instructions-to-3of3.txt  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
ctf-player@pico-chall$ cat 2of3.flag.txt 
0ut_0f_\/\/4t3r_
ctf-player@pico-chall$ cat instructions-to-3of3.txt 
Lastly, ctf-player, go home... more succinctly `~`
```
3. The home (`~`) directory contains last third of the flag:
```
ctf-player@pico-chall$ cd ~
ctf-player@pico-chall$ ls
3of3.flag.txt  drop-in
ctf-player@pico-chall$ cat 3of3.flag.txt 
1118a9a4}
ctf-player@pico-chall$
```

**Answer**: `picoCTF{xxsh_0ut_0f_\/\/4t3r_1118a9a4}`
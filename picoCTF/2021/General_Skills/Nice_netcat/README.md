# picoCTF 2021 [Nice netcat...](https://play.picoctf.org/practice/challenge/156)
## There is a nice program that you can talk to by using this command in a shell: `nc mercury.picoctf.net 22342`, but it doesn't speak English...
1. The `nc` output could be ASCII.
```
$ nc mercury.picoctf.net 22342
112 
105 
99 
111 
67 
84 
70 
123 
103 
48 
48 
100 
95 
107 
49 
116 
116 
121 
33 
95 
110 
49 
99 
51 
95 
107 
49 
116 
116 
121 
33 
95 
53 
102 
98 
53 
101 
53 
49 
100 
125 
10 
$ nc mercury.picoctf.net 22342 > nc_output.txt
```
2. The following python script reads `nc_output.txt`, converts each line with a number to an ASCII character:
```python
output = ""
with open("nc_output.txt") as file:
	lines = file.readlines()
	for line in lines:
		if line.strip().isdigit():
			output += chr(int(line.strip()))
print(output)
```
1. `nice_netcat.py` prints:
```
$  python nice_netcat.py
picoCTF{g00d_k1tty!_n1c3_k1tty!_5fb5e51d}
``` 
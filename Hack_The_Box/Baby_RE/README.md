# Hack The Box [Baby RE](https://app.hackthebox.eu/challenges/92)
1. Make the `baby` binary `chmod +x baby` executable.
2. Trace the binary `baby`
```bash
$ ltrace ./baby
puts("Insert key: "Insert key: 
)                                                                                                                                  = 13
fgets(123
"123\n", 20, 0x7f97fd834800)                                                                                                                    = 0x7ffebbe5a320
strcmp("123\n", "abcde122313\n")                                                                                                                      = -48
puts("Try again later."Try again later.
)                                                                                                                              = 17
+++ exited (status 0) +++
```
3. Insert `abcde122313` as input
```
$ ./baby
Insert key:
abcde122313
HTB{B4BY_R3V_TH4TS_EZ}
```

**Flag**: `HTB{B4BY_R3V_TH4TS_EZ}`
```bash
user@thm:~$ ping -c 4 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data
64 bytes from 8.8.8.8: icmp_seq=1 ttl=56 time=7.16 ms
64 bytes from 8.8.8.8: icmp_seq=1 ttl=56 time=8.83 ms
64 bytes from 8.8.8.8: icmp_seq=1 ttl=56 time=8.29 ms
64 bytes from 8.8.8.8: icmp_seq=1 ttl=56 time=8.31 ms
--- 8.8.8.8 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 4006ms
rtt min/avg/max/mdev = 8.132/9.428/10.957/1.057 ms
Flag: THM{I_PINGED_THE_SERVER}
```
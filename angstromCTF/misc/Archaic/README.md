# Archaic
The archaeological team at ångstromCTF has uncovered an archive from over 100 years ago! Can you read the contents?

Access the file at `/problems/2021/archaic/archive.tar.gz` on the shell server.
## Solution
1. By using `scp`, copy the archive from the ångstromCTF server, to your machine,
2. extract the files,
3. add read permission to `flag.txt`,
4. open `flag.txt`.
```shell
scp team<number>@shell.actf.co:/problems/2021/archaic/archive.tar.gz .
tar -xf archive.tar.gz
chmod +r flag.txt
cat flag.txt
```
**Flag**: `actf{thou_hast_uncovered_ye_ol_fleg}`

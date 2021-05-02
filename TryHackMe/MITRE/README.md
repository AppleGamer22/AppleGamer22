# TryHackMe [MITRE](https://www.tryhackme.com/room/mitre)
#### References
* Jepma, J. (2021, January 11). MITRE TryHackMe Write-up. Jon Jepma. https://www.jonjepma.com/ctf-write-ups/mitre-tryhackm/
## ATT&CK&reg; Framework
### Only blue teamers will use the ATT&CK Matrix?
**Answer**: `Nay`
### What is the ID for [this phishing](https://attack.mitre.org/techniques/T1566/) technique?
**Answer**: `T1566`
### Based on this technique, what mitigation covers identifying social engineering techniques?
* According to [MITRE ATT&CK](https://attack.mitre.org/techniques/T1566/):
> #### Mitigations
> Mitigation | Description
> --|--
> User Training | Users can be trained to identify social engineering techniques and phishing emails.

**Answer**: `User Training`
### There are other possible areas for detection for this technique, which occurs after what other technique?
* According to [MITRE ATT&CK](https://attack.mitre.org/techniques/T1566/):
> Anti-virus can potentially detect malicious documents and files that are downloaded on the user's computer. Many possible detections of follow-on behavior may take place once [User Execution](https://attack.mitre.org/techniques/T1204) occurs.

**Answer**: `User Execution`
### What group has used spear phishing in their campaigns?
* According to [MITRE ATT&CK](https://attack.mitre.org/techniques/T1566/):
> #### Procedure Examples
> Name | Description
> --|--
> Dragonfly | Dragonfly has used spearphising campaigns to gain access to victims.<sup>[[1]](https://www.secureworks.com/research/resurgent-iron-liberty-targeting-energy-sector)</sup>
**Answer**: `Dragonfly`
### Based on the information for this group, what are their associated groups?
* According to [MITRE ATT&CK](https://attack.mitre.org/groups/G0035/):
> Associated Groups: TG-4192, Crouching Yeti, IRON LIBERTY, Energetic Bear

**Answer**: `TG-4192, Crouching Yeti, IRON LIBERTY, Energetic Bear`
### What tool is attributed to this group to transfer tools or files from one host to another within a compromised environment?
* According to [MITRE ATT&CK](https://attack.mitre.org/groups/G0035/):
> #### Software
> ID | Name | References | Techniques
> --|--|--|--
> [S0029](https://attack.mitre.org/software/S0029) | [PsExec](https://attack.mitre.org/software/S0029) | [[2]](https://www.secureworks.com/research/resurgent-iron-liberty-targeting-energy-sector) | [Lateral Tool Transfer](https://attack.mitre.org/techniques/T1570), [Remote Services](https://attack.mitre.org/techniques/T1021): [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002), [System Services](https://attack.mitre.org/techniques/T1569): [Service Execution](https://attack.mitre.org/techniques/T1569/002)

**Answer**: `PsExec`
### Based on the information about this tool, what group used a customized version of it?
* According to [MITRE ATT&CK](https://attack.mitre.org/software/S0029/):
> #### Groups That Use This Software
> ID | Name | References
> --|--|--
> G0053 | FIN5 | FIN5 uses a customized version of PsExec.<sup>[[4]](https://www.youtube.com/watch?v=fevGZs0EQu8)</sup>

**Answer**: `FIN5`
### This group has been active since what year?
* According to [MITRE ATT&CK](https://attack.mitre.org/groups/G0053/):
> FIN5 is a financially motivated threat group that has targeted personally identifiable information and payment card information. The group has been active since at least 2008 and has targeted the restaurant, gaming, and hotel industries. The group is made up of actors who likely speak Russian. <sup>[[1]](https://www2.fireeye.com/WBNR-Are-you-ready-to-respond.html) [[2]](https://www.youtube.com/watch?v=fevGZs0EQu8) [[3]](https://www.darkreading.com/analytics/prolific-cybercrime-gang-favors-legit-login-credentials/d/d-id/1322645?)</sup>

**Answer**: `2008`
### Instead of Mimikatz, what OS Credential Dumping tool is does this group use?
* According to [MITRE ATT&CK](https://attack.mitre.org/groups/G0053/):
> #### Software
> ID | Name | References | Techniques
> --|--|--|--
> [S0005](https://attack.mitre.org/software/S0005) | [Windows Credential Editor](https://attack.mitre.org/software/S0005) | [[3]](https://www.darkreading.com/analytics/prolific-cybercrime-gang-favors-legit-login-credentials/d/d-id/1322645?)[[2]](https://www.youtube.com/watch?v=fevGZs0EQu8) | [OS Credential Dumping](https://attack.mitre.org/techniques/T1003): [LSASS Memory](https://attack.mitre.org/techniques/T1003/001)

**Answer**: `2008`
## CAR Knowledge Base
### For the above analytic, what is the pseudocode a representation of?
* From the background information: 
> We're also provided with Pseudocode and a query on how to search for this specific analytic within Splunk. A pseudocode is a plain, human-readable way to describe a set of instructions or algorithms that a program or system will perform.

**Answer**: `Splunk search`
### What tactic has an ID of TA0003?
* According to [MITRE ATT&CK](https://attack.mitre.org/tactics/TA0003/):
> ID: TA0003

**Answer**: `TA0003`
### What is the name of the library that is a collection of Zeek (BRO) scripts?
* According to [MITRE CAR](https://car.mitre.org/):
> #### Analytic Source Code Libraries
> Some analytics are built as source code for specific products. In these ca#### ses, code might support a broad set of detections in a way that makes it hard to describe a set of distinct analytics. For these types of analytics, rather than integrating them into the main CAR site, we’ve collected them under a library of implementations. Currently, the only library is [BZAR](https://github.com/mitre-attack/bzar), a collection of Zeek (Bro) scripts looking primarily at SMB and RPC traffic.

**Answer**: `BZAR`
### What is the name of the technique for running executables with the same hash and different names?
* According to [MITRE CAR](https://car.mitre.org/):
> #### Analytics
> ID | Name | Submission Date | ATT&CK Techniques | Implementations | Applicable Platforms
> --|--|--|--|--|--
> [CAR-2013-05-009](https://car.mitre.org/analytics/CAR-2013-05-009/) | Running executables with same hash and different names | May 23 2013 | [Masquerading](https://attack.mitre.org/techniques/T1036/) | Dnif, Logpoint, Sigma, Splunk | Windows, Linux, macOS

**Answer**: `Masquerading`
### Examine CAR-2013-05-004, what additional information is provided to analysts to ensure coverage for this technique?
**Answer**: `Unit Tests`
## Shield Active Defense
### Which Shield tactic has the most techniques?
* On https://shield.mitre.org/matrix/, The Detect tactic has the most techniques.

**Answer**: `Detect`
### Is the technique Decoy Credentials listed under the tactic from the previous question (Yay/Nay)?
* The technique Decoy Credentials is listed under the Detect tactic.

**Answer**: `Yay`
### Explore `DTE0011`, what is the ID for the use case where a defender can plant artifacts on a system to make it look like a virtual machine to the adversary?
* According to [MITRE Shield](https://shield.mitre.org/techniques/DTE0011/):
> #### Use Cases
> ID | Description
> --|--
> DUC0234 | A defender can plant files, registry entries, software, processes, etc. to make a system look like a VM when it is not.
**Answer**: `DUC0234`
### Based on the above use case, what is its ATT&CK&reg; Technique mapping?
* According to [MITRE Shield](https://shield.mitre.org/techniques/DTE0011/):
> #### ATT&CK&reg; Techniques
> ID | Name | ATT&CK Tactics
> --|--|--
> [T1497](https://attack.mitre.org/techniques/T1497) | Virtualization/Sandbox Evasion | [Defense Evasion](https://shield.mitre.org/attack_mapping/TA0005), [Discovery](https://shield.mitre.org/attack_mapping/TA0007)

**Answer**: `T1497`
### Continuing from the previous question, look at the information for this ATT&CK&reg; Technique, what 2 programs are listed that adversary's will check for?
* According to [MITRE ATT&CK](https://attack.mitre.org/tactics/TA0003/):
> Adversaries may use several methods to accomplish [Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1497) such as checking for security monitoring tools (e.g., Sysinternals, Wireshark, etc.) or other system artifacts associated with analysis or virtualization.  Adversaries may also check for legitimate user activity to help determine if it is in an analysis environment. Additional methods include use of sleep timers or loops within malware code to avoid operating within a temporary sandbox.<sup>[[1]](https://unit42.paloaltonetworks.com/ups-observations-on-cve-2015-3113-prior-zero-days-and-the-pirpi-payload/)</sup>
## ATT&CK&reg; Emulation Plans
### How many phases does APT3 Emulation Plan consists of?
* According to [MITRE ATT&CK](https://attack.mitre.org/resources/adversary-emulation-plans/):
![APT3 Phases Diagrams](https://attack.mitre.org/theme/images/APT3_phase_diagram.png)

**Answer**: `3`
### Under Persistence, what binary was replaced with `cmd.exe`?
* According to [MITRE ATT&CK](https://attack.mitre.org/docs/APT3_Adversary_Emulation_Plan.pdf):
> APT3 has replaced the Sticky Keys binary
(`C:\Windows\System32\sethc.exe`) with `cmd.exe` [[T1015 -
Accessibility Features]](https://attack.mitre.org/wiki/Technique/T1015) and enabled Remote Desktop Protocol
(RDP) if it is not already enabled [[T1076 – Remote Desktop
Protocol]](https://attack.mitre.org/wiki/Technique/T1076).

**Answer**: `sethc.exe`
### Examining APT29, what 2 tools were used to execute the first scenario?
* According to [The Center for Threat-Informed Defense](https://github.com/center-for-threat-informed-defense/adversary_emulation_library/blob/master/apt29/Emulation_Plan/Scenario_1/Infrastructure.md):
> #### A note about red team payloads
> * This evaluation utilizes four payloads that model APT29 malware.
> * The payloads are customized variants of reverse shells from Pupy RAT and Metasploit.
> * Pre-compiled payloads are available in the [resources](https://github.com/center-for-threat-informed-defense/adversary_emulation_library/blob/master/apt29/Resources) directory; however, they are configured to connect back to static IP addresses `192.168.0.5` and `192.168.0.4`.
> * If you would like to build the payloads yourself, please see [`payload_configs.md`](https://github.com/center-for-threat-informed-defense/adversary_emulation_library/blob/master/apt29/Resources/Scenario_1/payload_configs.md) for further instructions.

**Answer**: `Pupy and Metasploit`
### What tool was used to execute the second scenario?
* According to [The Center for Threat-Informed Defense](https://github.com/center-for-threat-informed-defense/adversary_emulation_library/blob/master/apt29/Emulation_Plan/Scenario_2/Infrastructure.md):
> #### Emulation Team Infrastructure
> 1. Server running an offensive framework (we tested and executed using PoshC2 -- https://github.com/nettitude/> PoshC2) capable of:
> * Executing native PowerShell commands
> * Loading and executing PowerShell scripts (.ps1)
> * Generating a DLL payload and an encoded PowerShell oneliner
> * Receiving and maintaining multiple callbacks at once

**Answer**: `PoshC2`
### Where can you find step-by-step instructions to execute both scenarios?
**Answer**: `ATT&CK Arsenal`
## ATT&CK&reg; and Threat Intelligence
### What is a group that targets your sector who has been in operation since at least 2013?
* According to [MITRE ATT&CK](https://attack.mitre.org/groups/G0064/):
> [APT33](https://attack.mitre.org/groups/G0064) is a suspected Iranian threat group that has carried out operations since at least 2013. The group has targeted organizations across multiple industries in the United States, Saudi Arabia, and South Korea, with a particular interest in the aviation and energy sectors.<sup>[[1]](https://www.fireeye.com/blog/threat-research/2017/09/apt33-insights-into-iranian-cyber-espionage.html)[[2]](https://www.brighttalk.com/webcast/10703/275683)</sup>

**Answer**: `APT33`
### Does this group use Stuxnet (Yay/Nay)?
**Answer**: `Nay`
### As your organization is migrating to the cloud, is there anything attributed to this APT group that you should focus on, and if so, what is it?
* According to [MITRE ATT&CK](https://attack.mitre.org/groups/G0064/):
> Techniques Used
> Domain | ID | Name | Use
> --|--|--|--
> Enterprise | [T1078.004](https://attack.mitre.org/techniques/T1078/004) | [Cloud Accounts](https://attack.mitre.org/techniques/T1078/004) | [APT33](https://attack.mitre.org/groups/G0064) has used compromised Office 365 accounts in tandem with [Ruler](https://attack.mitre.org/software/S0358) in an attempt to gain control of endpoints.<sup>[[3]](https://www.microsoft.com/security/blog/2020/06/18/inside-microsoft-threat-protection-mapping-attack-chains-from-cloud-to-endpoint/)</sup>

**Answer**: `Cloud Accounts`
### What tool is associated with this technique?
**Answer**: `Ruler`
### Per the detection tip, what should you be detecting?
* According to [MITRE ATT&CK](https://attack.mitre.org/techniques/T1078/004/):
> #### Detection
> Monitor the activity of cloud accounts to detect abnormal or malicious behavior, such as accessing information outside of the normal function of the account or account usage at atypical hours.

**Answer**: `Abnormal or malicious behavior`
### What platforms does this affect?
**Answer**: `AWS, Azure, Azure AD, GCP, Office 365, SaaS`
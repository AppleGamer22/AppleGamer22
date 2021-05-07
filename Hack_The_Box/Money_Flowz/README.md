# Hack The Box [Money Flowz](https://app.hackthebox.eu/challenges/123)
### References
* Harry. (2020, October 30). HackTheBox: Money Flowz OSINT Challenge - MyCrypto - Medium. Medium; MyCrypto. https://medium.com/mycrypto/hackthebox-money-flowz-osint-challenge-df9ee05b25ce
## Description
> Frank Vitalik is a hustler, can you figure out where the money flows?
## Challenge
1. Frank Vitalik has posted a post regarding cryptocurrencies on reddit:
<iframe id="reddit-embed" src="https://www.redditmedia.com/user/frankvitalik/comments/goxefp/incredible_scam_giveaway_you_can_get_free_coins/?ref_source=embed&amp;ref=share&amp;embed=true&amp;theme=dark" sandbox="allow-scripts allow-same-origin allow-popups" style="border: none;" height="170" width="640" scrolling="no"></iframe>

2. The reddit post leads to [Freecoinz!!](https://steemit.com/htb/@freecoinz/freecoinz), which contains the Ethereum address `0x1b3247Cd0A59ac8B37A922804D150556dB837699`.
3. The first two outgoing transaction contain the hexadecimal string `0x4854427b43727950743043757272336e63795f31735f46754e7a21217d`:
   * [0xc9dc91514cd66e1bb032f12056a06a31b87e3b8905968047643b9e16c0dbb4ba](https://ropsten.etherscan.io/tx/0xc9dc91514cd66e1bb032f12056a06a31b87e3b8905968047643b9e16c0dbb4ba)
   * [0xe1320c23f292e52090e423e5cdb7b4b10d3c70a8d1b947dff25ae892609f2ef4](https://ropsten.etherscan.io/tx/0xe1320c23f292e52090e423e5cdb7b4b10d3c70a8d1b947dff25ae892609f2ef4)
4. This hexadecimal string translates to `HTB{CryPt0Curr3ncy_1s_FuNz!!}` in UTF-8.

**Flag**: `HTB{CryPt0Curr3ncy_1s_FuNz!!}`
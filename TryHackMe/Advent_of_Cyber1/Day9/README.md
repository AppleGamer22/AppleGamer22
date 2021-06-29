# TryHackMe [Advent of Cyber 1](https://tryhackme.com/room/25daysofchristmas) Day 9
## What is the value of the flag?
* [`main.py`](main.py) makes HTTP GET requests until the JSON response marks the end:
```python
from typing import TypedDict, List
from requests import get

class Response3000(TypedDict):
	value: str
	next: str

url = "http://10.10.169.100:3000/"

path = ""
values: List[str] = []

if __name__ == "__main__":
	while path != "end":
		response: Response3000 = get(url + path).json()
		if response["value"] != "end":
			values.append(response["value"])
		path = response["next"]
	print("".join(values))
```

**Flag**: `sCrIPtKiDd`
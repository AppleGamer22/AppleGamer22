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

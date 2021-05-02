output = ""
with open("nc_output.txt") as file:
	lines = file.readlines()
	for line in lines:
		if line.strip().isdigit():
			output += chr(int(line.strip()))
print(output)
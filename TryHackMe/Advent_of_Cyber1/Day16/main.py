# https://muirlandoracle.co.uk/2020/01/06/tryhackme-christmas-2019-challenge-write-up/#Day_Sixteen_-_File_Confusion
from os import listdir, getcwd, system
from zipfile import ZipFile

cwd = getcwd()

# How many files did you extract (excluding all the .zip files)?
with ZipFile(f"{cwd}/final-final-compressed.zip", "r") as zipfile:
	zipfile.extractall(f"{cwd}/extracted_zips")

for file in listdir(f"{cwd}/extracted_zips"):
	with ZipFile(f"{cwd}/extracted_zips/{file}") as zipfile:
		zipfile.extractall(f"{cwd}/extracted_files")

system("rm -r extracted_zips")

print("How many files did you extract (excluding all the .zip files)?")
print(f"Answer: {len(listdir(f'{cwd}/extracted_files'))}")

# How many files contain Version: 1.1 in their metadata?
directory = "extracted_files"
for file in listdir(directory):
	system(f"exiftool {directory}/{file} >> exiftool.txt")

with open("exiftool.txt") as metadata_file:
	metadata = metadata_file.readlines()
system("rm exiftool.txt")

counter = 0
for line in metadata:
	if "Version" in line and "1.1" in line:
		counter += 1

print("How many files contain Version: 1.1 in their metadata?")
print(f"Answer: {counter}")

# Which file contains the password?
print("Which file contains the password?")
for filename in listdir("extracted_files"):
	try:
		with open(f"extracted_files/{filename}", "r") as file:
			data = file.read()
			if "password" in data:
				print(f"Answer: {filename}")
				break
	except:
		continue

system("rm -r extracted_files")
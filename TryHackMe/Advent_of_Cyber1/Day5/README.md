# TryHackMe [Advent of Cyber 1](https://tryhackme.com/room/25daysofchristmas) Day 5
## What is Lola's date of birth?
1. Get the Name of the author using `exiftool`:
```bash
$ exiftool thegrinch.jpg 
ExifTool Version Number         : 12.26
File Name                       : thegrinch.jpg
Directory                       : .
File Size                       : 69 KiB
File Modification Date/Time     : 2021:06:28 17:00:31+10:00
File Access Date/Time           : 2021:06:28 17:00:31+10:00
File Inode Change Date/Time     : 2021:06:28 17:00:36+10:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
XMP Toolkit                     : Image::ExifTool 10.10
Creator                         : JLolax1
Image Width                     : 642
Image Height                    : 429
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 642x429
Megapixels                      : 0.275
```
2. Search `@JLolax1` on [Twitter](https://twitter.com/JLolax1) and find the user's date of birth.

**Answer**: `December 29, 1900`
## What is Lola's current occupation?
* According to [`@JLolax1`](https://twitter.com/JLolax1) Twitter bio.
**Answer**: `Santa's Helper`
## What phone does Lola make?
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Oooo! <br><br>Us Elves can now make iPhone&#39;s! Who&#39;da thought it!<br><br>~ Sent from iPhone X</p>&mdash; Elf Lola (@JLolax1) <a href="https://twitter.com/JLolax1/status/1202335449311825929?ref_src=twsrc%5Etfw">December 4, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

**Answer**: `iPhone X`
## What date did Lola first start her photography?
1. Go the earliest version of Lola's [website](https://web.archive.org/web/20191023204650/https://lolajohnson1998.wordpress.com/).
2. The website became public on 23/10/2019.
3. Lola says in the website:
> I started as a freelance photographer five years ago today! To celebrate, I am knocking 20% of all event photography days!

**Answer**: `23/10/2014`
## What famous woman does Lola have on her web page?
* Lola features a painting  of [Ada Lovelace](https://web.archive.org/web/20191023204650/https://lolajohnson1998.wordpress.com/#jp-carousel-22)

**Answer**: `Ada Lovelace`
# TryHackMe [Advent of Cyber 1](https://tryhackme.com/room/25daysofchristmas) Day 14
## What is the name of the file you found?
```xml
$ curl -s advent-bucket-one.s3.amazonaws.com | xmllint --format -
<?xml version="1.0" encoding="UTF-8"?>
<ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <Name>advent-bucket-one</Name>
  <Prefix/>
  <Marker/>
  <MaxKeys>1000</MaxKeys>
  <IsTruncated>false</IsTruncated>
  <Contents>
    <Key>employee_names.txt</Key>
    <LastModified>2019-12-14T15:53:25.000Z</LastModified>
    <ETag>"e8d2d18588378e0ee0b27fa1b125ad58"</ETag>
    <Size>7</Size>
    <StorageClass>STANDARD</StorageClass>
  </Contents>
  <Contents>
    <Key>test.txt</Key>
    <LastModified>2021-06-25T06:02:36.000Z</LastModified>
    <ETag>"098f6bcd4621d373cade4e832627b4f6"</ETag>
    <Size>4</Size>
    <Owner>
      <ID>65a011a29cdf8ec533ec3d1ccaae921c</ID>
    </Owner>
    <StorageClass>STANDARD</StorageClass>
  </Contents>
</ListBucketResult>
```

**Answer**: `employee_names.txt`
## What is in the file?
```bash
$ curl -s advent-bucket-one.s3.amazonaws.com/employee_names.txt
mcchef
```

**Answer**: `mcchef`
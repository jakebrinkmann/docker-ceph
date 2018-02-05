# Ceph playground

```bash
python ceph_buckets.py http://localhost:7480/ /path/to/aws/creds.ini "bucket-name"
[
    {
        "LastModified": "2018-02-05 15:27:13.181000+00:00",
        "ETag": "\"918dd80202643a758d1b16733e5ed7f7-43\"",
        "StorageClass": "STANDARD",
        "Key": "filename.tar.gz",
        "Owner": {
            "DisplayName": "DEVELOPER NAME",
            "ID": "username"
        },
        "Size": 352614672
    }
]
```

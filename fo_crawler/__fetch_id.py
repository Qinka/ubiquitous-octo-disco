# Fetch the video ide in the page

from urllib import request
import re


pattern1 = r'"videoCenterId"\,[ \t\n\x0B\f\r]*"[0-9a-f]+"'
pattern2 = r'guid[ \t\n\x0B\f\r]*=[ \t\n\x0B\f\r]"[0-9a-f]+"'



def fetch_id (url):
    req = request.Request(url,
                          data=None,
                          headers={
                              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
                          }
    )
    with request.urlopen(req) as f:
        text = f.read().decode()
        items = re.findall(pattern1,text)
        id = None
        if len(items) == 0:
            items = re.findall(pattern2,text)
            id = items[0].split('"')[1]
        else:
            id = items[0].split('"')[1]
        print(id)
        return id

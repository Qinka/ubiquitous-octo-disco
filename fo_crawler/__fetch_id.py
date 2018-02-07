# Fetch the video ide in the page

from urllib import request
import re


pattern = r'"videoCenterId"\,"[0-9a-f]+"'


def fetch_id (url):
    req = request.Request(url,
                          data=None,
                          headers={
                              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
                          }
    )
    with request.urlopen(req) as f:
        bytes = f.read()
        id =  re.findall(pattern,bytes.decode())[0].split(',')[1].split('"')[1]
        print(id)
        return id

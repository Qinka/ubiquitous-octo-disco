# Fetch info via a id

from urllib import request
import json

def fetch_info(id):
    req = request.Request('http://vdn.apps.cntv.cn/api/getHttpVideoInfo.do?pid='+id,
                          data=None,
                          headers={
                              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
                          }
    )
    with request.urlopen(req) as f:
        data = f.read()
        return json.loads(data.decode('utf-8'))

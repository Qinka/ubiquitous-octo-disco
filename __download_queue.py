# Dowload queue

import threading
import queue
from urllib import request
import os
import sys
from urllib.parse import (
    urlparse, urlsplit, urljoin, unwrap, quote, unquote,
    splittype, splithost, splitport, splituser, splitpasswd,
    splitattr, splitquery, splitvalue, splittag, to_bytes,
    unquote_to_bytes, urlunparse)
import contextlib
import tempfile
import urllib.error

__is_init = False

__que = None
__t = None

def init_queue(maxsize):
    global __is_init
    global __que
    global __t
    if __is_init :
        print('Launched')
        return None
    else:
        __que = queue.Queue(maxsize=maxsize)
        __t = threading.Thread(target=download_worker, name="Download Worker")
        __is_init = True
        __t.start()
        return (lambda:__t.join())

def download_worker():
    global __is_init
    while __is_init:
        url = __que.get()
        print("\n" + url)
        fn = os.path.basename(url)
        request.urlretrieve(url,fn,lambda bn,bs,ts:display_processing(fn,bn,bs,ts))

def put_queue(items):
    global __is_init
    if __is_init:
        for item in items:
            __que.put(item)
    else:
        raise ValueError('init first')

def stop_worker():
    __is_init = False
    __t.join()

def display_processing(filename,blocknum,blocksize,totalsize):
    sys.stderr.write("%s: total=%u,downloaded=%u=%u*%u\r" % (filename, totalsize, blocknum * blocksize,  blocknum,  blocksize))
    sys.stderr.flush()


## rewrite urlretrieve
def urlretrieve(url, filename=None, reporthook=None, data=None):
    url_type, path = splittype(url)
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
    req = request.Request(url,data=data,headers=headers)
    with contextlib.closing(request.urlopen(req)) as _fp:
        headers = _fp.info()
        if url_type == "file" and not filename:
            return os.path.normpath(path), headers
        # Handle temporary file setup.
        if filename:
            tfp = open(filename, 'wb')
        else:
            tfp = tempfile.NamedTemporaryFile(delete=False)
            filename = tfp.name
            request._url_tempfiles.append(filename)
        with tfp:
            result = filename, headers
            bs = 1024*8
            size = -1
            read = 0
            blocknum = 0
            if "content-length" in headers:
                size = int(headers["Content-Length"])
            if reporthook:
                reporthook(blocknum, bs, size)
            while True:
                block = _fp.read(bs)
                if not block:
                    break
                read += len(block)
                tfp.write(block)
                blocknum += 1
                if reporthook:
                    reporthook(blocknum, bs, size)
    if size >= 0 and read < size:
        raise urllib.error.ContentTooShortError(
            "retrieval incomplete: got only %i out of %i bytes"
            % (read, size), result)
    return result

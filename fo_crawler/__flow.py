# Main flow

from .__fetch_id import *
from .__fetch_info import *
from .__fetch_urls import *
from .__download_queue import *
from .__saver import *
import logging
from urllib.error import URLError, HTTPError


def main(saverfp,loggerfp,urllist):
    lines = None

    logger = logging.getLogger('disco')
    formatter = logging.Formatter('%(name)-12s %(asctime)s %(levelname)-8s %(message)s', '%a, %d %b %Y %H:%M:%S',)
    file_handler = logging.FileHandler(loggerfp)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler(sys.stderr)
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    print('Logger start!')

    with open(urllist, 'r') as f:
        lines = f.readlines()

    ibeg = load_saver(saverfp)

    for iid in range(ibeg,len(lines)):
        try:
            print('line %d' % iid)

            url = lines[iid].split('\n')[0]
            print('url %s' % url)

            vid = fetch_id(url)
            print('id %s' % vid)

            info = fetch_info(vid)

            items = fetch_video_urls(info)
            for vurl in items:
                download_video(vurl)
                print('downloaded %s' % vurl)

        except Exception as e:
            print('error %s' % url)
            print(e)
        finally:
            save_saver(saverfp,iid+1)

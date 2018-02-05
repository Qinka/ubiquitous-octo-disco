# Main flow

from .__fetch_id import *
from .__fetch_info import *
from .__fetch_urls import *
from .__download_queue import *
from .__saver import *
import logging

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

    def flush():
        file_handler.flush()
        stream_handler.flush()

    logger.info('Logger start!')
    flush()

    with open(urllist, 'r') as f:
        lines = f.readlines()

    ibeg = load_saver(saverfp)

    for iid in range(ibeg,len(lines)):
        logger.info('line %d' % iid)
        flush()

        url = lines[iid].split('\n')[0]
        logger.info('url %s' % url)
        flush()

        vid = fetch_id(url)
        logger.info('id %s' % vid)
        flush()

        info = fetch_info(vid)

        items = fetch_video_urls(info)
        for vurl in items:
            download_video(vurl)
            logger.info('downloaded %s' % vurl)
            flush()

        save_saver(saverfp,iid+1)
    stop_worker()
    logger.shutdown()

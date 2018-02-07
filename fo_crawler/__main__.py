import argparse
from .__flow import main

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="focus on")
    parser.add_argument('--saver', '-s', action='store', help='saver file', default='fo.saver',dest='saverfp')
    parser.add_argument('--logger', '-l', action='store', help='logger file', default='out.log', dest='loggerfp')
    parser.add_argument('--url-list', '-u',action='store', help='url list',default='url.list', dest='urllist' )
    args = parser.parse_args()
    main(args.saverfp,args.loggerfp,args.urllist)

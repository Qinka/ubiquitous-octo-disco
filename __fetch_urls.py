# Fetch urls


def fetch_video_urls(j):
    rt = []
    for i in j['video']['chapters4']:
        rt.append(i['url'])
    return rt

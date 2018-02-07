# Fetch urls


def fetch_video_urls(j):
    rt = []
    video = j.get('video')
    items = video.get('chapters4',video.get('chapters3',video.get('chapters2',video.get('chapters',video.get('lowChapters',[])))))
    for i in items:
        rt.append(i['url'])
    return rt

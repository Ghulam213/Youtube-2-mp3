import youtube_dl


def youtubeConverter(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'media/Youtube2Audio/download/%(title)s.%(ext)s',
        'download_archive': 'media/Youtube2Audio/downloaded_songs.txt',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],

    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.cache.remove()
        info_dict = ydl.extract_info(url, download=False)
        ydl.prepare_filename(info_dict)
        ydl.download([url])
        return info_dict["title"]


import yt_dlp
import re
import os

def download_thumbnail(link):
    ydl_opts = {
        'skip_download': True,
        'writethumbnail': True,
        'convertthumbnails': 'png',
        'outtmpl': '%(title)s_%(id)s.%(ext)s',
	    'postprocessors': [{
            'key': 'FFmpegThumbnailsConvertor',
            'format': 'png'
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Fetching reel thumbnail information...")
            ydl.download([link])
            print("Download complete!")
            print(f"Files should be visible here: {os.getcwd()}")
            
    except Exception:
        print("Error downloading reel thumbnail: Please try again/later or Update to the latest version of Instagram-Downloader")
        print("Click here to get the latest version: https://github.com/shreyashish2211/Instagram-Downloader/releases")

def main_menu():
    while True:
        print("\n============================== Instagram Thumbnail Downloader ==============================")
        print("                     =========== by Shreyashish Mitra ===========                             ")
        link = input("Enter the link to download (or type 'exit'): ").strip()

        if re.match(r'^https?://', link):
            print("Starting downloading...")
            download_thumbnail(link)

        elif link == 'exit':
            print('Exiting Programme Bye bye...')
            break
        
        else:
            print("Invalid input. Please enter a valid YouTube link.")

if __name__ == "__main__":
    main_menu()

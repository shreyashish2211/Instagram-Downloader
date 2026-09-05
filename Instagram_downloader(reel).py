import yt_dlp
import re
import os

def download_reel(link):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s_%(id)s.%(ext)s',
        'postprocessors': [{
                'key': 'FFmpegMetadata',  # Key to activate metadata embedding
            },
            {
                'key': 'EmbedThumbnail',  # Optional: Also embed the video thumbnail
                'already_have_thumbnail': False # Let yt-dlp manage the thumbnail file
            }],
        'writethumbnail': True,
        'windowsfilenames': True,
        'merge_output_format': 'mp4',
        'sanitize_filenames': True,
        'cookiefile': 'instagram.com_cookies.txt',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Fetching reel information...")
            ydl.download([link])
            print("Download complete!")
            print(f"Files should be visible here: {os.getcwd()}")
        
    except Exception:
        print("Error downloading reel: Please try again/later or Update to the latest version of Instagram Downloader")
        print("Click here to get the latest version: https://github.com/shreyashish2211/Instagram-Downloader/releases")

def main_menu():
    while True:
        print("\n============================== Instagram Reel Downloader ==============================")
        print("                     =========== by Shreyashish Mitra ===========                        ")
        link = input("Enter the link to download (or type 'exit'): ").strip()

        if re.match(r'^https?://', link):
            print(f"Starting download...")
            download_reel(link)

        elif link == 'exit':
            print('Exiting Programme Bye bye...')
            break

        else:
            print("Invalid input. Please enter a valid link.")
if __name__ == "__main__":
    main_menu()

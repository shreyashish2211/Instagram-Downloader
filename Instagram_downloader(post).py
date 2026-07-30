import instaloader
import re
import os
import time

def download_post(link):
    custom_pattern = "Post by {owner_username}__{shortcode}"

    L = instaloader.Instaloader(
        filename_pattern=custom_pattern,
        download_pictures=True,
        download_videos=False,
        download_video_thumbnails=False,
        dirname_pattern=".",
        save_metadata=False,
        post_metadata_txt_pattern="",
        compress_json=False,
    )
    
    try:   
        match = re.search(r"/p/([^/]+)/", link)
        if not match:
            raise ValueError("Invalid Instagram post URL")

        shortcode = match.group(1)
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        L.download_post(post, target='.')
        print("Post downloaded successfully.")
        print(f"Files should be visible here: {os.getcwd()}")

    except instaloader.exceptions.QueryReturnedBadRequestException:
        print("Private post: you must follow the account.")

    except instaloader.exceptions.LoginRequiredException:
        print("Login required or session expired.")

    except Exception as e:
        print("Unexpected error:", e)
        
def main_menu():
    while True:
        print("\n============================== Instagram Post Downloader ==============================")
        print("                     =========== by Shreyashish Mitra ===========                        ")
        link = input("Enter the link to download (or type 'exit'): ").strip()

        if re.match(r'^https?://', link):
            print(f"Starting download...")
            print(f"Fetching post information...")
            time.sleep(1)
            print("Sleeping 5.00 seconds as required by the site")
            time.sleep(5)
            download_post(link)

        elif link == 'exit':
            print('Exiting Programme Bye bye...')
            break

        else:
            print("Invalid input. Please enter a valid link.")

if __name__ == "__main__":
    main_menu()

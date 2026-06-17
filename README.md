# __Instagram Downloader__

Have you ever thought to download insta reels or post but insta doesn't let you do that though sometimes insta does provides you to download feature for some reels with watermark of the original creator who had posted the reel, and is restricted to your phone. But now you can freely download any instagram content of your favourite content creator. This is only limited to public account **so make sure that the reel, story or post is from a public account not from a private account**, otherwise it will throw an error. 

---

## __General Instructions__

1. Copy the URL link of the Reel/Post you want to download.
2. Paste the URL link into "Enter the link to download." when you start the app.
3. Make sure that the reel/post is from a public account not private account.
5. Even Downloads Stories/Highlights **(Make sure to use the right application to download it)**.
4. Choose the appropriate downloader option:
   - `Instagram_downloader(post):` Downloads only Pictures uploaded by the admin.
   - `Instagram_downloader(thumbnail):` Downloads only Thumbnails from the reel in JPG format.
   - `Instagram_downloader(reel):` Downloads Reel and stories.
5. Type exit when you are done and hit enter.
6. **Linux Usage:** If using the compiled binary, navigate to the directory in your terminal and run the program using ./app_name.

---

## __Requirements__

* **Compatibility:** __This works in Windows i.e Windows 10 & 11 and Linux (I can't make macOS build).__
* __You have to install FFmpeg to run the app; otherwise, the downloader wouldn't work__
* __Installation via Windows, open Terminal or PowerShell(preferably as Administrator) and run this command:__
  ```
  winget install FFmpeg
  ```
  ```
  winget install Nodejs
  ```
* __Installation via Linux, open Terminal and run these command:__

   - For Fedora, CentOS, and RHEL linux distros
     ```
     sudo dnf swap 'ffmpeg-free' 'ffmpeg' --allowerasing
     ```
     ```
     sudo dnf install nodejs
     ```
   - For Ubuntu, Debian, Mint, and Kali Linux distros
     ```
     sudo apt install ffmpeg
     ```
     ```
     sudo apt install nodejs npm 
     ```
   - For other Linux distros/macOS search in the internet 
> [!Note]
> The program may show a security warning the first time you run the compiled app __*on Windows*__. If this happens, click on
>- **More info -> Run anyway.**

---

## __Tips__

- Running PowerShell or Terminal as Administrator is recommended, though not always required.
- Ensure your internet connection is stable and good for faster and more reliable downloads.
- If anytime the downloader fails randomly try to download it again, then also if it fails please make sure to download the latest build which I would be providing in  Github.

---

## Star History

<a href="https://www.star-history.com/?repos=Instagram-Downloader%2FInstagram-Downloader&type=date&logscale=&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=Instagram-Downloader/Instagram-Downloader&type=date&theme=dark&logscale&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=Instagram-Downloader/Instagram-Downloader&type=date&logscale&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/image?repos=Instagram-Downloader/Instagram-Downloader&type=date&logscale&legend=top-left" />
 </picture>
</a>

Thank you for checking out this project!

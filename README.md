# __Instagram-Downloader__

Have you ever tried to download Insta reels or posts, but Insta doesn't let you? Sometimes Insta does provide you with a download feature for some reels with a watermark of the original creator who posted the reel, and it is restricted to your phone. But now you can freely download any Instagram content of your favourite content creator. This is only limited to public accounts **so make sure that the reel, story or post is from a public account, not from a private account**, otherwise it will throw an error. 

---

## __General Instructions__

1. Copy the URL link of the Reel/Post you want to download.
2. Paste the URL link into "Enter the link to download." when you start the app.
3. Make sure that the reel/post is from a public account, not a private account.
5. Even Downloads Stories/Highlights **(Make sure to use the right application to download it)**.
4. Choose the appropriate downloader option:
   - `Instagram_downloader(post):` Downloads only Pictures uploaded by the admin.
   - `Instagram_downloader(thumbnail):` Downloads only thumbnails from the reel in JPG format.
   - `Instagram_downloader(reel):` Downloads reels and stories.
5. Type exit when you are done and hit enter.
6. **Linux Usage:** If using the compiled binary, navigate to the directory in your terminal and run the program using ./app_name.

---

## __Requirements__

* **Compatibility:** __This works in Windows, i.e Windows 10 & 11, and Linux (I can't make macOS build).__
* __If you use the source code instead of the compiled app (*You have to Install FFmpeg, if you are using the compiled app*), you must install the following:__
    * `yt-dlp` library and `yt-dlp-ejs` dependency.
    * `FFmpeg`
    * `Node.js`
* __Installation via Windows, open Terminal or PowerShell(preferably as Administrator) and run this command:__
  ```
  winget install FFmpeg
  ```
  ```
  winget install Nodejs
  ```
* __Installation via Linux: open Terminal and run these commands:__

   - For Fedora, CentOS, and RHEL Linux distros
     ```
     sudo dnf install ffmpeg --allowerasing
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
   - For other Linux distros/macOS, search on the internet 

> [!Note]
> The program may show a security warning the first time you run the compiled app __*on Windows*__. If this happens, click on
>* **More info -> Run anyway.**
---

## __Tips__

- Use the source code recommended.
- Running PowerShell or Terminal as Administrator is recommended, though not always required.
- Ensure your internet connection is stable and good for faster and more reliable downloads.
- **If the downloader fails randomly at any time, try downloading it again and again; then also, if it fails, please make sure to download the latest build, which I will be providing on GitHub.**

---

## License

This project's source code is licensed under the GPLv3 license.

<div align="right">
<table><td>
<a href="#start-of-content">👆 Scroll to top</a>
</td></table>
</div>

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

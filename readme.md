# Youtube Auto Viewer

## Install

### Windows

```bash
pip install -r requirements.txt
```


### Linux (Ubuntu)

```bash
sudo apt install pip
sudo pip3 install -r requirements.txt

## Chrome installation
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
sudo apt update
sudo apt install google-chrome-stable

## Chrome driver installation
wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/chromedriver
```

## Usage

1. Add video urls to `video_urls` array in `youtube-viewer.py` file.
1. Customize the view time on `view_time` variable in `youtube-viewer.py` file.
1. Run the script:

```bash
python3 youtube-viewer.py
```

## Disclaimer

This script is for educational purposes only. I am not responsible for any damage caused by this script. Use at your own risk.

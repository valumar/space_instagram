# Space Instagram

Program for fetching images from [SpaceX API](https://github.com/r-spacex/SpaceX-API) and [Hubble API](http://hubblesite.org/api/documentation) and uploading them to Instagram.

### How to install

For proper use you have to get Instagram account.
After that rename the file `.env-example` to `.env` and paste your Instagram credentials.

Python3 should be already installed. 
It is strictly recommended that you use [virtual environment](https://docs.python.org/3/library/venv.html) for project isolation. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:

```
pip install -r requirements.txt
```

##### Fetching images from SpaceX API
Run script `fetch_spacex.py`

##### Fetching images from Hubble API
Run script `fetch_hubble.py`

##### Publishing images to Instagram
Run script `instapub.py`

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
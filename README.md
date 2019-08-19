# drmvid
Django Restful web application for Video uploading and transcoding.

## Requirements
* Python3
* ffmpeg
* redis-server

## Installation & Deployment Guide -

### 1. Install global dependencies

     sudo apt-get install virtualenv python3-pip git ffmpeg redis-server

### 2. Upgrade `pip` and `setuptools` that are bundled with the OS to the latest stable versions.

     sudo -H pip install pip -U

     sudo -H pip install setuptools -U

### 3. Clone the drmvid from github to your preferred directory.

    git clone https://github.com/sauravmahuri2007/drmvid.git

    cd drmvid

### 4. Create virtualenv and install project dependencies

    virtualenv --python=python3 venv

    source venv/bin/activate

    pip install -r requirements.txt

### 5. Run the redis-server

    redis-server
    
### 6. Create superuser

    python manage.py createsuperuser
    
### 7. Run the migrations

    python manage.py migrate
    
## Running the application

  Two terminal windows/tabs will be required to run the application
    
### 1. In 1st terminal run the app using the default lightweight Django web server

    python manage.py runserver
    
### 2. In 2nd terminal run the Django Redis Queue worker

    python manage.py rqworker


The app should have started running at http://127.0.0.1:8000

## Usage

### Django Rest API to get the JWT based authentication token.
  POST '/api/token' with the username and password as POST body to get the `access` and `refresh` token. Use `access` token in Authentication header `Bearer <access_token>` for API calls and when `access` token expires (1h configurable, check `settings.py`) then use `refresh` token as POST body {'refresh': <refresh_token>} and the API '/api/token/refresh' to generate get the `access` token once again. TTL of `refresh` token is 24h (configurable, check `settings.py`)
    
### Django rest API to GET/POST the video and transcode the video

  '/api/vid' can be used to upload the videos with POST method which can again be used to GET the list of all uploaded and trascoded videos.
    
### Using DRF UI to GET/POST the videos (preferred for testing the functionality).

  visit http://127.0.0.1:8000/api/vid in a browser to use Django Rest Framework interactive UI to get the video list and upload a new video for transcoding. Login is required in order to access this URL which can be done using the login button on top-right header secion of the page.

Note:
As soon as the video gets uploaded Django's `post_save` signal will call a django_rq task which will start the video encoding as a backend process. Check `settings.py` with constants starting with VID* for more details about the confirations. All transcoded video details will be available as part of the GET response of http://127.0.0.1:8000/api/vid 


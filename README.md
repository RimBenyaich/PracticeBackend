# Backend Practice

This is a REST microservice following the [`Gemography Backend Challenge`](https://github.com/gemography/backend-coding-challenge) using the [FastAPI](https://fastapi.tiangolo.com) webframework.

## Getting Started
After cloning the repository, run the command to activate the virtual environment set for the application:
```bash
source venv/bin/activate
```

After activating the VE, you will need to install the requirements present in our requirement.txt file: 
```bash
pip3 install -r requirements.txt
```

## Run the App
```bash
# You can access the app at: http://127.0.0.1:8000/repositories
uvicorn app.main:app --reload
```

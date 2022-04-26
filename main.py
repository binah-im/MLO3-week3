from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"message": "Hello AWS World!"}


#Bonus
#import logging
#from logging.config import dictConfig
#from log_config import log_config               # my local file
#Bonus dictConfig(log_config)
#Bonus logger = logging.getLogger("my-project-logger") # should be this name unless you change it in log_config.py
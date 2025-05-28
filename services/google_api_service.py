import os
import requests
from flask import current_app

class GoogleApiService:
    def __init__(self):
        self.api_key = current_app.config.get('GOOGLE_API_KEY')
    
    
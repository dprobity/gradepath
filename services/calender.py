# services/calendar.py
import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

# SCOPES: What we ask the student for permission to do
SCOPES = ['https://www.googleapis.com/auth/calendar']

# PATHS: Configured via .env (Secure!)
CREDENTIALS_FILE = os.getenv("GOOGLE_CREDENTIALS_PATH", "credentials.json") # YOUR App Key
TOKEN_FILE = os.getenv("GOOGLE_TOKEN_PATH", "token.json")     # STUDENT'S Saved Session

class CalendarService:
    def __init__(self):
        self.service = None
        self.is_connected = False
        self._load_existing_token()

    def _load_existing_token(self):
        """Try to load a saved student token without triggering a popup."""
        creds = None
        if os.path.exists(TOKEN_FILE):
            try:
                creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
                if creds and creds.valid:
                    self.service = build('calendar', 'v3', credentials=creds)
                    self.is_connected = True
            except Exception:
                self.is_connected = False

    def connect(self):
        """
        Triggers the 'SSO' Popup. 
        Call this ONLY when the user clicks 'Connect' in the UI.
        """
        if self.is_connected: return True

        if not os.path.exists(CREDENTIALS_FILE):
            raise FileNotFoundError(f"Missing App Credentials at {CREDENTIALS_FILE}")

        # This triggers the browser popup (SSO Simulation)
        flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
        creds = flow.run_local_server(port=0)

        # Save the student's token locally
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
        
        self.service = build('calendar', 'v3', credentials=creds)
        self.is_connected = True
        return True

    def add_event(self, title: str, start_iso: str):
        if not self.is_connected:
            return {"error": "Calendar not connected"}
        
        # ... (Rest of your add_event logic) ...
        # [Use the code from previous step]

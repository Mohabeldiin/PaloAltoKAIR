import logging
import os

import gspread
from google.oauth2.service_account import Credentials

logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.DEBUG,
        filename="status.log",
        filemode="w")
log = logging.getLogger("KAIR")

privet_key_test = os.environ.get("PRIVATE_KEY")


credential ={
  "type": "service_account",
  "project_id": "paloaltokair",
  "private_key_id": os.environ.get("PRIVATE_KEY_ID"),
  "private_key":privet_key_test,
  "client_email": os.environ.get("CLIENT_EMAIL"),
  "client_id": os.environ.get("CLIENT_ID"),
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/python-api%40paloaltokair.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

sheet_id = os.environ.get("SHEET_ID")

client = gspread.authorize(Credentials.from_service_account_info(credential,
    scopes=["https://www.googleapis.com/auth/spreadsheets"]
    ))

workbook = client.open_by_key(sheet_id)

vallist = workbook.sheet1.row_values(1)

log.debug(vallist)
from dotenv import load_dotenv
import os

"""Loading Environment Variables"""

load_dotenv()

PASSWORD = os.getenv("PASSWORD")
EMAIL_ADDR = os.getenv("EMAIL_ADDR")
API_KEY = os.getenv("API_KEY")

url = f"https://www.d3stinn3.net/api/?api_key={API_KEY}"

login_info = {
    "email": EMAIL_ADDR,
    "password": PASSWORD,
    "api_key": API_KEY
}

print(login_info)
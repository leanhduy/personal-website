from dotenv import load_dotenv
import os

load_dotenv()

PROJECT_TYPES = [("personal", "Personal"), ("commercial", "Commercial")]
ACHIEVEMENT_TYPES = (("award", "Award"), ("certification", "Certification"))
# API URLs
GET_AWARDS_URL = f"{os.getenv('API_BASE_URL')}/api/awards/"

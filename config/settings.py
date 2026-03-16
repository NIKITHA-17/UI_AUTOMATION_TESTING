import os

BASE_URL = os.getenv("BASE_URL", "https://react-frontend-api-testing.vercel.app")
GRID_URL = os.getenv("GRID_URL", "http://localhost:4444/wd/hub")
BROWSER = os.getenv("BROWSER", "chrome").lower()
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
RUN_MODE = os.getenv("RUN_MODE", "local").lower()
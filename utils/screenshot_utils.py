from pathlib import Path
from datetime import datetime

def save_screenshot(driver, name="failure"):
    screenshots_dir = Path("reports") / "screenshots"
    screenshots_dir.mkdir(parents=True, exist_ok=True)

    file_name = f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    file_path = screenshots_dir / file_name
    driver.save_screenshot(str(file_path))
    return str(file_path)
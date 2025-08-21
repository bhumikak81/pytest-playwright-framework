import os

def take_screenshot(page, name: str = 'screenshot.png'):
    reports_dir = os.path.join(os.getcwd(), "reports")
    os.makedirs(reports_dir, exist_ok=True)
    path = os.path.join(reports_dir, name)
    page.screenshot(path=path)
    return path

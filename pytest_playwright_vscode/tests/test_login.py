import yaml
from pages.login_page import LoginPage

def load_config():
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)

def test_valid_login(page, pytestconfig):
    cfg = load_config()
    # Use built-in pytest-playwright option for base URL
    base_url = pytestconfig.getoption("base_url") or cfg["base_url"]

    login = LoginPage(page)
    login.open(base_url)
    login.login(cfg["username"], cfg["password"])
    assert "You logged into a secure area!" in login.success_message()

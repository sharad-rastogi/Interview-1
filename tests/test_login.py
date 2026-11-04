
import pytest
from config import USERNAME, PASSWORD


@pytest.mark.no_auth
@pytest.mark.smoke
def test_valid_login(login_page, app_url):
    login_page.open(app_url)
    login_page.login(USERNAME, PASSWORD)
    assert "inventory.html" in login_page.page.url


@pytest.mark.no_auth
@pytest.mark.parametrize(
    "username,password,error",
    [
        ("locked_out_user", PASSWORD, "Sorry, this user has been locked out."),
        ("", PASSWORD, "Username is required"),
        (USERNAME, "", "Password is required"),
        ("", "", "Username is required")
    ]
)
def test_negative_login(login_page, app_url, username, password, error):
    login_page.open(app_url)
    login_page.login(username, password)
    login_page.verify_error(error)

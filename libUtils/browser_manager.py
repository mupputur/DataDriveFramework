import subprocess
import requests
import os
import zipfile
import platform
from bs4 import BeautifulSoup
import re


class BrowserManager:
    def __init__(self):
        self.driver_path = "..//dependencies//browser-driver"

    def download_zip_file(self, download_url):
        """Download the browser driver zip file."""
        try:
            response = requests.get(download_url, stream=True)
            if response.status_code == 200:
                zip_path = "browser_driver.zip"

                with open(zip_path, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)

                print(f"Downloaded browser driver zip: {zip_path}")
                return zip_path
            else:
                raise Exception(f"Failed to download Browser Driver from {download_url}")
        except Exception as e:
            print(f"Error downloading BrowserDriver: {e}")
            return None

    def extract_zipfile(self, zip_path):
        """Extract the browser driver from the downloaded zip file."""
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(self.driver_path)
                print(f"Extracted Browser Driver to: {self.driver_path}")

            os.remove(zip_path)
            print(f"BrowserDriver is ready at {self.driver_path}")
            return True
        except Exception as e:
            print(f"Error extracting BrowserDriver: {e}")
            return False

class ChromeBrowserManager(BrowserManager):60
    def __init__(self):
        super().__init__()
        self.reg_path = r'reg query "HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon" /v version'

    def get_chrome_version(self):
        """Get the Chrome browser version installed on Windows."""
        try:
            output = subprocess.check_output(self.reg_path, shell=True, encoding='utf-8')
            version = output.split()[-1]
            print(f"Chrome Version: {version}")
            return version
        except Exception as e:
            print(f"Failed to read Chrome browser version from path: {self.reg_path}")
            raise Exception(f"Failed to get Chrome browser version. Error: {e}")

    def get_driver_url(self, chrome_version):
        """Get the URL for the ChromeDriver for the given Chrome version."""
        try:
            architecture = 'win64' if platform.architecture()[0] == '64bit' else 'win32'
            print(architecture)
            download_url = f"https://storage.googleapis.com/chrome-for-testing-public/{chrome_version}/{architecture}/chromedriver-{architecture}.zip"
            print(f"Chrome Driver Download URL: {download_url}")

            response = requests.head(download_url)
            if response.status_code != 200:
                raise Exception(f"Failed to get ChromeDriver for Chrome {chrome_version}.")
            return download_url
        except Exception as e:
            print(f"Error getting ChromeDriver download URL: {e}")
            return None

class FirefoxBrowserManager(BrowserManager):
    def __init__(self):
        super().__init__()
        self.reg_path = r'reg query "HKEY_LOCAL_MACHINE\SOFTWARE\mozilla.org\Mozilla" /v CurrentVersion'
        self.base_url = "https://github.com/mozilla/geckodriver/releases"

    def get_firefox_version(self):
        """Get the Firefox browser version installed on Windows."""
        try:
            output = subprocess.check_output(self.reg_path, shell=True, encoding='utf-8')
            version = output.split()[-1]
            print(f"Firefox Version: {version}")
            return version
        except Exception as e:
            print(f"Failed to read Firefox browser version from path: {self.reg_path}")
            raise Exception(f"Failed to get Firefox browser version. Error: {e}")

    def get_firefox_url(self, firefox_version):
        """Get the URL for the GeckoDriver for the given Firefox version."""
        architecture = 'win64' if platform.architecture()[0] == '64bit' else 'win32'
        architecture_sys = architecture[:-2]
        architecture_ver = architecture[-2:]

        response = requests.get(self.base_url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch GeckoDriver releases: {response.status_code}")

        # Parse the releases page to find the latest compatible version
        soup = BeautifulSoup(response.text, "html.parser")

        for link in soup.find_all("a", href=True):
            if "tag" in link["href"]:
                tag = link["href"].split("/")[-1]
                if re.match(r"v\d+\.\d+\.\d+", tag):
                    if architecture == "win64":
                        download_url = f"https://github.com/mozilla/geckodriver/releases/download/{tag}/geckodriver-{tag}-{architecture_sys}-aarch{architecture_ver}.zip"
                    elif architecture == "win32":
                        download_url = f"https://github.com/mozilla/geckodriver/releases/download/{tag}/geckodriver-{tag}-{architecture_sys}.zip"
                    return download_url

        raise Exception("GeckoDriver download URL not found.")

if __name__ == "__main__":
    chrome_manager = ChromeBrowserManager()
    # Get Chrome version
    chrome_version = chrome_manager.get_chrome_version()
    if not chrome_version:
        print("Failed to get Chrome version.")
        exit(1)

    # Get ChromeDriver download URL
    chrome_download_url = chrome_manager.get_driver_url(chrome_version)
    if not chrome_download_url:
        print("Failed to get ChromeDriver download URL.")
        exit(1)

    # Download ChromeDriver zip file
    chrome_zip_path = chrome_manager.download_zip_file(chrome_download_url)
    if chrome_zip_path:
        chrome_success = chrome_manager.extract_zipfile(chrome_zip_path)
        if chrome_success:
            print("ChromeDriver is set up successfully!")
        else:
            print("Failed to extract ChromeDriver.")
    else:
        print("Failed to download ChromeDriver.")

    # Firefox Browser Setup
    firefox_manager = FirefoxBrowserManager()

    # Get Firefox version
    firefox_version = firefox_manager.get_firefox_version()
    if not firefox_version:
        print("Failed to get Firefox version.")
        exit(1)

    # Get GeckoDriver download URL
    firefox_download_url = firefox_manager.get_firefox_url(firefox_version)
    if not firefox_download_url:
        print("Failed to get GeckoDriver download URL.")
        exit(1)

    # Download GeckoDriver zip file
    firefox_zip_path = firefox_manager.download_zip_file(firefox_download_url)
    if firefox_zip_path:
        firefox_success = firefox_manager.extract_zipfile(firefox_zip_path)
        if firefox_success:
            print("GeckoDriver is set up successfully!")
        else:
            print("Failed to extract GeckoDriver.")
    else:
        print("Failed to download GeckoDriver.")

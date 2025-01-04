from bs4 import BeautifulSoup
import re
import subprocess
import platform
import requests
import zipfile
import os

class BrowserManager:

    def __init__(self):
        self.driver_path = "..//dependencies//firefox-driver"
        self.reg_path = r'reg query "HKEY_LOCAL_MACHINE\SOFTWARE\mozilla.org\Mozilla" /v CurrentVersion'
        self.base_url = "https://github.com/mozilla/geckodriver/releases"

    def get_firefox_version(self):   #Get the firefox browser version installed on Windows.
        try:
            # Check Firefox version in HKEY_LOCAL_MACHINE
            output = subprocess.check_output(self.reg_path, shell=True, encoding='utf-8')
            version = output.split()[-1]
            print(f"Firefox Version: {version}")
            return version
        except Exception as e:
            print(f"Failed to read chrome browser version from path: {e}")
            raise Exception(f"Failed to get firefox browser version. Error: {e}")

    def get_firefox_url(self, firefox_version):
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

    def download_zip_file(self, download_url):
        try:
            response = requests.get(download_url, stream=True)
            if response.status_code == 200:
                zip_path = "greckodriver.zip"

                with open(zip_path, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=1024):
                        file.write(chunk)

                print(f"Downloaded ChromeDriver zip: {zip_path}")
                return zip_path
            else:
                raise Exception(f"Failed to download Firefox Driver from {download_url}")
        except Exception as e:
            print(f"Error downloading FirefoxDriver: {e}")
            return None

    def extract_zipfile(self, zip_path):
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(self.driver_path)
                print(f"Extracted Firfox Driver to: {self.driver_path}")

            os.remove(zip_path)
            print(f"ChromeDriver is ready at {self.driver_path}\\chromedriver.exe")
            return True

        except Exception as e:
            print(f"Error extracting ChromeDriver: {e}")
            return False



if __name__ == "__main__":
    manager = BrowserManager()

    # Get Firefox version
    firefox_version = manager.get_firefox_version()
    if not firefox_version:
        print("Failed to get Firefox version.")
        exit(1)

    # Get GeckoDriver download URL
    download_url = manager.get_firefox_url(firefox_version)
    if not download_url:
        print("Failed to get GeckoDriver download URL.")
        exit(1)

    # Download firefoxDriver zip file
    zip_path = manager.download_zip_file(download_url)
    if zip_path:
        success = manager.extract_zipfile(zip_path)
        if success:
            print("ChromeDriver is set up successfully!")
        else:
            print("Failed to extract ChromeDriver.")
    else:
        print("Failed to download ChromeDriver.")



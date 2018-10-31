import os
driver_path = os.getcwd() + "/bin"

os.environ["PATH"] += os.pathsep + driver_path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1280x1696')
chrome_options.add_argument('--user-data-dir=/tmp/user-data')
chrome_options.add_argument('--hide-scrollbars')
chrome_options.add_argument('--enable-logging')
chrome_options.add_argument('--log-level=0')
chrome_options.add_argument('--v=99')
chrome_options.add_argument('--single-process')
chrome_options.add_argument('--data-path=/tmp/data-path')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--homedir=/tmp')
chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
chrome_options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
chrome_options.binary_location = driver_path + "/headless-chromium"


def lambda_handler(event, context):
    # TODO implement
    conv_url = "https://www.converto.io/?v="

    driver = webdriver.Chrome(chrome_options=chrome_options)

    yt_url = ""
    if 'url' in event.keys():
        yt_url = event['url']

    if "youtube" not in yt_url:
        return "Invalid URL: " + yt_url
    vid_id = yt_url.split("?v=")[1]

    driver.get(conv_url + vid_id)
    element = driver.find_element_by_class_name("convert-btn")
    element.click()
    page_data = driver.page_source
    driver.close()

    return page_data

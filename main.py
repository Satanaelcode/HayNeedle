import requests
import logging
import random
import json
from multiprocessing import Pool
from utils.valueutil import generate_ipv4
from utils.setup import setup

logging.basicConfig(filename='urls.log', level=logging.INFO, format='%(asctime)s | %(message)s')

logging.info(f"Init Setup..")
setup()
logging.info(f"STARTING SCAN")
try:
    with open("files.json", "r") as f:
        filenames = json.load(f)["files"]
except Exception as e:
    logging.error(f"Error: {e}")
    exit("COULD NOT READ FILES.JSON!")


def make_request(url):
    try:
        response = requests.get(url, timeout=50)
        if response.status_code == 200:
            logging.info(f"VALID » {url}")
            print(f"\033[32mGood request to {url}\033[0m")
        elif response.status_code == 404:
            logging.warning(f"NONE » {url}")
            print(f"\033[31mBad response from {url}\033[0m")
    except requests.exceptions.Timeout:
        logging.warning(f"TIMEOUT » {url}")
    except requests.exceptions.ConnectionError:
        logging.warning(f"BAD » {url}")

def generate_urls(filenames):
    urls = []
    for _ in range(30):  # Batch processing 30 URLs at a time
        ip = generate_ipv4()
        url = f"http://{ip}/{random.choice(filenames)}"
        urls.append(url)
    return urls


print("START SCAN..")
with Pool(processes=75) as pool:  # Create a pool of 20 worker processes
    while True:
        urls = generate_urls(filenames)
        pool.map(make_request, urls)
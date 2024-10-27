import os
from typing import Match

import requests
import picologging as logging
import random
import json
from multiprocessing import Pool

from setuptools.command.bdist_egg import can_scan

from utils.valueutil import generate_ipv4
from utils.setup import setup
import time

logging.basicConfig(filename=f'./logs/{time.time()}_{time.localtime().tm_mday}.{time.localtime().tm_mon}.{time.localtime().tm_year}', level=logging.INFO, format='%(message)s')


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
        response = requests.get(url, timeout=10)
        match response.status_code:
            case 200:
                if response.history:
                    logging.warning(f"BAD » {url}")
                    print(f"\033[31mBAD response from {url}\033[0m")
                    with open("./results/webpages.txt", "a") as file:
                        file.write(url+"\n")
                else:
                    logging.info(f"VALID » {url}")
                    print(f"\033[32mGood request to {url}\033[0m")
                    with open("./results/valid.txt", "a") as file:
                        file.write(url+"\n")
                    with open("./results/webpages.txt", "a") as file:
                        file.write(url+"\n")

            case 404:
                logging.warning(f"BAD » {url}")
                print(f"\033[31mBAD response from {url}\033[0m")
                with open("./results/webpages.txt", "a") as file:
                    file.write(url + "\n")

    except requests.exceptions.Timeout:
        logging.warning(f"TIMEOUT » {url}")
    except requests.exceptions.ConnectionError:
        logging.warning(f"NETERROR » {url}")

def generate_urls(filenames):
    urls = []
    for _ in range(210):  # Batch processing 30 URLs at a time
        ip = generate_ipv4()
        url = f"http://{ip}/{random.choice(filenames)}"
        urls.append(url)
    return urls


print("START SCAN..")
with Pool(processes=80) as pool:  # Create a pool of 20 worker processes
    while True:
        urls = generate_urls(filenames)
        pool.map(make_request, urls)
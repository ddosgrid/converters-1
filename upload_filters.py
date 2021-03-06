#!/usr/bin/env python3
import requests
import argparse
import os

parser = argparse.ArgumentParser(description='Publish filter rules to DDoSDB')
parser.add_argument('--authtoken',
                    help='OAuth2 token')
parser.add_argument('--url',
                    help='URL of the DDoSDB instance')
parser.add_argument('file', help='The iptables script to be published')
args = parser.parse_args()

inputFile = args.file

files = {
    "iptables": open(inputFile, "rb")
}

key = os.path.basename(inputFile).split(".")[0]
authtoken = args.authtoken
url = args.url

headers = {
    "X-Filename": key,
    "Authorization": "Bearer " + authtoken
}


r = requests.post(url, files=files, headers=headers,verify=True)
if r.status_code != 201:
    print("Failed to upload (" + str(r.status_code) + ")")
    print(r.text)

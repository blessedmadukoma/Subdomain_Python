#!/usr/bin/env python

import requests
import json
import sys


# get the domain to scan for subdomains

# search for command line arguments, reset to "annashut.com" if not found
args = sys.argv[1:]
domain = args[0] if len(args) > 0 else "annashut.com"

# read all subdomains
file = open("subdomains.txt")
# read all content
content = file.read()
# split by new lines
subdomains = content.splitlines()
file.close()

for subdomain in subdomains:
    # construct the url
    url = f"https://{subdomain}.{domain}"
    try:
        # if this raises an ERROR, that means the subdomain does not exist
        requests.get(url)
    except requests.ConnectionError:
        # if the subdomain does not exist, just pass, print nothing
        pass
    else:
        print("=> Discovered subdomain:", url)
        subdomain_name = url.split("//")[1].split(".")[0]
        dict = {'subdomain name': subdomain_name, 'domain name': url}
        #Convert the dictionary gotten to json
        dict = json.dumps(dict)
        print(dict)

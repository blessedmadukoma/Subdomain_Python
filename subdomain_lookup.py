#!/usr/bin/env python

import json
import sys
import time
import subprocess
import os.path


def get_subdomain_subpr(domain):
    base_dir = os.path.dirname(__file__)
    subprocess.run(["python", os.path.join(base_dir, "Sublist3r", "sublist3r.py"), "-d", domain,
                    "-o", os.path.join(base_dir, "subdomain_list.json")])
    subdomains = open(os.path.join(base_dir, "subdomain_list.json"), 'r').readlines()
    subdomains_new = []
    for line in subdomains:
        line = line.strip()
        if line:
            subdomains_new.append(line)
    with open(os.path.join(base_dir, "subdomain_list.json"), 'w') as file:
        file.write(json.dumps(subdomains_new))


if __name__ == '__main__':
    try:
        domain = sys.argv[1]
    except:
        print('Invalid input, use: "python {} <domain>"'.format(os.path.basename(__file__)))
        sys.exit()
    start = time.perf_counter()
    get_subdomain_subpr(domain)
    print("List of subdomains generated in", round(time.perf_counter() - start, 2), "seconds")
#!/usr/bin/env python

from pprint import pprint
import concurrent.futures
import requests
import json
import sys
import time
import re


def scrape(domain, subdomain):
    #for subdomain in subdomains:
    # construct the url
    #url = f"https://{subdomain}.{domain}"
    url = "https://" + subdomain + "." + domain
    
    try:
        # if this raises an ERROR, that means the subdomain does not exist
        requests.get(url)
    except requests.ConnectionError:
        # if the subdomain does not exist, just pass, print nothing
        pass
    else:
        for subdomain in subdomains:
            print("==> Discovered subdomain:", url)
            # subdomain_name = url.split("//")[1].split(".")[0]
            return url
    
    
def read_list():
    file = open("subdomains.txt")       # read all subdomains
    content = file.read()               # read all content
    subdomains = content.splitlines()   # split by new lines 
    file.close()
    return subdomains

    
def main(domain, subdomains):
    discovered = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        #executor.map(scrape_wrapper, subdomains)
        
        future_to_url = {executor.submit(scrape, domain, subdomain): subdomain for subdomain in subdomains}
        #[scrape_wrapper(subdomain) for subdomain in subdomains]
        
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                pass
            else:
                discovered.append(data)
    return discovered
    

if __name__ == '__main__':
    g = open("subdomain_list.json", 'w')
    # search for command line arguments, reset to "annashut.com" if not found
    args = sys.argv[1:]
    domain = args[0] if len(args) > 0 else "annashut.com"
    subdomains = read_list()
    
    # Profile the operation
    start = time.perf_counter()   
    discovered = main(domain, subdomains)
    print("done in", time.perf_counter() - start, "seconds")
    
    # Uncomment next line to print the result
    # pprint(discovered)

    # Write the output to a file as a json array
    g.write(json.dumps(discovered))
    g.close()

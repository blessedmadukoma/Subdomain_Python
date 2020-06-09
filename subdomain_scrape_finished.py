#!/usr/bin/env python

from pprint import pprint
import concurrent.futures
import threading
import requests
import json
import sys
import time
import re


def scrape(domain, subdomain):
    #for subdomain in subdomains:
        # construct the url
    #url = f"https://{subdomain}.{domain}"
    url = "https://"+ subdomain + "."+domain
    
    try:
        # if this raises an ERROR, that means the subdomain does not exist
        requests.get(url)
    except requests.ConnectionError as error:
        # if the subdomain does not exist, just pass, print nothing
        raise error
    else:
        for subdomain in subdomains:
            print("==> Discovered subdomain:", url)
            subdomain_name = url.split("//")[1].split(".")[0]
            dict = {'subdomain name': subdomain_name, 'domain name': url}
            #Convert the dictionary gotten to json
            #dict = json.dumps(dict)
            #print(dict)
            # open the file with r meaning to treat as raw string and ignore errors
            #g = open("php_file.json", "a")
            #g.write(dict + "\n")  # Writes each mail into mails.csv
            #g.close  # closes the file
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
                #print('%r generated an exception: %s' % (url, exc))
                pass
            else:
                discovered.append(data)
    return discovered
    

if __name__ == '__main__':
    g = open("php_file.json", 'w')
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

    Write the output to a file as a json array
    g.write(json.dumps(discovered))
    g.close()

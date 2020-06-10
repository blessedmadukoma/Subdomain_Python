# Subdomain checking code for Team-Neon backend

## Setup And Instructions
For python devs. To run the python script successfully please make sure you install the following modules with pip:
- `pip install -r requirements.txt`

After installing, run the script from command line in the form 
- `python subdomain_lookup.py <domain>`

or use the older brute force method
- `python subdomain_scrape_finished.py <domain>`

Where `<domain>` is the domain you wish to find its subdomains

The subdomains found would get stored in the file `subdomain_list.json` which would be created in the same directory as the script

Load the subdomain_list.json file to get the prepared json form of the list


The search method used here is a DNS Zone Transfer using the Sublist3r program included in this module. 
The repository for Sublist3r is at https://github.com/aboul3la/Sublist3r
 
### *#Team-Neon*

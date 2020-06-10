# Subdomain checking code for Team-Neon backend

## Setup
To run the python script successfully please make sure you have **Sublist3r** installed. For instructions
to install Sublist3r see below.

To use this script, first clone the repository 
- `git clone https://github.com/madukomablessed/Subdomain_Python`

then install the dependencies
- `pip install -r requirements.txt`

## Instructions
To search for subdomains, open the directory you cloned this repo into
- `cd path/to/Subdomain_Python` 

then run
- `python subdomain_lookup.py <domain>`

or use the older brute force method
- `python subdomain_scrape_finished.py <domain>`

Where `<domain>` is the domain you wish to find its subdomains

The subdomains found would get stored in the file `subdomain_list.json` which would be created in the same directory as the script

Load the subdomain_list.json file to get the prepared json form of the list


The search method used here is a DNS Zone Transfer using the Sublist3r program included in this module. 
The repository for Sublist3r is at [https://github.com/aboul3la/Sublist3r]
 
 
## Sublist3r Installation
To install sublist3r, open a terminal window and run

  - `git clone https://github.com/aboul3la/Sublist3r.git`

  - `cd Sublist3r`  

  - `pip install -r requirements.txt`
  
  - `python setup.py install`


### *#Team-Neon*


[]: https://github.com/aboul3la/Sublist3r
# Subdomain checking code for Team-Neon backend

<<<<<<< HEAD
## Setup
To run the python script successfully please make sure you have **Sublist3r** installed. For instructions
to install Sublist3r [see below](https://github.com/madukomablessed/Subdomain_Python#sublist3r-installation).

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

The subdomains found would get stored in the file `subdomain_list.json` which would be created in the same directory as the script.
Load this file to get the prepared json form of the list


The search method used here is a DNS Zone Transfer using the Sublist3r program included in this module. 
The repository for Sublist3r is at https://github.com/aboul3la/Sublist3r
 
 
## Sublist3r Installation
To install sublist3r, open a terminal window and run

  - `git clone https://github.com/aboul3la/Sublist3r.git`

  - `cd Sublist3r`  

  - `pip install -r requirements.txt`
  
  - `python setup.py install`

  ## php script
  steps to get the script running:
  -run `php -S localhost:3000` on your terminal
  -on the index.php file, insert the url you wish to get the subdomain from
  e.g:
  `require ('Script.php');
$class=new Script('<url>');`

- then run `localhost:3000` on your browser


### *#Team-Neon*
=======
## Setup And Instructions
For python devs. To run the python script successfully please make sure you install the following modules with pip:
- `pip install requests`
- `pip install json`

After installing, run the script from command line in the form 
- `python subdomain_scrape_finished.py <domain>` 

Where `<domain>` is the domain you wish to find its subdomains

For other devs, call the php_file.json and work with that

## *#Team-Neon*
>>>>>>> 6e57ac51a3396edc9994005b010d6fa607b9dcea

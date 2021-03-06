[![PyPI version](https://badge.fury.io/py/ecope.svg)](https://badge.fury.io/py/ecope)
# Ecommerce Perú Scrap CLI
> I'm already tired of the GUIs

Extract a list of products from some e-commerce websites more popular of Perú

## Features
- Scraping ecommerces by product category (Only some categories)
- Products export data in csv or json 

## Production 

Before you need Python 3.7 or more, then install ecope with pip

`pip install ecope`

Then you can usage this command `ecope` CLI :) 

Example 1: Export laptops in CSV format 

`ecope -c laptop -f csv`

Example 2: Export celular in JSON format with filename export.json

`ecope -c celular -f json -o export`

For more info

`ecope -h` 


## Development 

### Local installing 

First go to `application` folder and install (Python3.7 o later) with virtualenv or pipenv

`virtualenv env -p python3`

Then install dependencies:

` pip install -r requirements.txt `

For data scraping use CLI more info:

`python cli.py -h` 

## Todos
* Add more ecommerces websites
* paginate support 
* Support docker
* Tests


## Collaborate

How to collaborate?

* Let me issues or 
* Add more items in `application/ecommerces.json` (You can with PR direct)



License
----
MIT

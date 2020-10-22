# Ecommerce Perú Scrap CLI
> I'm already tired of the GUIs

Extract a list of products from some e-commerce websites more popular of Perú

## Features
- Scraping ecommerces by product category (Only some categories)
- Products export data in csv or json 

## Development usage 

First go to `application` folder and install (Python3.7 o later) with virtualenv or pipenv

`virtualenv env -p python3`

Then install dependencies:

` pip install -r requirements.txt `

For data scraping use CLI more info:

`python cli.py -h` 


## Production usage 

For execute in production mode:

`python setup.py install`

Then you can usage this command `ecope` CLI :) 

Example 1: Export laptops in CSV format 

`ecope -c laptop -f csv`

Example 2: Export celular in JSON format with filename export.json

`ecope -c celular -f json -o export`

For more info

`ecope -h` 

## TO-DO
* Add more ecommerces websites
* paginate support 
* Support docker
* Tests


## Collaborate

How to collaborate?

* Let me issues or 
* Add more items in `application/ecommerces.json` (You can with PR direct)


## License
[MIT](LICENCE.txt)
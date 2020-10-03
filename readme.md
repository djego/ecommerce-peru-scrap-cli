# Products list API
> From Scraping to API

A list of products from some e-commerce websites more popular of Perú


## Features
- Scraping ecommerces by product category
- Products export data in csv
- API services (comming soon)

## Development usage

First install (Python3.7 o later)

` pip install -r requirements.txt `

For data scraping use CLI more info:

`python cli.py -h`

For run server app

```
export FLASK_APP=api.py
export FLASK_ENV=development
python -m flask run 
```

## TO-DO
* (Scraping) Add more ecommerces websites
* (Scraping) paginate support 
* (Scraping+API) Category support
* API Public deploy
* Persistence in DB
* Tests
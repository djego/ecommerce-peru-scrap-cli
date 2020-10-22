import argparse
from scrap import Scraper
from utils import export_to

ap = argparse.ArgumentParser(prog='cli-export',
                              usage='%(prog)s [options] path',)

ap.add_argument("-c","--category", required=True, 
   choices=["laptop","celular"], default="laptop", help="category to export")

ap.add_argument("-o", "--output", required=False,
   help="file to export data", default="out")
ap.add_argument("-f", "--format", required=False,
   help="format to export data", choices=["csv","json"], default="csv")

args = vars(ap.parse_args())

scrap = Scraper(args['category'])
all_products = scrap.all_ecommerce()
exp = export_to(all_products, filename=args['output'], format=args['format'])
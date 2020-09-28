import argparse
from scrap import Scraper

ap = argparse.ArgumentParser()

ap.add_argument("-o", "--output", required=True,
   help="file to export data")
ap.add_argument("-f", "--format", required=False,
   help="format to export data", choices=["csv","json"])

args = vars(ap.parse_args())
scrap = Scraper()
total = scrap.fb() + scrap.ln() + scrap.rp()
scrap.export(total, filename=args['output'], format=args['format'])

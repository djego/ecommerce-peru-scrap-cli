import argparse
from scrap import Scraper
# Construct the argument parser
ap = argparse.ArgumentParser()
# Add the arguments to the parser
ap.add_argument("-o", "--output", required=True,
   help="file to export")

args = vars(ap.parse_args())
scrap = Scraper()
total = scrap.fb() + scrap.ln() + scrap.rp()
scrap.export(total, filename=args['output'])

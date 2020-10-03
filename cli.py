import argparse
from scrap import Scraper

ap = argparse.ArgumentParser(prog='cli-export',
                              usage='%(prog)s [options] path',)

ap.add_argument("-o", "--output", required=False,
   help="file to export data", default="out")
ap.add_argument("-f", "--format", required=False,
   help="format to export data", choices=["csv","json"], default="csv")
args = vars(ap.parse_args())

scrap = Scraper("laptop")

total = scrap.fb() + scrap.ln() + scrap.rp() + scrap.oc()
exp = scrap.export(total, filename=args['output'], format=args['format'])
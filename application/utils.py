import csv
import re
import os
import json
def price_to_float(x):
    rs = 0.0
    if x != None:
        rs = re.search("-?\d+(?:,\d{3})*(?:\.\d+)?", x).group()
        rs = float(rs.replace(",",""))
    return rs

def export_to(data, format="csv", filename="out"):
    all_formats = ("csv","json")
    filename_path = os.getcwd() + "/out/"+filename+"."+format
    #FIXME go to class in fhe future
    if not os.path.exists(os.path.dirname(filename_path)):
        try:
            os.makedirs(os.path.dirname(filename_path))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    if format in all_formats:
        if format == "csv":
            keys = data[0].keys()
            with open(filename_path, "w", newline="") as f:
                dict_writer = csv.DictWriter(f, keys)
                dict_writer.writeheader()
                dict_writer.writerows(data)
        if format == "json":
            with open(filename_path, 'w') as outfile:
                json.dump(data, outfile)

        print("Exported: %s items" % str(len(data)))

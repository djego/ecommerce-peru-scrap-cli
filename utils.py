import re
def price_to_float(x):
    rs = 0.0
    if x != None:
        rs = re.search("-?\d+(?:,\d{3})*(?:\.\d+)?", x).group()
        rs = float(rs.replace(",",""))
    return rs
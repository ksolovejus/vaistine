from requests import get
from lxml.etree import HTML

vaistai = []

for psl in range(1, 2):
    response = get(f'https://camelia.lt/c/prekiu-medis/nereceptiniai-vaistai-898?page={psl}#') #Gaunamas puslapis
    tree = HTML(response.text) # Puslapio HTML paverciamas "tree" kintamuoju
    products = tree.xpath("//div[contains(@class, 'product-card')]")
    vaistai +=(
        [{
            "name": p.xpath(".//div[contains(@class,'product-name')]/text()")[0].strip(), # We need "[0]" because "name" is list
            "price": p.xpath(".//div[contains(@class, 'price')]/text()")[0].strip()[:-2].replace(',', '.'),
            "discount": bool(p.xpath(".//div[contains(@class, 'discount-badge')]"))
        } for p in products])
    break

from requests import get
from lxml.etree import HTML

response = get("https://camelia.lt/c/prekiu-medis/arbatos-specializuotas-maistas-900?page=1")
html = HTML(response.text)
from bs4 import BeautifulSoup
import requests
import csv

page_to_scrape = requests.get("https://spartantcg.cl/")
soup = BeautifulSoup(page_to_scrape.content, 'html.parser')

producto = soup.find_all("a", attrs={"class": "full-unstyled-link"})
precios = soup.find_all("span", attrs={"class": "price-item--regular"})
tipos = soup.find_all("div", attrs={"class": "price__regular"})


with open("web_scrape.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["PRECIO", "TIPO VENTA"])
    
    for precio, tipo, producto in zip(precios, tipos, producto):
        precio_text = precio.get_text(strip=True)
        tipo_text = tipo.get_text(strip=True)
        producto_text = producto.get_text(strip=True)
        print(precio_text + " - " + tipo_text)
        writer.writerow([precio_text, tipo_text, producto_text])
from bs4 import BeautifulSoup
import bs4
import openpyxl
import requests

URL = "https://www.kbb.com/car-make-model-list/used/view-all/model/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}

# Create Excel

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'ScrapeData'
sheet.append(['Make', 'Model', 'Year', 'Slug'])


result = requests.get(URL, headers=headers)
doc = BeautifulSoup(result.text, "html.parser")

# Find Table
table = doc.find('tbody', class_='css-1x79xxz-TableBody e1f65lhp2')

bs4_rows = table.find_all('tr')

for row in bs4_rows:
    div = row.find_all('div', class_='css-1mzj64w-ContentWrapper e1f65lhp0')
    model = div[0].text
    make = div[1].text
    year_div = div[2]
    year_spans = year_div.find_all('span')
    for span in year_spans:
        data = span.find_all('a')
        year = data[0].string
        slug = data[0]['href']
        print("Make: ", make, "Model: ", model, "Year: ", year, "Slug: ", slug)
        sheet.append([make, model, year, slug])


# Save Excel
excel.save('KBB_MMY.xlsx')
print('done!')

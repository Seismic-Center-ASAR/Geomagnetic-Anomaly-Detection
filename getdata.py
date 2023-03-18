import requests
from bs4 import BeautifulSoup

# Make a request to the website page. Do not abuse with requests !
# Modifi the year, month or day according to your desired data download day
# The request will get the data table of geomagnetic data for a single day.
url = 'https://www.intermagnet.org/data-donnee/dataplot-1-eng.php?year=2023&month=3&day=19&start_hour=0&end_hour=24&filter_region%5B%5D=America&filter_region%5B%5D=Asia&filter_region%5B%5D=Europe&filter_region%5B%5D=Pacific&filter_region%5B%5D=Africa&filter_lat%5B%5D=NH&filter_lat%5B%5D=NM&filter_lat%5B%5D=E&filter_lat%5B%5D=SM&filter_lat%5B%5D=SH&sort=iaga&iaga_code=SUA&type=xyz&fixed_scale=0&format=html'
response = requests.get(url)

# Parse the HTML source code using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table element based on the class attribute
table = soup.find('table', {'class': 'span-6'})

# Extract the table data and write it to a text file
with open('table_data.txt', 'w') as file:
    file.write("Date/Time (UT)\tX (nT)\tY (nT)\tZ (nT)\tF (nT)\n") # write the header
    for row in table.find_all('tr'):
        for cell in row.find_all('td'):
            file.write(cell.get_text() + '\t')
        file.write('\n')
#Each file will contain a header. Do not forget to remove the headers if you will comnine data from multiple files.
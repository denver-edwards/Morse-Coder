from bs4 import BeautifulSoup
import requests

web = requests.get("http://self.gutenberg.org/articles/eng/Wabun_code").text

soup = BeautifulSoup(web,"html.parser")

table = soup.select_one(".wikitable")

rows = [str(row) for row in table.find_all("tr")[1::]]
# a  = [_ for _ in rows.find_all("td")]
# rows = table.find_all("tr")[1::]
rows = [item.split("</td>") for item in rows]
print((rows[0][1]))
from bs4 import BeautifulSoup

with open('my-website.html') as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, 'html.parser')
print(soup.title.string)
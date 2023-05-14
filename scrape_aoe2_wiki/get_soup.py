from bs4 import BeautifulSoup
from selenium import webdriver


def get_data_from_wiki(url):
    # Get the data from wiki

    
    # Set up the WebDriver and load the website
    driver = webdriver.Chrome()
    driver.get(url)

    # Get the HTML content of the loaded website
    html_content = driver.page_source

    # Close the WebDriver
    driver.quit()

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup


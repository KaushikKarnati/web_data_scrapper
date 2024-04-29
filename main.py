import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_data(url,tag,class_name=None):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        if class_name:
            elements = soup.find_all(tag,class_=class_name)
        else:
            elements = soup.find_all(tag)

        extracted_data = [element.get_text(strip=True) for element in elements]
        return extracted_data

    except requests.RequestException as e:
        print(f'error fetching data from {url} : {e}')
        return []


def save_to_excel(data, file_name):
    """
    This function saves the provided data into an Excel file.

    Parameters:
    - data (list): Data to be saved.
    - file_name (str): Name of the Excel file to be created.

    Returns:
    - None
    """
    # Creating a DataFrame
    df = pd.DataFrame(data, columns=["Extracted Data"])

    # Saving the DataFrame to an Excel file
    df.to_excel(file_name, index=False)
    print(f"Data saved to {file_name} successfully.")

# Uncomment the lines below to use the functions
user_url = input("Enter the URL to scrape: ")
user_tag = input("Enter the HTML tag to extract: ")
user_class = input("Enter the class name (optional, press enter to skip): ")
if user_class == "":
  user_class = None
data = scrape_data(user_url, user_tag, user_class)
save_to_excel(data, "scraped_data.xlsx")





import os
import pandas as pd
import numpy as np
import requests
import bs4
import lxml


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def question1():
    """
    NOTE: You do NOT need to do anything with this function.

    """
    # Don't change this function body!
    # No python required; create the HTML file.

    return


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------




def extract_book_links(text):
    """
    :Example:
    >>> fp = os.path.join('data', 'products.html')
    >>> out = extract_book_links(open(fp, encoding='utf-8').read())
    >>> url = 'scarlet-the-lunar-chronicles-2_218/index.html'
    >>> out[1] == url
    True
    """
    soup = bs4.BeautifulSoup(text)
    articles = soup.find_all('article', class_='product_pod')
    links = []
    for article in articles:
        # star rating
        star = article.find('p', class_='star-rating')['class'][1]
        # price
        price_text = article.find('p', class_='price_color').text
        price_text = ''.join(filter(lambda x: x.isdigit() or x == '.', price_text)) # GPT
        price = float(price_text)
        if price < 50 and (star == 'Four' or star == 'Five'):
            # link
            link = article.find('a')['href']
            links.append(link)
    return links


def get_product_info(text, categories):
    """
    :Example:
    >>> fp = os.path.join('data', 'Frankenstein.html')
    >>> out = get_product_info(open(fp, encoding='utf-8').read(), ['Default'])
    >>> isinstance(out, dict)
    True
    >>> 'Category' in out.keys()
    True
    >>> out['Rating']
    'Two'
    """
    # By GPT
    soup = bs4.BeautifulSoup(text)
    info = {}
    
    # Title
    info['Title'] = soup.h1.text
    
    # Category
    breadcrumb = soup.find('ul', class_='breadcrumb')
    category = breadcrumb.find_all('a')[-1].text.strip()
    if category not in categories:
        return None
    info['Category'] = category
    
    # Rating
    rating = soup.find('p', class_='star-rating')['class'][1]
    info['Rating'] = rating
    
    # Product Description
    description = soup.find('div', id='product_description')
    if description:
        description_text = description.find_next('p').text
    else:
        description_text = ""
    info['Description'] = description_text
    
    # Product Table
    table = soup.find('table', class_='table table-striped')
    rows = table.find_all('tr')
    
    # Extract information from the table
    for row in rows:
        header = row.find('th').text.strip()
        value = row.find('td').text.strip()
        info[header] = value
    
    return info


def scrape_books(k, categories):
    """
    :param k: number of book-listing pages to scrape.
    :returns: a dataframe of information on (certain) books
    on the k pages (as described in the question).
    :Example:
    >>> out = scrape_books(1, ['Mystery'])
    >>> out.shape
    (1, 11)
    >>> out['Rating'][0] == 'Four'
    True
    >>> out['Title'][0] == 'Sharp Objects'
    True
    """
    base_url = "http://books.toscrape.com/catalogue/page-{}.html"
    book_links = []
    
    for i in range(1, k+1):
        url = base_url.format(i)
        response = requests.get(url)
        links = extract_book_links(response.text)
        book_links.extend(links)
    
    book_info_list = []
    for link in book_links:
        book_url = "http://books.toscrape.com/catalogue/" + link
        response = requests.get(book_url)
        info = get_product_info(response.text, categories)
        if info:
            book_info_list.append(info)
    
    df = pd.DataFrame(book_info_list)
    return df


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def stock_history(ticker, year, month):
    """
    Given a stock code and month, return the stock price details for that month
    as a DataFrame.

    >>> history = stock_history('BYND', 2019, 6)
    >>> history.shape == (20, 13)
    True
    >>> history.label.iloc[-1]
    'June 03, 19'
    """
    api_key = 'RAgrDosBFHcH1N1qGRG06n6W76lkQCHe'
    import calendar
    start_date = f"{year}-{month:02d}-01"
    end_date = f"{year}-{month:02d}-{calendar.monthrange(year, month)[1]}"
    base_url = f'https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}?from={start_date}&to={end_date}&apikey={api_key}'
    
    response = requests.get(base_url)
    data = response.json()
    
    if 'historical' in data:
        df = pd.DataFrame(data['historical'])
    else:
        df = pd.DataFrame()
    
    return df


def stock_stats(history):
    """
    Given a stock's trade history, return the percent change and transactions
    in billions of dollars.

    >>> history = stock_history('BYND', 2019, 6)
    >>> stats = stock_stats(history)
    >>> len(stats[0]), len(stats[1])
    (7, 6)
    >>> float(stats[0][1:-1]) > 30
    True
    >>> float(stats[1][:-1]) > 1
    True
    >>> stats[1][-1] == 'B'
    True
    """
    # get the percent change
    close_price = history['close'].iloc[0]
    open_price = history['open'].iloc[-1]
    percent_change = (close_price - open_price) / open_price * 100
    percent_change_str = f'{percent_change:.2f}%'
    if percent_change > 0 :
        percent_change_str = '+' + percent_change_str

    # get the total volume
    average_price = 0.5 * (history['high']+ history['low'])
    total_volume = sum(history['volume'] * average_price) / 1e9
    total_volume_str = f'{total_volume:.2f}B'

    return percent_change_str, total_volume_str



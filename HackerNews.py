import requests
import os
from multiprocessing import Pool, cpu_count
from functools import partial
from bs4 import BeautifulSoup, SoupStrainer
#Makes Output Directory if it does not exist
if not os.path.exists(os.path.join(os.getcwd(), 'HackerNews')):
  os.makedirs(os.path.join(os.getcwd(), 'HackerNews'))
'''
@params page_no: The page number of HackerNews to fetch.
Adding only page number in order to add multiprocess support in future.
@params verbose: Adds verbose output to screen instead of running the program silently.
'''
def get_article_snippet(url):
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'html.parser')
        meta_description = soup.find('meta', attrs={'name': 'description'})
        if meta_description:
            return meta_description['content']
        else:
            return soup.find('p').text
    except:
        return "Could not fetch snippet."

def fetch(page_no, query, category, verbose=False):
    #Should be unreachable, but just in case
    if page_no <= 0:
        raise ValueError('Number of Pages must be greater than zero')
    page_no = min(page_no, 20)
    i = page_no
    if verbose:
        print('Fetching Page {}...'.format(i))
    try:
        if query:
            res = requests.get('https://hn.algolia.com/api/v1/search?query='+query+'&tags='+category+'&page='+str(i))
        else:
            res = requests.get('https://hn.algolia.com/api/v1/search_by_date?tags='+category+'&page='+str(i))
        results = res.json()['hits']
        with open(os.path.join('HackerNews', '{}_{}_NewsPage{}.txt'.format(query, category, i)), 'w+') as f:
            f.write('-'*80)
            f.write('\n')
            f.write('Page {}'.format(i))
            for result in results:
                if result.get('points', 0) > 100:
                    f.write('\n'+'-'*80+'\n')
                    f.write('\nArticle Title: '+result.get('title', 'Could not get article title'))
                    f.write('\nSource URL: '+result.get('url', 'No URL found for this article'))
                    snippet = get_article_snippet(result.get('url'))
                    f.write('\nArticle Snippet: '+snippet)
                    f.write('\nArticle Author: '+result['author'])
                    f.write('\nArticle Score: '+str(result['points']))
                    f.write('\nPosted: '+result['created_at'])
                    f.write('\n'+'-'*80+'\n')
    except (requests.ConnectionError, requests.packages.urllib3.exceptions.ConnectionError) as e:
        print('Connection Failed for page {}'.format(i))
    except requests.RequestException as e:
        print("Some ambiguous Request Exception occurred. The exception is "+str(e))
while(True):
    try:
        query = input('Enter your search query (optional): ')
        category = input('Enter category (default: story): ') or "story"
        pages = int(input('Enter number of pages that you want the HackerNews for (max 20): '))
        v = input('Want verbose output y/[n] ?')
        verbose = v.lower().startswith('y')
        if pages > 20:
            print('A maximum of only 20 pages can be fetched')
        pages = min(pages, 20)
        for page_no in range(1, pages + 1):
            fetch(page_no, query, category, verbose)
        break
    except ValueError as e:
        print('\nInvalid input, probably not a positive integer\n')
        continue

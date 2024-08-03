# HackerNews-Scraper
A simple web scraper to scrape the Hacker News(HN) website for news at https://news.ycombinator.com

Parameters:

**pages:** Number of pages one wants the HackerNews for, this creates one file for each page, and a maximum of only 20 pages can be fetched for now.

**verbose:** Enable or disable verbose output by Y/N, if Y, then progress is printed to the terminal when each page is fetched, 
else, the program runs silently.

First, please install the dependencies for this scraper by using the `requirements.txt` file
```python
pip install -r requirements.txt
```

To use this for your daily share of HackerNews headlines, please clone and use the `HackerNews.py` file
```python
git clone https://github.com/bharatr21/HackerNews-Scraper.git
```

Future Scope: 
- Add support to extract a small snippet/preview of text from each article
- Add Multiprocess support in future, making it as an optional argument
- Add support to fetch more pages

Any contributions to this Project are always Welcome!!

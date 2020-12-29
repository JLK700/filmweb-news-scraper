# Filmweb News Scraper


## Description

Python script providing a corpus which contains Polish
cinematography-related news articles that can be later
used, for example, in NLP analysis.


#### Technologies
  - Python 3
  - bs4
  - requests

## How to use

Enter the range of sites from which you want to scrape
filmweb news (18 news per site) and a corpus.json
file will be created in the script directory.

#### Corpus details

The corpus is saved in a json file.  
Each news object can be identified with a unique id and
contains 4 types of information:
- News Title
- Date of Publication
- News Type
- Text of the news

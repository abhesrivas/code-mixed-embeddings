# Custom twitass scraper
Custom scraper that scrapes tweets from the Twitter Advanced Search webpage using the TwitAss API

# How do I set up? #

## Install the python modules

  - If you want to use python 2

    ```  
    pip install -r requirements2.txt
    ```
  - If you want to use python 3

    ```
    pip install -r requirements3.txt
    ```

## To scrape N tweets based on KEYWORD

  - python3 demo.py KEYWORD N 0 0
  
## To scrape N tweets based on KEYWORDS in a TXT file

  - python3 demo.py - N START_INDEX END_INDEX
  
The scraped .txt file will be saved in scraped folder.

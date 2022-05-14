# Kelly-Blue-Book
Scraping KBB website with BS4 for a web development project


## Project Overview

The goal of this project was to build a comprehensive list of recent vehicles in the US market. The scraping was done in stages:

1. Scrape all make/model/year combinations from KBB's master list, along with the URLs to those pages.
2. Read in the list of make/model/year URLs, and scrape those for a list of every trim option available for the vehicle, along with the URLs for those pages
3. Scrape each of the trim URLs and gather the trim's image URL

## Workflow

The scraping was performed with a basic loop, and pages that resulted in errors were saved and pushed to a separate error file so I could compile and re-run them.

## File Explanation
Here is a detailed overview of the scripts and the resultant data

### MMYScrapeFinal.py
This script is the initial gathering of make/model/year combos and their URLs

**Output: KBB_MMY.xlsx**

### MMY-Trim Scrape.py
This script gathers all the trim options for each MMY, and the URLs to those pages

**Output: KBB_MMY_Trim_URLs.xlsx**

### KBB Model Image Scrape.py
This script opens each trim URL, gathers the image URL, and compiles the final dataset

**Output: KBB MMYT Final Data.xlsx**

## Lessons Learned

Coding experience at this time was approximately 1 month. I had just learned that scraping was possible and watched/read enough material to get started. Here's a list of the hurdles and concepts I came across:

* Serving headers
* VPNs / Rotating IP Address services
* Unethical Scraping
* CDN Rate Limiting (eventually banned my IP)

# Kelly-Blue-Book
Scraping KBB website with BS4 for a web development project


## Project Overview

The goal of this project was to build a comprehensive list of recent vehicles in the US market. The scraping was done in stages:

1. Scrape all make/model/year combinations from KBB's master list, along with the URLs to those pages.
2. Read in the list of make/model/year URLs, and scrape those for a list of every trim option available for the vehicle, along with the URLs for those pages
3. Scrape each of the trim URLs and gather the trim's image URL

## Workflow

The scraping was performed with a basic loop, and pages that resulted in errors were saved and pushed to a separate error file so I could compile and re-run them.

## Lessons Learned

Coding experience at this time was approximately 1 month. I had just learned that scraping was possible and watched/read enough material to get started. Here's a list of the hurdles and concepts I came across:

* Serving headers
* VPNs / Rotating IP Address services
* Unethical Scraping
* CDN Rate Limiting (eventually banned my IP)

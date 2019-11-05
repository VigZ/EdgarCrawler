# EdgarCrawler

This a simple crawler built with Scrapy, that will crawl EDGAR, and pull the most recent holding report for your chosen ticker or CIK, and then output to a .tsv file.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

1. First, you will want to clone this repo to your machine with a ```git clone``` command and create a virtual environment using ```virtualenv```.
2. Next, ```cd``` into the root directory of this project, activate your virtualenv, and run ```pip install -r requirements.txt``` to install the dependencies.

## Usage
From your console, run the command ```scrapy crawl edgar_crawler```. This will prompt you for a CIK or ticker symbol. Enter your desired string, and hit enter.
The scraper will run, scrape your desired data, and output to a .tsv file (named after the CIK entered) that will appear in the scraped_reports directory. If no files are found using the CIK, an empty file will be created.

## Trials and Tribulations
Much of my prior experience is using the requests library, and BeautifulSoup4, but I decided to challenge myself and learn the Scrapy framework for this project. I'm not entirely happy with my solution for a dynamic user input interface, so I would love to hear
some feedback on what might be a better solution! I created very narrow rules for the crawler, as the data was located in a very specific place, and I didn't want my crawler to go crazy searching links it didn't need to. (The robots.txt didn't seem to want much scraping).

I needed to override the default csv feed exporter to allow for a different delimeter (In this case a tab, for our tsv).

There were two fields when scraping that were problematic (Those being the putcall and othermanager fields), as they didn't appear on every report. I had run into some NoneType errors while attempting to add them to the field dictionary,
so I decided to wrap them both in a try/except block. I would like to go back and implement a more dynamic solution, but the current solution works, albeit a little ugly.

I also ran into a funny "bug" while testing. Every field for each row was being correctly filled, except for the value field. The numbers were close, but still off. After wracking my brain for a while, I realized that while I had been testing, EDGAR was updated with a new latest report!
Which explains the misfilled values! After refreshing my testing shell, the values then aligned. What are the odds?!

## Testing

Testing was perhaps the most difficult part of this project. During development, the scrapy shell and response inspector were mvp's, as they allowed me to fine tune my xpath selectors/BS4 selectors, and manually test responses.

For unit testing, I had initally written a response mocker, utilizing a library called Betamax, and unittest...however I ran into many issues with relative imports within a file being run as __main__. I tried a variety of different
approaches, but nothing seemed to work, so I decided to turn to the less powerful Spider Contracts.

Spider Contracts are a sort of testing framework built into scrapy, that let you test a response pre and post evaluation.

These are inlayed into the docstring of the method that is parsing the response.

I threw a few small tests in, to ensure the item responses are shaped correctly, and are of the correct quantity.

You can run the tests with the command ```scrapy check```

I would love some feedback on efficient ways to test a recursive crawler if you wouldn't mind!

### Bugs

I did my best to squash any bugs, but there is one that I noticed, albeit small.

Because of the way I am invoking a user input, the user is prompted to enter a CIK when running tests. This input doesn't affect the testing however.
When the tests are run, an empty .tsv will be created.

### Feedback

I would greatly appreciate any and all feedback you may have. I'd also love to chat about this project. Thanks!

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks to the countless Scrapy tutorials the denizens of the internet have created.

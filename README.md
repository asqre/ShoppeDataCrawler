# Shoppee Scraper using Selenium in python 

Fields that will be retrieved are: 'Radarly pid", "Radarly corpusId", "Radarly corpusName", "Product_Name", "Product_url",  "Status", "Name", "Customer_Profile_Url", "Rating", "TimeStamps", "Review", "Media_Url", "Likes", "Id".
 
#### Fair Warning
Web scraping is not an exact science at times, so if a web page's structure changes, or even if something as simple as a class is renamed or a data-hook type attribute removed, this code will break. This repo could use some foolproofing and more thought, but for now it works - and we're definitely happy to have any contributions.

#### Debugging Tip
If you're running/testing and having errors, your chromedriver process is likely still running so make sure to Force quit or kill the process in your OS task/process manager.

#### Setup with pipenv
Install all dependencies from the `selenium`

```
pip install selenium
```

# Windows
py amzreviewscrape.py --asins="C:\PATH\TO\ASINS\FILE.CSV" --driverpath="C:\PATH\TO\CHROMEDRIVER"

# Mac OSx/Linux
py amzreviewscrape.py --asins="/path/to/asins/csv" --driverpath="/path/to/chromedriver"
To pass additional options to chromedriver such as:


#### The CSV Output currently looks like:

![output][screenshot]
![image](https://github.com/asqre/ShoppeDataCrawler/assets/62792214/ccc08a46-b316-4009-8e1d-775fd42fc903)

[screenshot]: https://github.com/aflansburg/amzreviewsscrape/blob/master/scrape-output.png 'CSV Output Screen Shot'


Certainly! Here's an example of a README.md file for your GitHub repository for the project that scrapes historical reviews from a website using Python and Selenium:

```markdown
# Historical Reviews Scraper

This Python script allows you to scrape historical reviews from a specified URL using Selenium. The extracted reviews are stored as text data for further analysis or storage.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python: Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
- Selenium: Install the Selenium library using `pip` by running `pip install selenium`.
- WebDriver: You'll need a WebDriver compatible with your browser (e.g., Chrome WebDriver). Download and configure it according to your system. You can download Chrome WebDriver [here](https://sites.google.com/chromium.org/driver/).

## Installation

1. Clone the repository:

```shell
git clone https://github.com/yourusername/historical-reviews-scraper.git
```

2. Navigate to the project directory:

```shell
cd historical-reviews-scraper
```

3. Install the required Python packages:

```shell
pip install -r requirements.txt
```

## Usage

1. Replace the `path/to/chromedriver` in the code with the actual path to your WebDriver executable.

2. Modify the `url` variable in the code to point to the webpage you want to scrape reviews from.

3. Run the script:

```shell
python scrape_reviews.py
```

4. The extracted reviews will be printed to the console and stored in the `historical_reviews.txt` file.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix:

```shell
git checkout -b feature/your-feature-name
```

3. Make your changes and commit them:

```shell
git commit -m 'Add your commit message here'
```

4. Push your changes to your fork:

```shell
git push origin feature/your-feature-name
```

5. Create a pull request on the original repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

You can customize this README to include more specific information about your project, such as additional features, usage examples, or any other relevant details.

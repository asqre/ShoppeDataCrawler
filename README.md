# Shoppee Scraper using Selenium in python 

This Python script allows you to scrape reviews from a specified URL using Selenium. The extracted reviews are stored as text data for further analysis or storage.
Fields that will be retrieved are: 'Radarly pid", "Radarly corpusId", "Radarly corpusName", "Product_Name", "Product_url",  "Status", "Name", "Customer_Profile_Url", "Rating", "TimeStamps", "Review", "Media_Url", "Likes", "Id".
 
#### Fair Warning
Web scraping is not an exact science at times, so if a web page's structure changes, or even if something as simple as a class is renamed or a data-hook type attribute removed, this code will break. This repo could use some foolproofing and more thought, but for now it works - and we're definitely happy to have any contributions.

#### Debugging Tip
If you're running/testing and having errors, your chromedriver process is likely still running so make sure to Force quit or kill the process in your OS task/process manager.

#### Setup with selenium
Install all dependencies from the `selenium`

```
pip install selenium
```

# Windows
py amzreviewscrape.py --asins="C:\PATH\TO\ASINS\FILE.CSV" --driverpath="C:\PATH\TO\CHROMEDRIVER"

# Mac OSx/Linux
py amzreviewscrape.py --asins="/path/to/asins/csv" --driverpath="/path/to/chromedriver"
To pass additional options to chromedriver such as:

## Example Data Format

### The JSON Output looks like 
```json
 {
        "Radarly pid": 6127,
        "Radarly corpusId": 64143,
        "Radarly corpusName": "Feminine Care",
        "Product_Name": "New tide rimless sunglasses ladies fashion all-match UV protection sunscreen sunshade sunglasses",
        "Product_url": "https://shopee.com.my/New-tide-rimless-sunglasses-ladies-fashion-all-match-UV-protection-sunscreen-sunshade-sunglasses-i.992975877.23941383249?sp_atk=c1860b1e-55b1-445d-86a6-ff85b3d50752&xptdk=c1860b1e-55b1-445d-86a6-ff85b3d50752",
        "Status": "Historical",
        "Name": "teodorabermido",
        "Customer_Profile_Url": "https://shopee.com.my/shop/128476722",
        "Rating": 5,
        "TimeStamps": "Philippines | 2023-08-22 15:49",
        "Review": "",
        "Media_Url": [
            "https://play-ws.vod.shopee.com/api/v4/11110103/mms/ph-11110103-6ke14-lkqktwtbv9vv57.default.mp4",
            "https://down-ws-in.img.susercontent.com/ph-11134103-7r98o-lkqktcm3fhbz5d.webp"
        ],
        "Likes": "1",
        "Id": ""
    },
```

#### The CSV Output currently looks like:

![image](https://github.com/asqre/ShoppeDataCrawler/assets/62792214/ccc08a46-b316-4009-8e1d-775fd42fc903)


```markdown

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python: Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
- Selenium: Install the Selenium library using `pip` by running `pip install selenium`.
- WebDriver: You'll need a WebDriver compatible with your browser (e.g., Chrome WebDriver). Download and configure it according to your system. You can download Chrome WebDriver [here](https://sites.google.com/chromium.org/driver/).
```
## Installation

1. Clone the repository:

```shell
git clone git@github.com:asqre/ShoppeDataCrawler.git
```

```shell
pip install selenium
```

## Usage

1. Replace the `path/to/chromedriver` in the code with the actual path to your WebDriver executable.

2. Modify the `url` variable in the code to point to the webpage you want to scrape reviews from.


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


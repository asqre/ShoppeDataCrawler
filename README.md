# Shoppee Scraper using Selenium in Python

## Overview

This Python script enables you to efficiently extract product reviews from specified URLs using Selenium. The scraped reviews are stored as text data, ready for further analysis or storage.

## Data Fields

The following data fields will be retrieved:

- Radarly pid
- Radarly corpusId
- Radarly corpusName
- Product_Name
- Product_url
- Status
- Name
- Customer_Profile_Url
- Rating
- TimeStamps
- Review
- Media_Url
- Likes
- Id

## Fair Warning

Web scraping can be a challenging endeavor due to the dynamic nature of web pages. If the structure of a webpage changes or elements like classes or attributes are modified, this code may break. While this repository could benefit from additional robustness and thoughtful design, it currently serves its purpose.

## Debugging Tip

If you encounter errors while running or testing the code, it's possible that the chromedriver process is still running. Be sure to force quit or terminate the process using your OS task or process manager.

## Setup with Selenium

### Installation of Dependencies

To get started, install all dependencies using pip:

```shell
pip install selenium
```

### Configuration

#### Windows

Replace `path/to/chromedriver` with the actual path to your Chrome WebDriver executable:

```python
path/to/chromedriver = "C:\\Users\\VICTUS\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
```

#### Mac OSx/Linux

Replace `path/to/chromedriver` with the correct path to your Chrome WebDriver executable:

```python
path/to/chromedriver = "C:/Users/VICTUS/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
```

## Example Data Format

The JSON output is structured as follows:

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
}
```

#### The CSV Output currently looks like:

![image](https://github.com/asqre/ShoppeDataCrawler/assets/62792214/ccc08a46-b316-4009-8e1d-775fd42fc903)


## Prerequisites

Before you begin, ensure you have the following requirements in place:

- **Python:** Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

- **Selenium:** Install the Selenium library using pip by running:

  ```shell
  pip install selenium
  ```

- **WebDriver:** You'll need a WebDriver compatible with your browser (e.g., Chrome WebDriver). Download and configure it according to your system. You can download Chrome WebDriver [here](https://sites.google.com/chromium.org/driver/).

## Installation

1. Clone the repository:

   ```shell
   git clone git@github.com:asqre/ShoppeDataCrawler.git
   ```

2. Install Selenium if not already installed:

   ```shell
   pip install selenium
   ```

## Usage

1. Replace the `path/to/chromedriver` in the code with the actual path to your WebDriver executable.

2. Modify the `url` variable in the code to point to the webpage from which you want to scrape reviews.

3. Run the script.

4. The extracted reviews will be displayed in the console and saved in the `historical_reviews.txt` file.

## Contributing

Contributions are welcome! To contribute to this project, follow these steps:

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


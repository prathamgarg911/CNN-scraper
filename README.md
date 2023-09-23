# CNN Website Scraper

This repository contains a Python script that uses the Scrapy framework to scrape news headlines, timestamps, and related images from the CNN website.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/prathamgarg911/CNN-scraper.git
```

2. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. Navigate to the project directory:

```bash
cd web_cnn
```

2. Run the Scrapy spider:

```bash
scrapy crawl web_scrape_cnn -O scraped_data.json
```

This will start the scraping process and save the data to an `scraped_data.json` file and the images to a folder named scraped-images.

## Output

The scraper will generate a JSON file (`scraped_data.json`) with the following structure:

```json
[
  {
    "headline": "Sample Headline",
    "timestamp": "Day Month Date, Year",
    "image_link": "https://example.com/image.jpg",
    "local_image": "web_cnn/scraped-images/image1.jpg"
  }
]
```
You can also generate a CSV file (`scraped_data.csv`) with a similar structure.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Make sure to follow the [Contributing Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

# Web Scraping Quotes Analysis

A complete data analysis project demonstrating how to collect public web data, clean it, transform it, and perform exploratory data analysis using Python.

## 📌 Project Overview

This project collects quotes from **[Quotes to Scrape](https://quotes.toscrape.com/)**, a website specifically designed for practicing web scraping.

The scraped data contains quotes, authors, and associated tags. The project then processes the collected data and performs exploratory data analysis to identify patterns in authors, tags, and quote lengths.

## 🎯 Objectives

* Collect quote data from a public website using web scraping.
* Store the scraped data as a raw dataset.
* Investigate the quality and structure of the collected data.
* Clean and transform the dataset.
* Create useful features for analysis.
* Perform exploratory data analysis.
* Visualize patterns using Matplotlib and Seaborn.
* Document the findings in a reproducible GitHub project.

## 🌐 Data Source

**Website:** [Quotes to Scrape](https://quotes.toscrape.com/)

The website provides publicly accessible quote data for web-scraping practice.

The project collected **100 quotes across 10 pages**.

### Collected Fields

| Column   | Description                    |
| -------- | ------------------------------ |
| `quote`  | Text of the quote              |
| `author` | Author of the quote            |
| `tags`   | Tags associated with the quote |

## 🛠️ Technologies Used

* Python
* Requests
* BeautifulSoup
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook
* Git & GitHub

## 🔄 Project Workflow

```text
Quotes to Scrape
       ↓
Web Scraping
       ↓
Raw Dataset
       ↓
Data Investigation
       ↓
Data Cleaning
       ↓
Exploratory Data Analysis
       ↓
Visualization
       ↓
Insights & Conclusion
```

## 🕷️ Web Scraping

The website was scraped using:

* `requests` for retrieving webpage content.
* `BeautifulSoup` for parsing HTML.
* Pagination handling to collect quotes from multiple pages.

The scraper extracts:

* Quote text
* Author
* Tags

The raw scraped dataset is stored in:

```text
data/raw/quotes_raw.csv
```

## 🔍 Data Investigation

The collected dataset was investigated for:

* Missing values
* Duplicate records
* Data types
* Unique authors
* Tag structure
* Empty tag lists
* Whitespace issues
* Duplicate tags within individual quotes
* Tag frequency
* Quote length

The investigation showed that the dataset did not contain major data-quality problems.

## 🧹 Data Cleaning

The cleaning process included:

* Converting the serialized `tags` values back into Python lists.
* Removing unnecessary whitespace from quote text.
* Validating author formatting.
* Checking tag formatting.
* Preserving valid empty tag lists instead of removing them.

The cleaned dataset is stored in:

```text
data/cleaned/quotes_cleaned.csv
```

## ⚙️ Feature Engineering

Two additional features were created for analysis:

### `quote_length`

The number of characters in each quote.

### `tag_count`

The number of tags associated with each quote.

These features were used to investigate quote-length patterns and relationships between quotes and their tags.

## 📊 Exploratory Data Analysis

The analysis covered:

### Author Analysis

* Number of quotes per author
* Average quote length by author
* Average number of tags by author
* Quote-length distribution across frequently occurring authors

### Tag Analysis

* Most frequently occurring tags
* Number of tags per quote
* Tag distribution across the dataset

### Quote Analysis

* Quote-length distribution
* Minimum, maximum, mean, and median quote length

### Relationship Analysis

* Quote length vs. tag count
* Number of quotes vs. average quote length

Visualizations were created using **Seaborn** and **Matplotlib** and saved in the `images/` directory.

## 🔎 Key Findings

* The dataset contains **100 quotes from 50 unique authors**.
* Albert Einstein has the highest number of quotes in the collected dataset with **10 quotes**.
* `love` is the most frequent tag with **14 occurrences**.
* Most quotes contain **one or two tags**.
* The average number of tags per quote is **2.32**.
* Quote length ranges from **34 to 1,084 characters**.
* The median quote length is **86 characters**, while the mean is **122.27 characters**.
* The analysis did not show a strong visual relationship between quote length and tag count.

These findings describe the collected dataset and should not be generalized to all quotes or authors.

## 📂 Project Structure

```text
web-scraping-quotes-analysis/
│
├── scraper/
│   └── scraper.py
│
├── data/
│   ├── raw/
│   │   └── quotes_raw.csv
│   │
│   └── cleaned/
│       └── quotes_cleaned.csv
│
├── notebooks/
│   └── Quotes-raw-data-analysis.ipynb
│
├── images/
│   
├── docs/
│   └── EDA_Conclusion.md
│
├── README.md
└── requirements.txt
```

## 🚀 How to Run

Clone the repository:

```bash
git clone https://github.com/vikasa-y/web-scraping-quotes-analysis.git
```

Navigate into the project:

```bash
cd web-scraping-quotes-analysis
```

Install the required libraries:

```bash
pip install -r requirements.txt
           or
pip install pandas , matplotlib, seaborn , numpy , Beautifulsoup4 , request , python 3.13.7
```

Run the scraper:

```bash
python scraper/scraper.py
```

Then open the notebook:

```text
notebooks/Quotes-raw-data-analysis.ipynb
```

## 📌 Limitations

* The analysis is based on only 100 collected quotes.
* The dataset represents the content available on the scraped pages at the time of collection.
* The results describe this specific dataset rather than the broader population of quotes or authors.
* Quote tags are website-provided labels and may not represent every possible theme within a quote.

## 🚀 Future Improvements

* Store scraped data in a SQL database.
* Expand the dataset by collecting additional permitted pages.
* Perform more advanced text analysis.
* Analyze relationships between authors and themes.
* Apply natural language processing techniques such as sentiment or keyword analysis.
* Build an interactive dashboard for exploring the collected quotes.

## 📄 Documentation

Additional EDA findings and conclusions are available in:

```text
docs/EDA_Conclusion.md
```

## 📚 Learning Focus

This project was built to practice and demonstrate a complete data workflow:

**Web Scraping → Data Cleaning → Feature Engineering → EDA → Visualization → Insights**

It also provides practical experience working with semi-structured scraped data and converting it into an analysis-ready dataset.

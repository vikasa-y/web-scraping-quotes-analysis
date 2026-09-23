# 📊 Overall EDA Conclusion

The exploratory data analysis was performed on **100 quotes collected from Quotes to Scrape**. The analysis focused on authors, tags, quote length, and relationships between these variables.

## Key Findings

* The dataset contains **50 unique authors**, with Albert Einstein having the highest number of quotes (**10**).
* **Love** was the most frequently occurring tag with **14 occurrences**, followed by **inspirational** and **life**, each with **13 occurrences**.
* Most quotes contain **one or two tags**, with an average of **2.32 tags per quote**.
* Quote length ranges from **34 to 1,084 characters**, with a median of **86 characters** and a mean of **122.27 characters**.
* The difference between the mean and median quote length indicates that a small number of substantially longer quotes increase the average.
* Quote length varies across authors, and the distribution within individual authors shows that their quotes do not all have similar lengths.
* The analysis of quote length and tag count does not show a strong visual relationship between the two variables.
* Authors with more collected quotes do not necessarily have longer average quotes.

## Overall Conclusion

The dataset is relatively small but provides useful insights into the distribution of authors, themes, tags, and quote lengths. The analysis also demonstrates how scraped web data can be transformed into a structured dataset and investigated using data-cleaning and exploratory-analysis techniques.

The project shows the complete workflow from **web scraping → data cleaning → feature creation → exploratory data analysis → visualization → insights**.

Because the dataset contains only 100 quotes from a single website, the findings describe this particular collected dataset and should not be generalized to all quotes or authors.

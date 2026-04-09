# 📊 Big Data Science and Analytics in Financial Data (IDX Stocks)

This project demonstrates the implementation of a **Big Data pipeline**, **API integration**, **database management**, and **financial data analysis** using Indonesian stock market (IDX) data.

The system is built using **Python** and **PostgreSQL** to retrieve, process, store, and analyze stock market End-of-Day (EOD) data.

---

# 🚀 Project Workflow (01–08)

## 🔹 01. Database Connection

* Established connection to PostgreSQL using `psycopg2` and `SQLAlchemy`
* Verified database connectivity

## 🔹 02. IDX API Ingestion

* Retrieved Indonesian stock ticker list
* Processed and stored stock symbols for further analysis

## 🔹 03. EOD API Data Collection

* Connected to EOD Historical Data API
* Retrieved End-of-Day (EOD) stock data
* Parsed JSON data into structured format using pandas

## 🔹 04. Store Data to PostgreSQL

* Designed EOD stock database schema
* Inserted cleaned stock data into PostgreSQL
* Verified successful storage with SQL queries

## 🔹 05. SQL Analysis

* Performed financial data analysis using SQL:

  * Total records count
  * Aggregation of stock volume
  * Highest and lowest prices
  * Sorting and grouping
* Retrieved results into pandas DataFrame

## 🔹 06. Data Visualization

* Visualized stock data using matplotlib:

  * Bar charts (top stocks by volume)
  * Basic financial insights

## 🔹 07. Full IDX Stock Pipeline

* Automated pipeline for:

  * Fetching stock tickers
  * Collecting EOD data via API
  * Cleaning dataset
  * Exporting to CSV
* Demonstrates Big Data workflow integration

## 🔹 08. Advanced Analysis

* Performed cross-sectional stock analysis:

  * Price distribution
  * Top and lowest priced stocks
  * Market classification (High vs Low)
  * Summary statistics
* Visualization of market structure

---

# 📊 Dataset Description

The dataset contains stock market data with the following attributes:

* `symbol` — Stock ticker
* `date` — Trading date
* `open` — Opening price
* `high` — Highest price
* `low` — Lowest price
* `close` — Closing price
* `volume` — Trading volume

---

# ⚠️ Important Note

Due to API limitations (rate limits and access restrictions), the final dataset represents a **single-day snapshot** of the Indonesian stock market.

As a result:

* Time-series analysis (trend, index movement) is limited
* Machine Learning models (e.g., LSTM) are not applied
* Analysis focuses on **cross-sectional market insights**

This reflects a real-world data engineering challenge and demonstrates adaptability in analysis strategy.

---

# 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* PostgreSQL
* SQLAlchemy
* psycopg2
* REST API (EOD Historical Data)
* Jupyter Notebook
* Visual Studio Code

---

# 📈 Key Features

* End-to-end Big Data pipeline
* API data ingestion and processing
* Database design and storage
* SQL-based financial analysis
* Data visualization
* Adaptive analysis under data limitations

---

# 🧠 Insights

* Stock prices vary significantly across companies
* A small number of stocks dominate in price value
* Many stocks fall into lower price ranges
* Market classification helps identify high-value stocks
* Dataset reflects real-world limitations in financial data access

---

# 👨‍💻 Author

Ivan Firmansyah

---

# 📌 Conclusion

This project demonstrates how Big Data technologies and financial analysis techniques can be applied to stock market data.

Despite API limitations, the project successfully:

* Builds a complete data pipeline
* Performs structured analysis
* Provides meaningful financial insights

---

# ⭐ Notes

This project reflects real-world challenges in:

* Data availability
* API limitations
* Data cleaning and validation

and shows how to adapt analytical approaches accordingly.
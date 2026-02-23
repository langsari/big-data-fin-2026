# Big Data Science and Analytics in Financial Data (Stocks)

This project demonstrates the implementation of database design, API integration, and quantitative financial analysis using stock market data.

The system is built using PostgreSQL and Python to retrieve, store, analyze, and visualize stock End-of-Day (EOD) data.

---

## 1. Installation and Configuration

The following tools were installed and configured:

- Anaconda
- Jupyter Notebook
- Visual Studio Code (development environment)
- Python Libraries:
  - pandas
  - numpy
  - matplotlib
  - psycopg2
  - SQLAlchemy
- PostgreSQL
- pgAdmin
- Apache Spark (environment setup)
- Apache Cassandra (environment setup)

---

## 2. Basic Financial Database

### Database Creation via pgAdmin

- Created financial database in PostgreSQL
- Created stock data table
- Inserted basic financial records manually
- Verified table structure and data storage

### Database Creation via Python (Jupyter Notebook)

- Established PostgreSQL connection using psycopg2 / SQLAlchemy
- Created stock table programmatically using SQL
- Inserted financial data into database via Python
- Verified successful insertion using SQL queries

---

## 3. Database Design

A stock End-of-Day (EOD) database schema was designed to store structured stock market data.

### Table Structure:

- symbol (stock code)
- date (trading date)
- open (opening price)
- high (highest price)
- low (lowest price)
- close (closing price)
- volume (trading volume)

The schema was validated and queried successfully using SQL.

---

## 4. API Integration

- Connected to EOD Historical Data API
- Retrieved stock market End-of-Day (EOD) data via REST API
- Processed JSON response using pandas
- Cleaned and validated dataset
- Inserted structured data into PostgreSQL database

Data Source:
EOD Historical Data (https://eodhistoricaldata.com/api)

---

## 5. SQL Data Retrieval and Analysis

Performed SQL-based financial data analysis including:

- Counting total records in database
- Aggregating trading volume by stock symbol
- Identifying highest and lowest stock prices
- Grouping and sorting stock data using SQL
- Retrieving query results into pandas DataFrame

All queries were executed from Jupyter Notebook using SQLAlchemy.

---

## 6. Data Visualization

Basic visualization was performed using matplotlib:

- Bar chart of top traded stocks by total volume
- Visualization of stock performance metrics

This demonstrates integration between database querying and analytical visualization in Python.

---

## Technologies Used

- Python
- PostgreSQL
- Pandas
- NumPy
- SQLAlchemy
- psycopg2
- Matplotlib
- REST API integration

---

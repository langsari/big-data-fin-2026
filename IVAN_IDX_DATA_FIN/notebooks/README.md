# Big Data Science and Analytics in Financial Data (Stocks)

This project demonstrates the implementation of database design, API integration, and quantitative stock analysis using PostgreSQL and Python.

---

## 1. Installation and Configuration

The following tools were installed for Big Data environment setup:

- Anaconda
- Jupyter Notebook
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
- Created stock table
- Inserted basic financial data manually

### Database Creation via Python (Jupyter Notebook)
- Established connection using psycopg2 / SQLAlchemy
- Created table using SQL commands in Python
- Inserted financial data programmatically

---

## 3. Database Design

A stock End-of-Day (EOD) schema was designed with the following structure:

- symbol (stock code)
- date (trading date)
- open (opening price)
- high (highest price)
- low (lowest price)
- close (closing price)
- volume (trading volume)

The schema was validated using PostgreSQL and queried successfully.

---

## 4. API Integration

- Connected to stock market API
- Retrieved stock data programmatically
- Cleaned and validated data using pandas
- Inserted cleaned data into PostgreSQL database

---

## 5. SQL Data Retr

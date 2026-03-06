\# Stock Market Data Analytics Pipeline



\## Overview

This project builds an end-to-end financial analytics pipeline using Python, PySpark, MySQL, SQL and Power BI.



The system processes historical S\&P 500 stock market data and generates analytics dashboards for market insights.



---



\## Architecture



!\[Architecture](images/architecture.png)



Pipeline Flow:



CSV Dataset → Python Cleaning → PySpark Processing → MySQL Warehouse → SQL Analytics → Power BI Dashboard



---



\## Technologies Used



\- Python

\- Pandas

\- PySpark

\- MySQL

\- SQL

\- Power BI

\- Git



---



\## Features



• Processes 497k+ stock market records  

• Implements ETL pipeline for financial datasets  

• Performs analytics queries on stock performance  

• Visualizes market trends and trading volume  



---



\## Project Structure

stock-market-data-pipeline

│

├── python

│ ├── data\_cleaning.py

│ └── load\_to\_mysql.py

│

├── pyspark

│ └── process\_stock\_data.py

│

├── sql

│ └── analytics\_queries.sql

│

├── dashboard

│ └── stock\_market\_dashboard.pbix

│

├── images

│ ├── architecture.png

│

├── README.md

└── .gitignore



\## Author



Pranjali Sharma


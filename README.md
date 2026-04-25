# Log Detective ETL Pipeline 🔍
A Python-based automation tool that extracts error data from server logs and stores them in a structured SQLite database.

## 🚀 Features
- **Extraction:** Automated parsing of log files using Python's `enumerate`.
- **Transformation:** Real-time data cleaning and hourly error categorization using the `datetime` module.
- **Loading:** Permanent storage of processed logs in a SQLite database for future analysis.

## 🛠️ How to Run
1. Clone this repository.
2. Ensure you have a `server_log.txt` file in the directory.
3. Run `proccessor.py` to populate the database.
4. Run `reader.py` to view the stored results.

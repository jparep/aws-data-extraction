# Extracting Specific Health Data Fields with Date Filtering (Nov 2024 - Current) from AWS PostgreSQL

## Overview
This project focuses on extracting specific health data fields from an AWS-hosted PostgreSQL database, with date filtering from November 2024 to the current date in 2025.

## Prerequisites
- AWS account with access to the PostgreSQL database
- PostgreSQL client installed
- Python 3.11+ installed
- Required Python libraries: `psycopg2`, `pandas`, `SQLAlchemy`

## Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/jparep/aws-data-extraction.git
    cd aws-data-extraction
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Configure database connection:**
    Update the `config.py` file with your AWS PostgreSQL database credentials.

## Usage

1. **Run the extraction script:**
    ```sh
    python extract_data.py
    ```

2. **Specify the date range:**
    Modify the `extract_data.py` script to set the desired date range for data extraction.

## Output
The extracted data will be saved in a CSV file in the `output` directory.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or issues, please open an issue on the [GitHub repository](https://github.com/jparep/aws-data-extraction).

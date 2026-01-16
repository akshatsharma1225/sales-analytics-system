# Sales Analytics System

##  Project Overview

The **Sales Analytics System** is a Python-based data processing and reporting application designed to analyze sales transactions, generate comprehensive business insights, and enrich product data through API integration. This system processes raw sales data, validates transactions, generates multiple report formats, and provides meaningful analytics for decision-making.

---

##  Key Features

### 1. **Data Processing & Validation**
- Reads sales data from pipe-delimited text files
- Handles multiple encoding formats (UTF-8, Latin-1, CP1252)
- Parses transaction records into structured data
- Validates transaction integrity using ID prefixes (T for Transactions, P for Products, C for Customers)
- Filters transactions by quantity, price, and region

### 2. **Report Generation**
- **Basic Report**: Quick summary of total revenue and sales by region
- **Comprehensive Sales Report**: Detailed analytics including:
  - Overall revenue summary with average order value
  - Regional performance breakdown with percentages
  - Top 5 performing products with revenue metrics
  - Top 5 customers by spending
  - Daily sales trends and customer engagement
  - Product performance analysis
  - API enrichment success metrics

### 3. **API Integration**
- Fetches product data from DummyJSON API
- Maps product IDs to comprehensive product information
- Enriches sales transactions with API-sourced product details (category, brand, rating)
- Tracks enrichment success rates

### 4. **Data Output**
- Generates formatted text reports
- Saves enriched transaction data
- Organized output directory structure

---

##  Project Structure

```
sales-analytics-system/
│
├── main.py                    # Entry point - orchestrates the entire workflow
├── readme.md                  # Project documentation
├── requirments.txt            # Python dependencies
│
├── data/
│   └── sales_data.txt        # Source data file with sales transactions
│
├── output/
│   ├── report.txt            # Basic revenue summary report
│   └── sales_report.txt      # Comprehensive analytics report
│
└── utils/
    ├── file_handler.py       # File I/O operations with encoding handling
    ├── data_processor.py     # Data parsing and validation logic
    └── api_handler.py        # API integration and data enrichment
```

---

##  Module Breakdown

### **main.py**
**Purpose**: Core orchestration and report generation

**Key Functions**:
- `generate_report(transactions)`: Creates basic revenue summary
- `generate_sales_report(transactions, enriched_transactions, output_file)`: Generates comprehensive analytics report with multiple sections

**Workflow**:
1. Reads sales data from file
2. Parses and validates transactions
3. Fetches product categories
4. Generates both basic and detailed reports
5. Outputs formatted reports to the output directory

---

### **utils/file_handler.py**
**Purpose**: File operations with robust encoding handling

**Key Functions**:
- `read_sales_data(filename)`: 
  - Reads sales data with automatic encoding detection
  - Tries UTF-8, Latin-1, and CP1252 encodings
  - Skips header row and empty lines
  - Returns list of cleaned transaction strings

**Features**:
- Error handling for file not found
- Graceful encoding fallback strategy
- Data cleaning (removes extra whitespace)

---

### **utils/data_processor.py**
**Purpose**: Data parsing and validation

**Key Functions**:

1. **`parse_transactions(raw_lines)`**
   - Splits pipe-delimited lines into fields
   - Validates exactly 8 fields per record
   - Converts numeric fields (quantity, unit price)
   - Handles comma-formatted numbers
   - Returns list of transaction dictionaries

2. **`validate_and_filter(transactions, region=None, min_amount=None, max_amount=None)`**
   - Validates ID prefixes (T, P, C)
   - Checks for positive quantity and price
   - Applies optional region and amount filters
   - Returns filtered transactions and validation summary

**Data Format**:
Each transaction contains:
- `TransactionID`: Unique identifier 
- `Date`: Transaction date 
- `ProductID`: Product code 
- `ProductName`: Product description
- `Quantity`: Number of units sold
- `UnitPrice`: Price per unit
- `CustomerID`: Customer identifier 
- `Region`: Geographic region (North, South, East, West)

---

### **utils/api_handler.py**
**Purpose**: API integration and product data enrichment

**Key Functions**:

1. **`fetch_product_info(product_id)`**
   - Maps product IDs to product categories
   - Uses local dictionary mapping (P101-P110)
   - Returns "Unknown" for unmapped products

2. **`fetch_all_products()`**
   - Fetches product data from DummyJSON API
   - URL: `https://dummyjson.com/products?limit=100`
   - Handles API errors gracefully
   - Returns list of product objects

3. **`create_product_mapping(api_products)`**
   - Converts API response into ID-based dictionary
   - Extracts title, category, brand, rating

4. **`enrich_sales_data(transactions, product_mapping)`**
   - Adds API data to transaction records
   - Fields added: `API_Category`, `API_Brand`, `API_Rating`, `API_Match`
   - Handles errors gracefully (sets API_Match=False on failure)

5. **`save_enriched_data(enriched_transactions, filename)`**
   - Persists enriched data to file
   - Maintains all original fields plus new API fields
   - Pipe-delimited format

---

##  Data Flow

```
sales_data.txt (Raw Data)
        ↓
read_sales_data() - File I/O with encoding handling
        ↓
parse_transactions() - Parse pipe-delimited format
        ↓
validate_and_filter() - Validation & filtering
        ↓
fetch_product_info() - Local product mapping
        ↓
generate_report() - Basic summary
        ↓
generate_sales_report() - Comprehensive analytics
        ↓
output/ (report.txt, sales_report.txt)
```

---

##  Report Contents

### **Basic Report (report.txt)**
- Total Revenue: Sum of all transactions
- Sales by Region: Revenue breakdown by geographic region

### **Comprehensive Sales Report (sales_report.txt)**

**Overall Summary Section**:
- Total Revenue (₹)
- Total Transactions
- Average Order Value
- Date Range

**Regional Performance**:
- Region-wise sales revenue
- Percentage of total
- Transaction count per region

**Top Performers**:
- Top 5 Products: Quantity sold and revenue
- Top 5 Customers: Spending and order count

**Trends & Analysis**:
- Daily Sales Trend: Revenue and customer engagement by date
- Best Selling Day: Highest revenue day
- Low Performing Products: Products with <10 units sold
- API Enrichment Summary: Success rate and missing enrichments

---

##  Data Sample

**Input Format (sales_data.txt)**:
```
TransactionID|Date|ProductID|ProductName|Quantity|UnitPrice|CustomerID|Region
T018|2024-12-29|P107|USB Cable|8|173|C009|South
T063|2024-12-07|P110|Laptop Charger|6|1,916|C022|East
T023|2024-12-09|P109|Wireless Mouse|9|523|C022|North
```

**Parsed Transaction Object**:
```python
{
    "TransactionID": "T018",
    "Date": "2024-12-29",
    "ProductID": "P107",
    "ProductName": "USB Cable",
    "Quantity": 8,
    "UnitPrice": 173,
    "CustomerID": "C009",
    "Region": "South",
    "Category": "Accessories"  # Added by fetch_product_info
}
```

---

##  Installation & Usage

### **Prerequisites**
- Python 3.7+
- `requests` library (for API calls)

### **Setup**
1. Clone/download the project
2. Install dependencies:
   ```bash
   pip install -r requirments.txt
   ```

### **Running the System**
```bash
python main.py
```

**Expected Output**:
```
========================================
       SALES ANALYTICS SYSTEM
========================================
Summary: {'total_input': 82, 'invalid': 5, 'final_count': 77}
✔ Basic report generated successfully!
✔ Comprehensive sales report generated successfully!

✔ PROCESS COMPLETED SUCCESSFULLY
Reports generated in /output folder
```

---

##  Dependencies

- **requests**: HTTP library for API integration
- **datetime**: Standard library for date handling
- **collections**: Standard library for defaultdict

---

##  Validation Rules

The system validates transactions using these criteria:

| Rule | Requirement |
|------|-------------|
| Transaction ID | Must start with "T" |
| Product ID | Must start with "P" |
| Customer ID | Must start with "C" |
| Quantity | Must be > 0 |
| Unit Price | Must be > 0 |
| Fields Count | Exactly 8 pipe-delimited fields |

Invalid transactions are skipped and counted in the summary.

---

##  Supported Regions

- **North**
- **South**
- **East**
- **West**

---

##  Output Files

| File | Purpose | Format |
|------|---------|--------|
| `output/report.txt` | Basic revenue summary | Text, simple format |
| `output/sales_report.txt` | Comprehensive analytics | Text, formatted with sections |

---

##  Error Handling

1. **File Not Found**: Displays error message, returns empty list
2. **Encoding Issues**: Tries multiple encodings (UTF-8 → Latin-1 → CP1252)
3. **API Failures**: Logs error, continues with graceful degradation
4. **Invalid Data**: Skips malformed records, tracks invalid count

---

##  Code Quality Features

- **Modular Design**: Separated concerns (I/O, processing, API, reporting)
- **Error Handling**: Try-except blocks for robust operation
- **Data Validation**: ID prefix and value checks
- **Encoding Support**: Multiple charset handling
- **API Integration**: External data enrichment capability
- **Formatted Output**: Human-readable report generation

---

##  Customization

### **Filtering Transactions**
```python
valid_data, invalid_count, summary = validate_and_filter(
    transactions,
    region="North",        # Filter by region
    min_amount=1000,       # Minimum transaction amount
    max_amount=50000       # Maximum transaction amount
)
```

### **Adding Product Categories**
Update the `categories` dictionary in `api_handler.py`:
```python
categories = {
    "P101": "Laptop",
    "P102": "Mouse",
    # Add more mappings...
}
```

---

##  Notes

- The system generates two distinct reports for different use cases
- Data enrichment from API is optional but recommended for complete analysis
- All monetary values are formatted with commas and rupee symbol (₹)
- Reports include timestamps for audit trails
- The application gracefully handles missing or incomplete data

---

##  Contributing

To extend this system:
1. Add new analysis functions in `main.py`
2. Extend `data_processor.py` for additional validation
3. Add more API integrations in `api_handler.py`
4. Modify report templates in `generate_sales_report()`

---

**Last Updated**: January 15, 2026  
**Version**: 1.0  
**Status**: Production Ready

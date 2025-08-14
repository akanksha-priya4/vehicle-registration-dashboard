# Data Directory

This directory contains the data files for the Vehicle Registration Dashboard.

## Structure

```
data/
├── raw/           # Raw data files (CSV, JSON, Excel)
├── processed/     # Processed and cleaned data files
└── README.md      # This file
```

## Data Sources

### Current: Sample Data
- **Format**: Generated programmatically
- **Size**: 20,000+ records
- **Period**: 3 years of daily data
- **Categories**: 2W, 3W, 4W vehicles

### Future: Vahan Dashboard Integration
- **Source**: Vahan Dashboard (Government of India)
- **Method**: Web scraping with Selenium
- **Update Frequency**: Daily/Weekly
- **Data Validation**: Automated quality checks

## File Formats Supported

- **CSV**: Comma-separated values
- **JSON**: JavaScript Object Notation
- **Excel**: .xlsx files
- **Parquet**: Columnar storage format

## Data Schema

```json
{
  "date": "YYYY-MM-DD",
  "year": 2024,
  "month": 8,
  "quarter": "Q3",
  "vehicle_type": "2W|3W|4W",
  "manufacturer": "Company Name",
  "registrations": 15000,
  "region": "North|South|East|West|Central"
}
```

## Data Processing Pipeline

1. **Raw Data Collection** → `data/raw/`
2. **Data Cleaning** → Remove duplicates, handle missing values
3. **Data Transformation** → Add calculated fields
4. **Data Aggregation** → Group by time periods
5. **Processed Data** → `data/processed/`

## Usage

The dashboard automatically loads data from these directories. To add new data:

1. Place raw files in `data/raw/`
2. Run data processing scripts
3. Processed files will appear in `data/processed/`
4. Dashboard will automatically detect and load new data
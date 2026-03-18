# Weekly KPI Report Automation (Python)

**Turns raw CSV exports into a clean weekly KPI report + charts, with an optional Streamlit dashboard.**

## What It Does

- 📊 **Generates synthetic lead inquiry data** – Creates 2,500 sample records over 120 days with realistic distributions
- 🧹 **Cleans and standardizes data** – Parses dates, normalizes strings, ensures data types
- 📈 **Computes weekly KPIs** – Aggregates leads, conversions, response times, SLA metrics, and revenue
- 📄 **Creates an HTML report** – Professional report with embedded charts and summary metrics
- 📉 **Generates visualization charts** – Line graphs for leads, conversion rates, response times, and revenue
- 🎛️ **Provides an interactive dashboard** – Streamlit app for exploring KPIs with date filtering
- ⚙️ **Automates with GitHub Actions** – Runs pipeline weekly on schedule or on-demand

## Why It Matters

This project demonstrates a complete data analytics workflow suitable for small businesses, startups, and teams managing customer leads. It's a **production-ready template** that can be adapted to real company data exports (Salesforce, HubSpot, Pipedrive, etc.). The pipeline is fully automated, reproducible, and requires no external APIs or paid tools.

## How to Run

### 1. Set Up Python Environment

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Generate Sample Data

```powershell
python src/generate_sample_data.py
```

Outputs: `sample_leads_raw.csv` (2,500 sample leads)

### 3. Clean Data & Compute KPIs

```powershell
python src/clean_and_kpi.py
```

Outputs: `outputs/cleaned_leads.csv`, `outputs/weekly_kpis.csv`

### 4. Build Report & Charts

```powershell
python src/build_report.py
```

Outputs: `outputs/report.html`, `outputs/charts/*.png`

### 5. (Optional) Launch Interactive Dashboard

```powershell
streamlit run app.py
```

Then open http://localhost:8501 in your browser.

## Outputs

- **`sample_leads_raw.csv`** – Raw synthetic lead data
- **`outputs/cleaned_leads.csv`** – Cleaned and standardized dataset
- **`outputs/weekly_kpis.csv`** – Weekly aggregated KPIs
- **`outputs/report.html`** – Professional HTML report with embedded charts
- **`outputs/charts/leads.png`** – Weekly leads trend
- **`outputs/charts/conversion_rate.png`** – Conversion rate trend
- **`outputs/charts/avg_response.png`** – Average response time trend
- **`outputs/charts/revenue.png`** – Weekly revenue trend

## Screenshots

_Add your own screenshots here:_

- **Report Summary**: `assets/report_summary.png`
- **Dashboard**: `assets/dashboard.png`

## Next Improvements

- 🔌 **Connect to real data sources** – Adapt `generate_sample_data.py` to read from Salesforce, HubSpot, CSV exports, or APIs
- 📧 **Add email delivery** – Send report HTML via email every Monday morning
- 🔍 **Expand analytics** – Add cohort analysis, funnel metrics, and attribution tracking
- 🎨 **Enhance visualizations** – Use Plotly for interactive charts, add more KPI dimensions
- 🗄️ **Database integration** – Store historical data in SQLite or PostgreSQL for trend analysis
- 🚨 **Alert system** – Trigger alerts when KPIs fall below thresholds

## Architecture

```
Raw Data (CSV)
     ↓
generate_sample_data.py
     ↓
sample_leads_raw.csv
     ↓
clean_and_kpi.py (Cleaning + Weekly Aggregation)
     ↓
outputs/cleaned_leads.csv
outputs/weekly_kpis.csv
     ↓
build_report.py (Charts + HTML Report)
     ↓
outputs/report.html
outputs/charts/*.png
     ↓
app.py (Streamlit Dashboard)
```

## Technology Stack

- **Python 3.11+**
- **pandas** – Data manipulation and aggregation
- **numpy** – Numerical operations
- **matplotlib** – Chart generation
- **streamlit** – Interactive dashboard

## License

This project is provided as-is for educational and commercial use.

---

**Questions?** This is a template designed to be modified for your specific data and business needs.


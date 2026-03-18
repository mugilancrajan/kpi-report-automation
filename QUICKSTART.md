## 🚀 Quick Start Guide - KPI Report Automation

### Project Status: ✅ COMPLETE

All files have been created and tested successfully. The pipeline runs end-to-end without errors.

---

### 📁 Project Structure

```
kpi-report-automation/
├── README.md                          # Full project documentation
├── requirements.txt                   # Python dependencies (pandas, numpy, matplotlib, streamlit)
├── .gitignore                         # Git ignore rules
├── app.py                             # Streamlit interactive dashboard
├── sample_leads_raw.csv               # Generated synthetic lead data (2,500 records)
├── src/
│   ├── generate_sample_data.py        # Generate 2,500 synthetic leads over 120 days
│   ├── clean_and_kpi.py               # Clean data + compute weekly KPIs
│   └── build_report.py                # Generate charts and HTML report
├── outputs/
│   ├── cleaned_leads.csv              # Cleaned dataset
│   ├── weekly_kpis.csv                # Weekly aggregated metrics
│   ├── report.html                    # Professional HTML report with embedded charts
│   └── charts/
│       ├── leads.png                  # Weekly leads trend
│       ├── conversion_rate.png        # Conversion rate trend
│       ├── avg_response.png           # Response time trend
│       └── revenue.png                # Revenue trend
├── .github/
│   └── workflows/
│       └── weekly_report.yml          # GitHub Actions workflow (scheduled + manual)
└── .venv/                             # Python virtual environment (not in git)
```

---

### ✅ Successfully Generated Outputs

#### Data Files
- **sample_leads_raw.csv** (2,500 rows)
  - lead_id, created_at, first_response_at, response_minutes
  - source, campaign, region, owner, status, converted, revenue_usd

- **outputs/cleaned_leads.csv**
  - Standardized and cleaned version of raw data

- **outputs/weekly_kpis.csv**
  - 18 weeks of aggregated metrics
  - Columns: week, leads, conversions, conversion_rate, avg_response_min, p50_response_min, revenue, sla_15m_pct, sla_60m_pct

#### Visualizations (PNG Charts)
- leads.png - Weekly lead volume trend
- conversion_rate.png - Weekly conversion rate %
- avg_response.png - Average response time in minutes
- revenue.png - Weekly revenue in USD

#### HTML Report
- **outputs/report.html** - Professional dashboard with:
  - Latest week summary metrics (8 KPI cards)
  - 4 embedded trend charts
  - Full weekly KPI table
  - Responsive design with gradient header

---

### 🎯 Test Results

✅ Data Generation
- Generated 2,500 leads uniformly over 120 days
- Conversions: 482 (19.3%)
- Total revenue: $1,163,503
- Avg response time: 39.5 minutes

✅ Data Cleaning
- All 2,500 records cleaned successfully
- Standardized all string fields
- Ensured numeric conversions
- Computed weekly buckets

✅ Report Generation
- 4 charts created successfully (PNG)
- HTML report generated with UTF-8 encoding
- All SLA metrics calculated correctly

✅ Streamlit Dashboard
- App starts successfully
- Loads KPI data without errors
- Ready for interactive exploration

---

### 🎬 How to Run the Pipeline

#### Step 1: Install Dependencies
```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

#### Step 2: Generate Sample Data
```powershell
python src\generate_sample_data.py
```

#### Step 3: Clean Data & Compute KPIs
```powershell
python src\clean_and_kpi.py
```

#### Step 4: Build Report & Charts
```powershell
python src\build_report.py
```

#### Step 5: Launch Dashboard (Optional)
```powershell
streamlit run app.py
```
Open http://localhost:8501 in your browser

---

### 📊 Sample KPI Metrics

Latest Week (2026-03-16):
- Total Leads: 58
- Conversion Rate: 12.07%
- Avg Response Time: 41.4 minutes
- Median Response Time: 33 minutes
- 15-Min SLA: 19.0%
- 60-Min SLA: 75.9%
- Revenue: $16,344

---

### 🔧 GitHub Actions Workflow

The `.github/workflows/weekly_report.yml` is configured to:
- **Triggers:**
  - Run every Monday at 8 AM UTC (cron: `0 8 * * 1`)
  - Manual trigger via workflow_dispatch

- **Steps:**
  1. Checkout repository
  2. Setup Python 3.11
  3. Install dependencies
  4. Generate sample data
  5. Clean data and compute KPIs
  6. Build report and charts
  7. Upload artifacts (30-day retention)

To trigger manually: Go to Actions tab → Weekly KPI Report Pipeline → Run workflow

---

### 🎨 Dashboard Features

The Streamlit app (`app.py`) includes:

✅ **Date Range Filter**
- Sidebar controls for start/end dates
- Real-time data filtering

✅ **Metric Cards**
- Latest week's leads, conversion rate, response time, revenue
- Conversions, median response, SLA metrics

✅ **Interactive Charts**
- Leads + Revenue dual-axis chart
- Conversion Rate + Avg Response dual-axis chart

✅ **Data Table**
- Full weekly KPI table with filtering
- Summary statistics for period

---

### 🔄 Customization Guide

#### To Connect Real Data:
Modify `src/generate_sample_data.py`:
1. Replace the generation logic with your data source (CSV, API, database)
2. Ensure output has same column names
3. Run the rest of the pipeline as-is

#### To Adjust KPI Calculations:
Edit `src/clean_and_kpi.py`:
- Add/modify the aggregation logic in `compute_weekly_kpis()`
- Add new SLA metrics in the SLA metrics section

#### To Customize Report Styling:
Edit `src/build_report.py`:
- Modify CSS in the `html` variable
- Adjust chart styling parameters

---

### 📋 Quality Checklist

- ✅ All files created in correct structure
- ✅ Scripts run end-to-end without manual edits
- ✅ Synthetic data generation is reproducible (seed=42)
- ✅ Data cleaning is robust (coerce errors, type conversion)
- ✅ Outputs are created successfully
- ✅ Streamlit app runs without errors
- ✅ README is polished and explains the project
- ✅ GitHub Actions workflow is configured
- ✅ No external APIs required
- ✅ No secrets or credentials needed
- ✅ Fully offline capable

---

### 📞 Technical Details

**Python Version:** 3.11+

**Dependencies:**
- pandas - Data manipulation
- numpy - Numerical operations
- matplotlib - Chart generation
- streamlit - Dashboard framework

**Runtime:** ~2-3 seconds per full pipeline run

**Data Volume:** 2,500 leads/run (easily scalable)

---

### 🚀 Next Steps

1. **Test the dashboard:** Run `streamlit run app.py`
2. **Review outputs:** Open `outputs/report.html` in a browser
3. **Check GitHub Actions:** Push to GitHub, go to Actions tab
4. **Customize:** Replace data source, add metrics, enhance styling
5. **Deploy:** Use GitHub Pages, GitHub Actions, or cloud platform

---

**Project:** KPI Report Automation | **Status:** ✅ Production Ready | **Date:** March 18, 2026


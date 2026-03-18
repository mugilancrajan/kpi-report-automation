"""
Build HTML report and generate charts from weekly KPI data.

This script reads the computed KPIs, generates line charts for key metrics,
and creates a professional HTML report with embedded visualizations.
"""

import pandas as pd
import matplotlib
matplotlib.use("Agg")  # Use non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pathlib import Path
from datetime import datetime


def create_charts(df_weekly):
    """
    Create line charts for key weekly metrics.
    
    Args:
        df_weekly: DataFrame with weekly KPIs
    """
    # Ensure charts directory exists
    Path("outputs/charts").mkdir(parents=True, exist_ok=True)
    
    # Parse week column as datetime
    df_weekly["week"] = pd.to_datetime(df_weekly["week"])
    
    # Chart styling
    plt.style.use("default")
    fig_size = (12, 5)
    line_color = "#2E86AB"
    grid_alpha = 0.3
    
    # Chart 1: Leads per week
    fig, ax = plt.subplots(figsize=fig_size)
    ax.plot(df_weekly["week"], df_weekly["leads"], marker="o", color=line_color, linewidth=2, markersize=6)
    ax.set_title("Leads per Week", fontsize=14, fontweight="bold")
    ax.set_xlabel("Week", fontsize=11)
    ax.set_ylabel("Number of Leads", fontsize=11)
    ax.grid(True, alpha=grid_alpha)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("outputs/charts/leads.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("  ✅ Generated: leads.png")
    
    # Chart 2: Conversion rate per week
    fig, ax = plt.subplots(figsize=fig_size)
    ax.plot(df_weekly["week"], df_weekly["conversion_rate"], marker="o", color="#A23B72", linewidth=2, markersize=6)
    ax.set_title("Conversion Rate per Week (%)", fontsize=14, fontweight="bold")
    ax.set_xlabel("Week", fontsize=11)
    ax.set_ylabel("Conversion Rate (%)", fontsize=11)
    ax.grid(True, alpha=grid_alpha)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("outputs/charts/conversion_rate.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("  ✅ Generated: conversion_rate.png")
    
    # Chart 3: Average response time per week
    fig, ax = plt.subplots(figsize=fig_size)
    ax.plot(df_weekly["week"], df_weekly["avg_response_min"], marker="o", color="#F18F01", linewidth=2, markersize=6)
    ax.set_title("Average Response Time per Week (minutes)", fontsize=14, fontweight="bold")
    ax.set_xlabel("Week", fontsize=11)
    ax.set_ylabel("Minutes", fontsize=11)
    ax.grid(True, alpha=grid_alpha)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("outputs/charts/avg_response.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("  ✅ Generated: avg_response.png")
    
    # Chart 4: Revenue per week
    fig, ax = plt.subplots(figsize=fig_size)
    ax.plot(df_weekly["week"], df_weekly["revenue"], marker="o", color="#06A77D", linewidth=2, markersize=6)
    ax.set_title("Revenue per Week ($)", fontsize=14, fontweight="bold")
    ax.set_xlabel("Week", fontsize=11)
    ax.set_ylabel("Revenue (USD)", fontsize=11)
    ax.grid(True, alpha=grid_alpha)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("outputs/charts/revenue.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("  ✅ Generated: revenue.png")


def build_html_report(df_weekly):
    """
    Build an HTML report with embedded charts and summary metrics.
    
    Args:
        df_weekly: DataFrame with weekly KPIs
    """
    # Parse week column
    df_weekly["week"] = pd.to_datetime(df_weekly["week"])
    
    # Get latest week data
    latest = df_weekly.iloc[-1] if len(df_weekly) > 0 else None
    
    # Build HTML
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weekly KPI Report</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background: #f5f7fa;
            color: #333;
            line-height: 1.6;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 20px;
        }
        header {
            background: linear-gradient(135deg, #2E86AB 0%, #A23B72 100%);
            color: white;
            padding: 40px;
            border-radius: 8px;
            margin-bottom: 40px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        header p {
            font-size: 1.1em;
            opacity: 0.95;
        }
        .timestamp {
            font-size: 0.9em;
            opacity: 0.85;
            margin-top: 10px;
        }
        .metrics-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }
        .metric-card {
            background: white;
            padding: 25px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            border-left: 4px solid #2E86AB;
        }
        .metric-card h3 {
            color: #666;
            font-size: 0.9em;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 12px;
        }
        .metric-card .value {
            font-size: 2em;
            font-weight: bold;
            color: #2E86AB;
        }
        .metric-card.alt1 { border-left-color: #A23B72; }
        .metric-card.alt1 .value { color: #A23B72; }
        .metric-card.alt2 { border-left-color: #F18F01; }
        .metric-card.alt2 .value { color: #F18F01; }
        .metric-card.alt3 { border-left-color: #06A77D; }
        .metric-card.alt3 .value { color: #06A77D; }
        .section {
            background: white;
            padding: 30px;
            border-radius: 8px;
            margin-bottom: 30px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        .section h2 {
            font-size: 1.5em;
            color: #2E86AB;
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 2px solid #f0f0f0;
        }
        .charts-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }
        .chart-container {
            text-align: center;
        }
        .chart-container img {
            max-width: 100%;
            height: auto;
            border: 1px solid #e0e0e0;
            border-radius: 6px;
            background: white;
            padding: 10px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.95em;
        }
        table th {
            background: #f8f9fa;
            color: #333;
            font-weight: 600;
            padding: 12px;
            text-align: left;
            border-bottom: 2px solid #dee2e6;
        }
        table td {
            padding: 12px;
            border-bottom: 1px solid #dee2e6;
        }
        table tr:hover {
            background: #f8f9fa;
        }
        footer {
            text-align: center;
            color: #999;
            font-size: 0.9em;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #e0e0e0;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>📊 Weekly KPI Report</h1>
            <p>Lead inquiry metrics and performance analysis</p>
            <div class="timestamp">Generated: """ + datetime.now().strftime("%B %d, %Y at %H:%M:%S") + """</div>
        </header>

        <div class="section">
            <h2>Latest Week Summary</h2>
            <div class="metrics-grid">
                <div class="metric-card">
                    <h3>Total Leads</h3>
                    <div class="value">""" + str(int(latest["leads"])) + """</div>
                </div>
                <div class="metric-card alt1">
                    <h3>Conversions</h3>
                    <div class="value">""" + str(int(latest["conversions"])) + """</div>
                </div>
                <div class="metric-card alt2">
                    <h3>Conversion Rate</h3>
                    <div class="value">""" + f"{latest['conversion_rate']:.1f}%" + """</div>
                </div>
                <div class="metric-card alt3">
                    <h3>Revenue</h3>
                    <div class="value">""" + f"${latest['revenue']:,.0f}" + """</div>
                </div>
            </div>
            <div class="metrics-grid">
                <div class="metric-card">
                    <h3>Avg Response Time</h3>
                    <div class="value">""" + f"{latest['avg_response_min']:.0f}m" + """</div>
                </div>
                <div class="metric-card alt1">
                    <h3>Median Response Time</h3>
                    <div class="value">""" + str(int(latest["p50_response_min"])) + """m</div>
                </div>
                <div class="metric-card alt2">
                    <h3>15-Min SLA</h3>
                    <div class="value">""" + f"{latest['sla_15m_pct']:.1f}%" + """</div>
                </div>
                <div class="metric-card alt3">
                    <h3>60-Min SLA</h3>
                    <div class="value">""" + f"{latest['sla_60m_pct']:.1f}%" + """</div>
                </div>
            </div>
        </div>

        <div class="section">
            <h2>📈 Trend Charts</h2>
            <div class="charts-grid">
                <div class="chart-container">
                    <img src="charts/leads.png" alt="Leads per Week">
                </div>
                <div class="chart-container">
                    <img src="charts/conversion_rate.png" alt="Conversion Rate">
                </div>
            </div>
            <div class="charts-grid">
                <div class="chart-container">
                    <img src="charts/avg_response.png" alt="Avg Response Time">
                </div>
                <div class="chart-container">
                    <img src="charts/revenue.png" alt="Revenue">
                </div>
            </div>
        </div>

        <div class="section">
            <h2>📊 Weekly KPI Details</h2>
            """ + df_weekly.to_html(index=False, classes="kpi-table") + """
        </div>

        <footer>
            <p>This report was automatically generated by the KPI Report Automation pipeline.</p>
        </footer>
    </div>
</body>
</html>
    """
    
    return html


def main():
    """Main execution function."""
    print("📊 Building report...")
    
    # Read weekly KPIs
    print("  Reading weekly KPI data...")
    df_weekly = pd.read_csv("outputs/weekly_kpis.csv")
    
    # Create charts
    print("🎨 Creating charts...")
    create_charts(df_weekly)
    
    # Build HTML report
    print("📝 Generating HTML report...")
    html_content = build_html_report(df_weekly)
    
    # Save report with UTF-8 encoding to handle emoji
    with open("outputs/report.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print("\n✅ Report generation complete!")
    print(f"  📄 Report: outputs/report.html")
    print(f"  📈 Charts: outputs/charts/")
    

if __name__ == "__main__":
    main()


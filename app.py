"""
Interactive Streamlit dashboard for KPI analysis.

This dashboard provides an interactive view of weekly KPIs with date filtering,
metric cards, trend charts, and detailed data tables.
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pathlib import Path
from datetime import datetime


def load_kpis():
    """Load and parse weekly KPIs."""
    kpi_path = Path("outputs/weekly_kpis.csv")
    
    if not kpi_path.exists():
        st.warning("⚠️ KPI data not found. Please run the pipeline first:")
        st.code("""
python src/generate_sample_data.py
python src/clean_and_kpi.py
python src/build_report.py
        """)
        st.stop()
    
    df = pd.read_csv(kpi_path)
    df["week"] = pd.to_datetime(df["week"])
    return df


def format_metric(value, label, is_percentage=False, is_currency=False):
    """Format and display a metric card."""
    col = st.columns(1)[0]
    with col:
        if is_currency:
            formatted = f"${value:,.0f}"
        elif is_percentage:
            formatted = f"{value:.1f}%"
        else:
            formatted = f"{value:,.0f}" if isinstance(value, (int, float)) and value > 100 else f"{value:.1f}"
        
        st.metric(label, formatted)


def main():
    """Main Streamlit app."""
    # Page config
    st.set_page_config(page_title="KPI Dashboard", layout="wide", initial_sidebar_state="expanded")
    
    # Title
    st.title("📊 Weekly KPI Dashboard")
    st.markdown("Interactive view of lead inquiry metrics and performance")
    
    # Load data
    df = load_kpis()
    
    # Sidebar filters
    st.sidebar.markdown("### 📅 Date Range Filter")
    min_date = df["week"].min().date()
    max_date = df["week"].max().date()
    
    col1, col2 = st.sidebar.columns(2)
    with col1:
        start_date = st.date_input("Start Date", value=min_date, min_value=min_date, max_value=max_date)
    with col2:
        end_date = st.date_input("End Date", value=max_date, min_value=min_date, max_value=max_date)
    
    # Convert to datetime for comparison
    start_datetime = pd.Timestamp(start_date)
    end_datetime = pd.Timestamp(end_date)
    
    # Filter data
    df_filtered = df[(df["week"] >= start_datetime) & (df["week"] <= end_datetime)].copy()
    
    if len(df_filtered) == 0:
        st.error("❌ No data available for selected date range")
        return
    
    # Get latest week in filtered range
    latest = df_filtered.iloc[-1]
    
    # Metric cards for latest week
    st.markdown("### 📈 Latest Week Metrics")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Leads", f"{int(latest['leads']):,}")
    with col2:
        st.metric("Conversion Rate", f"{latest['conversion_rate']:.1f}%")
    with col3:
        st.metric("Avg Response Time", f"{latest['avg_response_min']:.0f}m")
    with col4:
        st.metric("Revenue", f"${latest['revenue']:,.0f}")
    
    # Additional metrics in second row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Conversions", f"{int(latest['conversions']):,}")
    with col2:
        st.metric("Median Response Time", f"{int(latest['p50_response_min'])}m")
    with col3:
        st.metric("15-Min SLA", f"{latest['sla_15m_pct']:.1f}%")
    with col4:
        st.metric("60-Min SLA", f"{latest['sla_60m_pct']:.1f}%")
    
    # Charts
    st.markdown("### 📊 Trend Charts")
    
    col1, col2 = st.columns(2)
    
    # Chart 1: Leads and Revenue
    with col1:
        fig, ax1 = plt.subplots(figsize=(10, 5))
        
        ax1.plot(df_filtered["week"], df_filtered["leads"], marker="o", 
                color="#2E86AB", linewidth=2, markersize=6, label="Leads")
        ax1.set_xlabel("Week")
        ax1.set_ylabel("Leads", color="#2E86AB")
        ax1.tick_params(axis="y", labelcolor="#2E86AB")
        ax1.grid(True, alpha=0.3)
        
        ax2 = ax1.twinx()
        ax2.plot(df_filtered["week"], df_filtered["revenue"], marker="s", 
                color="#06A77D", linewidth=2, markersize=6, label="Revenue")
        ax2.set_ylabel("Revenue ($)", color="#06A77D")
        ax2.tick_params(axis="y", labelcolor="#06A77D")
        
        ax1.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
        plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha="right")
        
        fig.suptitle("Leads & Revenue Trend", fontsize=12, fontweight="bold", y=0.98)
        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)
    
    # Chart 2: Conversion Rate and Avg Response
    with col2:
        fig, ax1 = plt.subplots(figsize=(10, 5))
        
        ax1.plot(df_filtered["week"], df_filtered["conversion_rate"], marker="o", 
                color="#A23B72", linewidth=2, markersize=6, label="Conversion Rate")
        ax1.set_xlabel("Week")
        ax1.set_ylabel("Conversion Rate (%)", color="#A23B72")
        ax1.tick_params(axis="y", labelcolor="#A23B72")
        ax1.grid(True, alpha=0.3)
        
        ax2 = ax1.twinx()
        ax2.plot(df_filtered["week"], df_filtered["avg_response_min"], marker="s", 
                color="#F18F01", linewidth=2, markersize=6, label="Avg Response")
        ax2.set_ylabel("Avg Response Time (min)", color="#F18F01")
        ax2.tick_params(axis="y", labelcolor="#F18F01")
        
        ax1.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
        plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha="right")
        
        fig.suptitle("Conversion Rate & Response Time Trend", fontsize=12, fontweight="bold", y=0.98)
        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)
    
    # Data table
    st.markdown("### 📋 Detailed Weekly KPIs")
    
    # Format dataframe for display
    df_display = df_filtered.copy()
    df_display["week"] = df_display["week"].dt.strftime("%Y-%m-%d")
    
    # Reorder columns for better readability
    display_cols = ["week", "leads", "conversions", "conversion_rate", 
                   "avg_response_min", "p50_response_min", "sla_15m_pct", 
                   "sla_60m_pct", "revenue"]
    df_display = df_display[display_cols]
    
    st.dataframe(df_display, use_container_width=True, hide_index=True)
    
    # Summary statistics
    st.markdown("### 📌 Summary Statistics")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Leads (Period)", f"{df_filtered['leads'].sum():,}")
    with col2:
        st.metric("Avg Conversion Rate", f"{df_filtered['conversion_rate'].mean():.1f}%")
    with col3:
        st.metric("Avg Response Time", f"{df_filtered['avg_response_min'].mean():.1f}m")
    with col4:
        st.metric("Total Revenue (Period)", f"${df_filtered['revenue'].sum():,.0f}")
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #999; font-size: 0.9em;'>"
        "KPI Report Automation • Auto-generated dashboard | "
        f"Data updated: {df['week'].max().strftime('%B %d, %Y')}"
        "</div>",
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()


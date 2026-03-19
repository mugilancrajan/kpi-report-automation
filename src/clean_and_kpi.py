"""
Clean raw lead data and compute weekly KPIs.

This script reads the raw lead CSV, performs data quality checks and standardization,
then aggregates metrics by week for reporting.
"""

import pandas as pd
import numpy as np
from pathlib import Path


def clean_data(df):
    """
    Clean and standardize raw lead data.

    Args:
        df: Raw DataFrame from CSV

    Returns:
        Cleaned DataFrame
    """
    df = df.copy()

    # Parse datetime columns
    df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")
    df["first_response_at"] = pd.to_datetime(df["first_response_at"], errors="coerce")

    # Standardize string columns
    df["source"] = df["source"].str.lower().str.strip()
    df["campaign"] = df["campaign"].str.lower().str.strip()
    df["owner"] = df["owner"].str.lower().str.strip()
    df["region"] = df["region"].str.strip()

    # Ensure numeric columns
    df["response_minutes"] = pd.to_numeric(df["response_minutes"], errors="coerce").fillna(0).astype(int)
    df["converted"] = pd.to_numeric(df["converted"], errors="coerce").fillna(0).astype(int)
    df["revenue_usd"] = pd.to_numeric(df["revenue_usd"], errors="coerce").fillna(0).astype(int)

    # Remove rows with invalid dates
    df = df.dropna(subset=["created_at"])

    return df


def compute_weekly_kpis(df):
    """
    Compute weekly KPI metrics from cleaned lead data.

    Args:
        df: Cleaned DataFrame

    Returns:
        DataFrame with weekly KPIs
    """
    # Create week column (start of week)
    df["week"] = df["created_at"].dt.to_period("W").dt.start_time

    # Group by week and compute metrics
    weekly = df.groupby("week").agg({
        "lead_id": "count",
        "converted": ["sum", "mean"],
        "response_minutes": ["mean", "median"],
        "revenue_usd": "sum"
    }).reset_index()

    # Flatten column names
    weekly.columns = ["week", "leads", "conversions", "conversion_rate",
                      "avg_response_min", "p50_response_min", "revenue"]

    # Round numeric columns
    weekly["conversion_rate"] = (weekly["conversion_rate"] * 100).round(2)
    weekly["avg_response_min"] = weekly["avg_response_min"].round(1)
    weekly["p50_response_min"] = weekly["p50_response_min"].round(0).astype(int)
    weekly["revenue"] = weekly["revenue"].round(0).astype(int)

    # Compute SLA metrics
    sla_metrics = df.groupby("week").apply(
        lambda x: pd.Series({
            "sla_15m_pct": (x["response_minutes"] <= 15).mean() * 100,
            "sla_60m_pct": (x["response_minutes"] <= 60).mean() * 100,
        })
    ).reset_index()

    # Merge SLA metrics
    weekly = weekly.merge(sla_metrics, on="week", how="left")

    # Round SLA percentages
    weekly["sla_15m_pct"] = weekly["sla_15m_pct"].round(1)
    weekly["sla_60m_pct"] = weekly["sla_60m_pct"].round(1)

    # Sort by week
    weekly = weekly.sort_values("week").reset_index(drop=True)

    return weekly


def main():
    """Main execution function."""
    print("🔍 Reading raw data...")

    # Read raw data
    df_raw = pd.read_csv("sample_leads_raw.csv")
    print(f"  Loaded {len(df_raw):,} records")

    # Clean data
    print("🧹 Cleaning data...")
    df_clean = clean_data(df_raw)
    print(f"  Cleaned {len(df_clean):,} records (removed {len(df_raw) - len(df_clean)} invalid rows)")

    # Ensure outputs directory exists
    Path("outputs").mkdir(exist_ok=True)

    # Save cleaned data
    print("💾 Saving cleaned data...")
    df_clean.to_csv("outputs/cleaned_leads.csv", index=False)
    print(f"  Saved: outputs/cleaned_leads.csv")

    # Compute weekly KPIs
    print("📊 Computing weekly KPIs...")
    df_weekly = compute_weekly_kpis(df_clean)
    print(f"  Computed {len(df_weekly)} weeks of data")

    # Save weekly KPIs
    print("💾 Saving weekly KPIs...")
    df_weekly.to_csv("outputs/weekly_kpis.csv", index=False)
    print(f"  Saved: outputs/weekly_kpis.csv")

    # Print summary
    print("\n📈 Summary:")
    print(f"  Total leads: {len(df_clean):,}")
    print(f"  Total conversions: {df_clean['converted'].sum():,}")
    print(f"  Overall conversion rate: {df_clean['converted'].mean() * 100:.1f}%")
    print(f"  Total revenue: ${df_clean['revenue_usd'].sum():,.0f}")
    print(f"  Avg response time: {df_clean['response_minutes'].mean():.1f} minutes")


if __name__ == "__main__":
    main()


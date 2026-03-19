"""
Generate synthetic lead inquiry data for KPI analysis.

This script creates a realistic dataset of 2,500 customer leads over the last 120 days,
with response times, conversion status, and revenue. Perfect for testing analytics pipelines.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def generate_sample_data(num_rows=2500, seed=42):
    """
    Generate synthetic lead inquiry data.

    Args:
        num_rows: Number of lead records to generate
        seed: Random seed for reproducibility

    Returns:
        DataFrame with lead data
    """
    np.random.seed(seed)

    # Define date range (last 120 days)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=120)

    # Generate lead IDs
    lead_ids = [f"LEAD_{i:06d}" for i in range(1, num_rows + 1)]

    # Random dates uniformly distributed over the range
    created_at = [start_date + timedelta(days=np.random.uniform(0, 120)) for _ in range(num_rows)]

    # Response times: skewed distribution (gamma) with min 1 minute
    response_minutes = np.maximum(np.random.gamma(shape=2, scale=20, size=num_rows), 1).astype(int)

    # Calculate first response time
    first_response_at = [created + timedelta(minutes=int(resp)) for created, resp in zip(created_at, response_minutes)]

    # Define categorical options
    sources = ["website_form", "email", "instagram_dm", "referral", "event"]
    campaigns = ["spring_promo", "organic", "newsletter", "paid_search", "partner"]
    regions = ["ATL", "Cumming", "Alpharetta", "Remote"]
    owners = ["alex", "sam", "jordan", "taylor"]

    # Generate random categorical data
    source_data = np.random.choice(sources, num_rows, p=[0.35, 0.25, 0.15, 0.15, 0.10])
    campaign_data = np.random.choice(campaigns, num_rows, p=[0.25, 0.30, 0.20, 0.15, 0.10])
    region_data = np.random.choice(regions, num_rows, p=[0.35, 0.25, 0.25, 0.15])
    owner_data = np.random.choice(owners, num_rows, p=[0.25, 0.25, 0.25, 0.25])

    # Calculate conversion probability based on source and response time
    conversion_prob = np.zeros(num_rows)
    base_prob = 0.15  # 15% base conversion rate

    # Boost for fast responses
    conversion_prob[response_minutes <= 15] = base_prob + 0.15
    conversion_prob[(response_minutes > 15) & (response_minutes <= 60)] = base_prob + 0.05

    # Penalty for slow responses
    conversion_prob[response_minutes >= 240] = base_prob - 0.08

    # Boost for high-intent sources
    conversion_prob[source_data == "referral"] += 0.10
    conversion_prob[source_data == "event"] += 0.08

    # Clamp between 0 and 1
    conversion_prob = np.clip(conversion_prob, 0, 1)

    # Generate conversions
    converted = (np.random.random(num_rows) < conversion_prob).astype(int)

    # Generate revenue (only if converted, gamma distribution)
    revenue_usd = np.zeros(num_rows, dtype=int)
    converted_indices = np.where(converted == 1)[0]
    revenue_usd[converted_indices] = np.random.gamma(shape=3, scale=800, size=len(converted_indices)).astype(int)

    # Ensure revenue is non-negative
    revenue_usd = np.maximum(revenue_usd, 0)

    # Generate status
    statuses = []
    for conv in converted:
        if conv == 1:
            statuses.append("converted")
        else:
            statuses.append(np.random.choice(["open", "nurture", "lost"], p=[0.40, 0.35, 0.25]))

    # Create DataFrame
    df = pd.DataFrame({
        "lead_id": lead_ids,
        "created_at": created_at,
        "first_response_at": first_response_at,
        "response_minutes": response_minutes,
        "source": source_data,
        "campaign": campaign_data,
        "region": region_data,
        "owner": owner_data,
        "status": statuses,
        "converted": converted,
        "revenue_usd": revenue_usd
    })

    # Convert timestamps to ISO format strings
    df["created_at"] = df["created_at"].dt.strftime("%Y-%m-%d %H:%M:%S")
    df["first_response_at"] = df["first_response_at"].dt.strftime("%Y-%m-%d %H:%M:%S")

    return df


if __name__ == "__main__":
    print("🚀 Generating synthetic lead data...")

    df = generate_sample_data(num_rows=2500, seed=42)

    # Save to CSV
    df.to_csv("sample_leads_raw.csv", index=False)

    print(f"✅ Generated {len(df):,} leads")
    print(f"💾 Saved to: sample_leads_raw.csv")
    print(f"📊 Conversions: {df['converted'].sum():,} ({df['converted'].mean() * 100:.1f}%)")
    print(f"💰 Total revenue: ${df['revenue_usd'].sum():,.0f}")
    print(f"⏱️  Avg response time: {df['response_minutes'].mean():.0f} minutes")


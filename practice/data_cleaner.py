# data_cleaner.py
"""
Entreprise Data cleaning pipeline
CAs d'utilisation: CRM raw data normalization before ML ingestion

"""

from typing import Optional


def clean_customer_record(raw: dict) -> dict:
    """
    Clean and Type-convert a raw customer record.
    Returns a ML-ready dict with proper types.
    """

    def safe_int(val: str, default: int = 0) -> int:
        try:
            return int(float(str(val).strip()))
        except (ValueError, TypeError):
            return default

    def safe_float(val: str, default: float = 0.0) -> float:
        try:
            return float(int(str(val).strip().replace(",", ".")))
        except (ValueError, TypeError):
            return default

    def clean_string(val: str) -> str:
        return str(val).strip().lower().replace(" ", "")

    def parse_bool(val: str) -> bool:  # ❌ Pas bien compris
        return str(val).strip().lower() in ('1', 'true', 'yes', 'oui')

    return {
        "custumer_id": safe_int(raw.get("id", 0)),
        "name": clean_string(raw.get("name", "")),
        "email": clean_string(raw.get("email", "").replace(" ", "")),
        "age": safe_int(raw.get("age", 0)),
        "revenue": safe_float(raw.get("revenue", 0.0)),
        "is_premium": parse_bool(raw.get("premium", "0")),
        "churn_risk": safe_float(raw.get("churn", None))
    }


# Simulation de données brutes CRM
raw_customers = [
    {"id": "1001", "name": "  JOHN doe ", "email": " John@Corp.COM ",
     "age": "34", "revenue": "12,500.50", "premium": "yes", "churn": "0.23"},
    {"id": "1002", "name": "sara SMITH", "email": "sara@biz.com",
     "age": "N/A", "revenue": "8900", "premium": "0", "churn": "N/A"},
    {"id": "abc", "name": "  Bob ", "email": "bob@test.com",
     "age": "29", "revenue": "3,200.00", "premium": "true", "churn": "0.87"},
]

print("=" * 140)
print(f"    {'CUSTUMER DATA CLEANING REPORT':^55}")
print("=" * 140)

for raw in raw_customers:
    cleaned = clean_customer_record(raw)
    print(f"\n     ID    :{cleaned['custumer_id']}")
    print(f" Name :  {cleaned['name']} ")
    print(f"  Email : {cleaned['email']} ")
    print(f"  Age : {cleaned['name']} ")
    print(f"  Revenue : {cleaned['revenue']} ")
    print(f"  Premium : {cleaned['is_premium']} ")
    print(f" Churn :  {cleaned['churn_risk']} ")
    print("    " + "-" * 140)


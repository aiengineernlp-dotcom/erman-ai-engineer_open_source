def evaluate_loan_qualification(applicant: dict[str, float]) -> dict[str, float]:
    age = int(applicant.get("age", 0))
    salary = float(applicant.get("salary", 0.0))
    credit_score = int(applicant.get("credit_score", 0))
    debt_ratio = float(applicant.get("debt_ratio", 1.0))
    employment_years = int(applicant.get("employment_years", 0))
    loan_amount = float(applicant.get("loan_amount", 0.0))

    # --HARD RULES (disqualification immetdiate)----

    if age < 18 or age > 75:
        return {"decision": "REJECTED", "reason": "Age out of range", "risk": 1.0}

    if credit_score < 500:
        return {"decision": "REJECTED", "reason": "credit score too low", "risk": 1.0}

    if debt_ratio > 0.6:
        return {"decision": "REJECTED", "reason": "debt ratio too high", "risk": 1.0}

    if employment_years < 2:
        return {"decision": "REJECTED", "reason": "employment years too small ", "risk": 1.0}

    if salary <= 0:
        return {"decision": "REJECTED", "reason": "No income declared ", "risk": 1.0}

    # --- SCORING RULES (accummulation de points---

    risk_score = 0.0

    # Scrore base sur le credit score

    if credit_score >= 750:
        risk_score -= 0.2
    if credit_score >= 650:
        risk_score += 0.1
    else:
        risk_score += 0.3

    # SCORE BASE SUR LE RAPPORT Ration salaire/pret

    loan_to_income = loan_amount / salary if salary > 0 else 10

    if loan_to_income < 3:
        risk_score -= 0.1
    elif loan_to_income < 5:
        risk_score += 0.1
    else:
        risk_score += 0.3

    # score base sur l'anciennete

    if employment_years >= 5:
        risk_score -= 0.1

    if employment_years < 2:
        risk_score += 0.2

    # score base sur le debit ratio

    risk_score += debt_ratio * 0.3

    # normalization 0-1
    risk_score = max(0.0, min(1.0, risk_score))

    # DECISION FINALE

    if risk_score < 0.3:
        decision = "APPROVED"
        reason = "Low risk profile"
    elif risk_score < 0.6:
        decision = "REVIEW"
        reason = "Medium  risk - review needed"
    else:
        decision = "REJECTED"
        reason = "HIGH RISK PROFILE"

    return {
        "decision": decision,
        "reason": reason,
        "risk": round(risk_score, 4)
    }


def display_results(name: str, result: dict) -> None:
    icons = {"APPROVED": "✅", "REVIEW": "⚠️", "REJECTED": "❌"}
    icon = icons.get(result["decision"], "?")
    print(f"\n    {icon} {name}")
    print(f"  Decision : {result['decision']}  ")
    print(f" Reason :{result['reason']}  ")
    print(f"  Risk :{result['risk']:.2%}  ")
    print(f"    ")


# Test avec plusieurs profils
applicants = [
    ("Alice Martin", {
        "age": 34, "salary": 75_000, "credit_score": 780,
        "debt_ratio": 0.25, "employment_years": 8,
        "loan_amount": 150_000
    }),
    ("Bob Chen", {
        "age": 26, "salary": 38_000, "credit_score": 610,
        "debt_ratio": 0.45, "employment_years": 1,
        "loan_amount": 200_000
    }),
    ("Carol Singh", {
        "age": 17, "salary": 20_000, "credit_score": 700,
        "debt_ratio": 0.2, "employment_years": 0,
        "loan_amount": 10_000
    }),
]

print("=" * 140)
print(f"     {'LOAN PRE-QUALIFICATION ENGINE':^55}")
print("=" * 140)

for name, data in applicants:
    result = evaluate_loan_qualification(data)
    display_results = (name, result)

    # print(result)
    print("\n")
    print(display_results)



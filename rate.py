#!/usr/bin/env python3
import argparse


def compute(net, tax_pct, expenses, buffer_pct, weeks_off, hours_per_week, billable_pct):
    tax = min(tax_pct, 80) / 100
    gross = (net / (1 - tax) + expenses) * (1 + buffer_pct / 100)
    weeks = max(52 - weeks_off, 1)
    billable_hours = weeks * hours_per_week * min(max(billable_pct, 1), 100) / 100
    rate = gross / billable_hours
    return {
        "hourly_rate": round(rate, 2),
        "revenue_needed_per_year": round(gross, 2),
        "billable_hours_per_year": round(billable_hours, 2),
        "day_rate_8h": round(rate * 8, 2),
        "project_10h": round(rate * 10, 2),
        "project_40h": round(rate * 40, 2),
    }


def main():
    p = argparse.ArgumentParser(
        prog="freelance-rate",
        description="Calculate the hourly rate you need to charge as a freelancer.",
    )
    p.add_argument("--net", type=float, required=True, help="Target take-home income per year")
    p.add_argument("--tax", type=float, default=25, help="Tax rate, percent (default 25)")
    p.add_argument("--expenses", type=float, default=0, help="Business expenses per year")
    p.add_argument("--buffer", type=float, default=10, help="Safety buffer, percent (default 10)")
    p.add_argument("--weeks-off", type=float, default=4, help="Unpaid weeks off per year (default 4)")
    p.add_argument("--hours-per-week", type=float, default=40, help="Working hours per week (default 40)")
    p.add_argument("--billable", type=float, default=70, help="Percent of hours that are billable (default 70)")
    p.add_argument("--json", action="store_true", help="Output as JSON")
    args = p.parse_args()

    r = compute(args.net, args.tax, args.expenses, args.buffer, args.weeks_off, args.hours_per_week, args.billable)

    if args.json:
        import json
        print(json.dumps(r, indent=2))
        return

    print(f"You should charge at least ${r['hourly_rate']:.2f} / hour\n")
    print(f"Revenue needed per year   {r['revenue_needed_per_year']:,.0f}")
    print(f"Billable hours per year   {r['billable_hours_per_year']:,.0f}")
    print(f"Day rate (8h)             {r['day_rate_8h']:,.2f}")
    print(f"10-hour project           {r['project_10h']:,.2f}")
    print(f"40-hour project           {r['project_40h']:,.2f}")


if __name__ == "__main__":
    main()

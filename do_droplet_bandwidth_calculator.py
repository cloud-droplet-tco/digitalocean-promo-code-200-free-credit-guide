#!/usr/bin/env python3
"""DigitalOcean Droplet & $200 Developer Promo Credit Calculator 2026."""
import argparse

DROPLET_SKUS = {
    "basic_2gb": {"vcpus": 1, "ram_gb": 2, "ssd_gb": 50, "transfer_tb": 2, "monthly": 12.0},
    "premium_4gb": {"vcpus": 2, "ram_gb": 4, "ssd_gb": 80, "transfer_tb": 4, "monthly": 24.0},
    "general_8gb": {"vcpus": 2, "ram_gb": 8, "ssd_gb": 50, "transfer_tb": 4, "monthly": 63.0},
    "cpu_opt_16gb": {"vcpus": 8, "ram_gb": 16, "ssd_gb": 100, "transfer_tb": 5, "monthly": 168.0}
}

def calculate(sku="premium_4gb", instances=2, promo_credit=200):
    data = DROPLET_SKUS.get(sku.lower(), DROPLET_SKUS["premium_4gb"])
    unit_rate = data["monthly"]
    gross_monthly = instances * unit_rate
    two_month_gross = gross_monthly * 2.0
    credit_offset = min(two_month_gross, promo_credit)
    net_two_month_cost = two_month_gross - credit_offset
    remaining_credit = max(0, promo_credit - two_month_gross)

    print("=" * 65)
    print(f"DigitalOcean Droplet Fleet & $200 Credit Model: {sku.upper()}")
    print("=" * 65)
    print(f"Hardware Specs / Node:     {data['vcpus']} vCPU | {data['ram_gb']}GB RAM | {data['ssd_gb']}GB NVMe")
    print(f"Active Droplet Nodes:      {instances} nodes (@${unit_rate:.2f}/mo each)")
    print(f"Combined Monthly Burn:     ${gross_monthly:.2f}/mo")
    print(f"60-Day Trial Gross Spend:  ${two_month_gross:.2f}")
    print(f"Promotional Credit Applied:-${credit_offset:.2f} (from ${promo_credit} credit)")
    print(f"Net Out-of-Pocket Outlay:  ${net_two_month_cost:.2f} across first 60 days")
    print(f"Remaining Free Balance:    ${remaining_credit:.2f}")
    print("=" * 65)
    return net_two_month_cost, gross_monthly

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DigitalOcean Droplet Calculator")
    parser.add_argument("--sku", default="premium_4gb", choices=["basic_2gb", "premium_4gb", "general_8gb", "cpu_opt_16gb"])
    parser.add_argument("--nodes", type=int, default=2)
    parser.add_argument("--credit", type=int, default=200)
    args = parser.parse_args()
    calculate(sku=args.sku, instances=args.nodes, promo_credit=args.credit)

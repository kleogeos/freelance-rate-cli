# freelance-rate-cli

![Test CLI](https://github.com/kleogeos/freelance-rate-cli/actions/workflows/test.yml/badge.svg)

Calculate the hourly rate you need to charge as a freelancer, given a target take-home income, taxes, expenses, time off, and how much of your time is actually billable. No dependencies, no sign-up — just Python 3.

```bash
python3 rate.py --net 60000 --tax 25 --expenses 2000 --weeks-off 4 --hours-per-week 40 --billable 70
```

```
You should charge at least $67.11 / hour

Revenue needed per year   90,200
Billable hours per year   1,344
Day rate (8h)             536.90
10-hour project           671.13
40-hour project           2,684.52
```

### Install (optional)

```bash
pip install git+https://github.com/kleogeos/freelance-rate-cli
freelance-rate --net 60000 --tax 25
```

### Options

| Flag | Default | Meaning |
|---|---|---|
| `--net` | required | Target take-home income per year |
| `--tax` | 25 | Tax rate, percent |
| `--expenses` | 0 | Business expenses per year |
| `--buffer` | 10 | Safety buffer, percent |
| `--weeks-off` | 4 | Unpaid weeks off per year |
| `--hours-per-week` | 40 | Working hours per week |
| `--billable` | 70 | Percent of hours that are actually billable (not admin/marketing/sales) |
| `--json` | off | Output as JSON instead of text |

## Why a CLI instead of a web app?

Same math as the [web calculator](https://kleogeos.github.io/freelancer-tools/rate-calculator.html), but scriptable — pipe `--json` output into a spreadsheet, a proposal generator, or re-run it for multiple scenarios without clicking through a form.

Prefer a browser form? Use the free web version: [rate calculator](https://kleogeos.github.io/freelancer-tools/rate-calculator.html) · [invoice generator](https://kleogeos.github.io/freelancer-tools/invoice.html)

Check a contract for missing clauses: [contract-checklist-cli](https://github.com/kleogeos/contract-checklist-cli) · Check if a crypto payment landed: [crypto-pay-cli](https://github.com/kleogeos/crypto-pay-cli)

Need the paperwork beyond pricing — proposals, contracts, invoices, late-payment emails, client scripts? [Freelancer Starter Kit ($15, pay with crypto)](https://kleogeos.github.io/freelancer-tools/kit.html)

Free and will stay free. If it saved you time: [tip with crypto](https://kleogeos.github.io/freelancer-tools/donate.html).

## License

MIT — do whatever you want with it.

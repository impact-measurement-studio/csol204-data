"""Validate csol204-data company files.

Usage:
    python tools/validate.py                 # check every company
    python tools/validate.py microsoft       # check one company
Exits with code 1 if any error is found. Warnings don't fail the check.
"""
import csv, sys, os, re
from collections import Counter

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "companies")

HEADERS = {
    "emissions.csv": ["company_slug", "reporting_entity", "period_label", "period_end", "period_type",
                      "scope", "scope3_category", "scope2_method", "status", "value_tco2e",
                      "value_original", "unit_original", "is_total", "restated", "method_note",
                      "source_doc", "source_url", "source_page", "source_quote"],
    "financials.csv": ["company_slug", "reporting_entity", "period_label", "period_end", "period_type",
                       "revenue_value", "currency", "unit_multiplier", "source_doc", "source_url",
                       "source_page", "source_quote"],
    "segments.csv": ["company_slug", "reporting_entity", "period_label", "split_type", "split_label",
                     "metric_type", "value", "unit", "additive", "source_doc", "source_url",
                     "source_page", "source_quote"],
}
STATUSES = {"reported", "not_relevant", "not_estimated", "not_disclosed"}
CATS = {str(i) for i in range(1, 16)} | {"total", ""}


def num(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


def check_company(slug):
    errs, warns = [], []
    folder = os.path.join(ROOT, slug)
    for fname, header in HEADERS.items():
        path = os.path.join(folder, fname)
        if not os.path.exists(path):
            errs.append(f"{slug}/{fname}: file missing")
            continue
        with open(path, newline="", encoding="utf-8") as f:
            try:
                rows = list(csv.reader(f, strict=True))
            except csv.Error as e:
                errs.append(f"{slug}/{fname}: CSV parse error: {e}")
                continue
        if not rows or rows[0] != header:
            errs.append(f"{slug}/{fname}: header doesn't match SCHEMA.md")
            continue
        for i, r in enumerate(rows[1:], start=2):
            if len(r) != len(header):
                errs.append(f"{slug}/{fname} line {i}: {len(r)} fields, expected {len(header)}")
                continue
            d = dict(zip(header, r))
            if d["company_slug"] != slug:
                errs.append(f"{slug}/{fname} line {i}: company_slug '{d['company_slug']}' != folder '{slug}'")
            if fname == "emissions.csv":
                if d["scope"] not in {"1", "2", "3"}:
                    errs.append(f"{slug}/{fname} line {i}: scope must be 1, 2 or 3")
                if d["status"] not in STATUSES:
                    errs.append(f"{slug}/{fname} line {i}: status '{d['status']}' not in {sorted(STATUSES)}")
                if d["scope"] == "2" and d["scope2_method"] not in {"location", "market"}:
                    errs.append(f"{slug}/{fname} line {i}: Scope 2 rows need scope2_method location or market")
                if d["scope"] == "1" and d["scope2_method"] not in {"", "market"}:
                    errs.append(f"{slug}/{fname} line {i}: Scope 1 rows leave scope2_method blank (or 'market' for a company's market-based Scope 1)")
                if d["scope"] == "3" and d["scope2_method"]:
                    errs.append(f"{slug}/{fname} line {i}: Scope 3 rows leave scope2_method blank")
                if d["scope"] == "3" and d["scope3_category"] not in CATS - {""}:
                    errs.append(f"{slug}/{fname} line {i}: Scope 3 rows need scope3_category 1-15 or total")
                if d["status"] == "reported":
                    if not num(d["value_tco2e"]):
                        errs.append(f"{slug}/{fname} line {i}: reported row needs a numeric value_tco2e")
                    if not d["source_page"] or not (d["source_url"] or d["source_doc"]):
                        errs.append(f"{slug}/{fname} line {i}: reported row needs source_doc/source_url and source_page")
                elif d["value_tco2e"]:
                    errs.append(f"{slug}/{fname} line {i}: status '{d['status']}' must have a blank value (missing is not zero)")
                if not re.match(r"^\d{4}-\d{2}-\d{2}$", d["period_end"] or ""):
                    warns.append(f"{slug}/{fname} line {i}: period_end should be YYYY-MM-DD")
            else:
                vcol = "revenue_value" if fname == "financials.csv" else "value"
                if not num(d[vcol]):
                    errs.append(f"{slug}/{fname} line {i}: {vcol} must be numeric")
                if not d["source_page"]:
                    errs.append(f"{slug}/{fname} line {i}: source_page missing")
        if fname == "emissions.csv" and len(rows) > 1:
            keys = Counter((r[1], r[2], r[5], r[6], r[7]) for r in rows[1:] if len(r) == len(header))
            for k, c in keys.items():
                if c > 1:
                    errs.append(f"{slug}/{fname}: duplicate row for entity/period/scope/category/method {k}")
    return errs, warns


def main():
    slugs = sys.argv[1:] or sorted(d for d in os.listdir(ROOT) if os.path.isdir(os.path.join(ROOT, d)))
    all_errs = 0
    for s in slugs:
        errs, warns = check_company(s)
        status = "OK" if not errs else f"{len(errs)} error(s)"
        print(f"{s}: {status}" + (f", {len(warns)} warning(s)" if warns else ""))
        for e in errs:
            print("  ERROR", e)
        for w in warns[:5]:
            print("  warn ", w)
        all_errs += len(errs)
    sys.exit(1 if all_errs else 0)


if __name__ == "__main__":
    main()

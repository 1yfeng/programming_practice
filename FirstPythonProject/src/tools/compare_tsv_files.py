"""
Compare two TSV files record by record, column by column.
Uses BscOfferHash as the primary key to match records between files.
Outputs a detailed comparison report.
"""

import csv
import sys
from collections import OrderedDict


def load_tsv(filepath):
    """Load a TSV file and return (headers, dict keyed by BscOfferHash)."""
    records = OrderedDict()
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        headers = reader.fieldnames or []
        for row in reader:
            key = row.get("BscOfferHash", "")
            records[key] = row
    return headers, records


def compare_files(origin_path, new_path):
    origin_headers, origin_records = load_tsv(origin_path)
    new_headers, new_records = load_tsv(new_path)

    # --- 1. Header comparison ---
    print("=" * 80)
    print("HEADER COMPARISON")
    print("=" * 80)
    if origin_headers == new_headers:
        print(f"  Headers match: {len(origin_headers)} columns")
    else:
        only_in_origin = set(origin_headers) - set(new_headers)
        only_in_new = set(new_headers) - set(origin_headers)
        if only_in_origin:
            print(f"  Columns only in Origin: {only_in_origin}")
        if only_in_new:
            print(f"  Columns only in New:    {only_in_new}")
    print()

    # --- 2. Record count ---
    print("=" * 80)
    print("RECORD COUNT")
    print("=" * 80)
    print(f"  Origin records: {len(origin_records)}")
    print(f"  New records:    {len(new_records)}")

    only_in_origin_keys = set(origin_records.keys()) - set(new_records.keys())
    only_in_new_keys = set(new_records.keys()) - set(origin_records.keys())
    common_keys = set(origin_records.keys()) & set(new_records.keys())
    print(f"  Common records: {len(common_keys)}")
    if only_in_origin_keys:
        print(f"  Only in Origin: {len(only_in_origin_keys)}")
        for k in only_in_origin_keys:
            print(f"    - {k}")
    if only_in_new_keys:
        print(f"  Only in New:    {len(only_in_new_keys)}")
        for k in only_in_new_keys:
            print(f"    - {k}")
    print()

    # --- 3. Column-by-column comparison for each common record ---
    # Use the union of headers for comparison
    all_headers = origin_headers if origin_headers == new_headers else list(
        OrderedDict.fromkeys(origin_headers + new_headers)
    )

    total_diffs = 0
    diff_summary_by_column = OrderedDict()  # column_name -> count of diffs
    for h in all_headers:
        diff_summary_by_column[h] = 0

    print("=" * 80)
    print("RECORD-BY-RECORD COMPARISON")
    print("=" * 80)

    for idx, key in enumerate(sorted(common_keys), 1):
        origin_row = origin_records[key]
        new_row = new_records[key]
        row_diffs = []

        for col in all_headers:
            origin_val = origin_row.get(col, "<MISSING>")
            new_val = new_row.get(col, "<MISSING>")
            if origin_val != new_val:
                row_diffs.append((col, origin_val, new_val))
                diff_summary_by_column[col] += 1
                total_diffs += 1

        # Print per-record result
        short_key = key[:16] + "..." if len(key) > 16 else key
        title = origin_row.get("Title", "")[:50]
        if row_diffs:
            print(f"\n  Record {idx} [BscOfferHash={short_key}] Title=\"{title}\"")
            print(f"  >> {len(row_diffs)} column(s) differ:")
            for col, ov, nv in row_diffs:
                ov_display = ov[:80] + "..." if len(ov) > 80 else ov
                nv_display = nv[:80] + "..." if len(nv) > 80 else nv
                print(f"     [{col}]")
                print(f"       Origin: {ov_display}")
                print(f"       New:    {nv_display}")
        else:
            print(f"\n  Record {idx} [BscOfferHash={short_key}] Title=\"{title}\"")
            print(f"  >> IDENTICAL (all {len(all_headers)} columns match)")

    # --- 4. Summary ---
    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"  Total records compared: {len(common_keys)}")
    print(f"  Total column differences: {total_diffs}")
    print()

    diff_cols = {k: v for k, v in diff_summary_by_column.items() if v > 0}
    if diff_cols:
        print("  Columns with differences:")
        print(f"  {'Column Name':<40} {'Diff Count':>10}")
        print(f"  {'-'*40} {'-'*10}")
        for col, count in diff_cols.items():
            print(f"  {col:<40} {count:>10}")
    else:
        print("  No differences found in any column!")

    match_cols = [k for k, v in diff_summary_by_column.items() if v == 0]
    print(f"\n  Columns fully matching: {len(match_cols)} / {len(all_headers)}")
    if diff_cols:
        print(f"  Columns with diffs:     {len(diff_cols)} / {len(all_headers)}")


if __name__ == "__main__":
    origin_file = r"d:\workspace\vs_workspace\data_workspace\BscOfferDataProcessor.OriginOfferBond.tsv"
    new_file = r"d:\workspace\vs_workspace\data_workspace\BscOfferDataProcessor.NewOfferBond.tsv"

    # Allow overriding via command line args
    if len(sys.argv) >= 3:
        origin_file = sys.argv[1]
        new_file = sys.argv[2]

    print(f"Origin: {origin_file}")
    print(f"New:    {new_file}")
    print()

    compare_files(origin_file, new_file)

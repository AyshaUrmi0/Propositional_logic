def print_truth_table():
    headers = ["p", "q", "not p", "p and q", "p or q", "p implies q", "p if and only if q"]
    print(" | ".join(headers))
    for p in [True, False]:
        for q in [True, False]:
            not_p = not p
            and_result = p and q
            or_result = p or q
            implies_result = (not p) or q
            equiv_result = p == q
            row = [str(p), str(q), str(not_p), str(and_result), str(or_result), str(implies_result), str(equiv_result)]
            print(" | ".join(row))

print_truth_table()

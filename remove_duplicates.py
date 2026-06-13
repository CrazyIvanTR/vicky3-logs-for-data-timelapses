seen = set()

with open("00-full-debug.txt", "r", encoding="utf-16") as f_in, open("00-full-debug-deduplicated.txt", "w", encoding="utf-16") as f_out:
    for ln in f_in:
        if ln not in seen:
            f_out.write(ln)
            seen.add(ln)

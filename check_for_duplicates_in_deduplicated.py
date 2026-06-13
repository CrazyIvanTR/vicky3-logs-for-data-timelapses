file_path = "00-full-debug-deduplicated.txt"

with open(file_path, "r", encoding="utf-16") as f:
    lines = [line.rstrip("\n") for line in f]

lines.sort(key=str.lower)

seen = set()
duplicates = set()

for line in lines:
    lowered = line.lower()
    if lowered in seen:
        duplicates.add(line)
    else:
        seen.add(lowered)

for dup in sorted(duplicates, key=str.lower):
    print(dup)

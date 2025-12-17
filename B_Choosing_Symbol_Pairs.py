from collections import Counter
S = input().strip()
count = Counter(S)
total_pairs = sum(v * v for v in count.values())
print(total_pairs)

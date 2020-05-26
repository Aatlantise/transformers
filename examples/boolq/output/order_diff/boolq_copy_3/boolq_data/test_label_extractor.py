
fi = open("test_matched.tsv", "r")
fo = open("test_matched_labels.tsv", "w")

first = True

for line in fi:
	parts = line.strip().split("\t")

	if first:
		headers = parts
		first = False

	else:
		fo.write(parts[headers.index("gold_label")] + "\n")



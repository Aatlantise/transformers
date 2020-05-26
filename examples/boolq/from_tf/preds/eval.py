import sys

fi_probs = open(sys.argv[1], "r")
fi_correct = open(sys.argv[2], "r")


correct = []
for line in fi_correct:
	correct.append(line.strip())

index = 0
right = 0
total = 0

for line in fi_probs:
	parts = line.strip().split("\t")

	p_c = float(parts[0])
	p_e = float(parts[1])

	if p_c > p_e:
		label = "contradiction"
	else:
		label = "entailment"

	if label == correct[index]:
		right += 1
	total += 1

	index += 1

print(right, total, right * 1.0 / total)

	




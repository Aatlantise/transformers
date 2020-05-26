from random import shuffle

fi_main = open("train_orig.tsv", "r")

fo = open("train.tsv", "w")

first = True

lines = []

for line in fi_main:
	if first:
		l1 = line
		first = False

	else:
		lines.append(line)

shuffle(lines)

fo.write(l1)

for line in lines:
	fo.write(line)


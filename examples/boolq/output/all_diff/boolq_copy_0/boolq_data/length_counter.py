import sys

#index	promptID	pairID	genre	sentence1_binary_parse	sentence2_binary_parse	sentence1_parse	sentence2_parse	sentence1	sentence2	label1	gold_label


import json_lines


def to_nli_labels(inp):
    if inp == True:
        return "entailment"
    elif inp == False:
        return "contradiction"
    else:
        print(inp)
        print(inp == "True")
        print(inp + "x")
        14/0


lengths = []
with open(sys.argv[1], 'rb') as f:
    for item in json_lines.reader(f):
        parts = ["blank" for i in range(12)]

        question = item['question']
        answer = item['answer']
        passage = item['passage']

        lenq = len(question.split())
        lenp = len(passage.split())
        total_len = lenq + lenp
        print(total_len)
        lengths.append(total_len)

        #print(item['answer'])

print(sorted(lengths)[::-1][:50])




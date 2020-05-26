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


fo = open(sys.argv[2], "w")

fo.write("index\tpromptID\tpairID\tgenre\tsentence1_binary_parse\tsentence2_binary_parse\tsentence1_parse\tsentence2_parse\tsentence1\tsentence2\tlabel1\tgold_label\n")



with open(sys.argv[1], 'rb') as f:
    for item in json_lines.reader(f):
        parts = ["blank" for i in range(12)]

        question = item['question']
        answer = item['answer']
        passage = item['passage']

        parts[8] = question
        parts[9] = passage
        parts[11] = to_nli_labels(answer)

        fo.write("\t".join(parts) + "\n") 

        #print(item['answer'])






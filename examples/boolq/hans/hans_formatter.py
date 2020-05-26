heuristic_list=["lexical_overlap", "subsequence", "constituent"]
subcase_list=["ln_subject_object_swap", "ln_preposition", "ln_relative_clause", "ln_passive", "ln_conjunction", "le_relative_clause", "le_around_prepositional_phrase", "le_around_relative_clause", "le_conjunction", "le_passive", "sn_NP/S", "sn_PP_on_subject", "sn_relative_clause_on_subject", "sn_past_participle", "sn_NP/Z", "se_conjunction", "se_adjective", "se_understood_object", "se_relative_clause_on_obj", "se_PP_on_obj", "cn_embedded_under_if", "cn_after_if_clause", "cn_embedded_under_verb", "cn_disjunction", "cn_adverb", "ce_embedded_under_since", "ce_after_since_clause", "ce_embedded_under_verb", "ce_conjunction", "ce_adverb"]





fi = open("qa_evaluation_set.txt", "r")
fo = open("dev_matched.tsv", "w")

def to_nli_labels(inp):
    if inp == "yes":
        return "entailment"
    elif inp == "no":
        return "contradiction"
    else:
        print(inp)
        print(inp == "True")
        print(inp + "x")
        
fo.write("gold_label\tsentence1_binary_parse\tsentence2_binary_parse2\tsentence1_parse\tsentence2_partse\tsentence1\tsentence2\tpairID\theuristic\tsubcase\ttemplate\n")

h = 0
s = 0

for n, line in enumerate(fi):
        item = line.strip().split("\t")

        parts = ["ba" for i in range(11)]

        question = item[1].lower()
        answer = item[2]
        passage = item[0]
        heuristic = heuristic_list[h]
        subcase = subcase_list[s]
	pairID = "ex" + str(n)

        parts[5] = question
        parts[6] = passage
        parts[7] = pairID
        parts[8] = heuristic
        parts[9] = subcase
        parts[0] = to_nli_labels(answer)

        fo.write("\t".join(parts) + "\n")
        
        if n % 10000 == 9999:
                h += 1
        if n % 1000 == 999:
                s += 1


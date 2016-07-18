def gene_search(total_gene, wanted_gene):
    large_gene = list(total_gene) #get total gene into an array of letters
    wanted = list(wanted_gene) #get wanted gene into an array of letters
    i = 0
    compared = []
    while len(wanted)+i<len(large_gene):
            if large_gene[i:len(wanted)+i] == wanted:
                    return True
            else:
                compared.append(large_gene[i:len(wanted)+i])
                try:
                    while large_gene[i:len(wanted)+i] in compared:
                        i+=1
                except ValueError:
                    i += len(wanted)
    return False


"""
searches linearly for a substring in a string. Boyer-Moore type of algorithm
Tests:
gene_search("ACCATGCA", "CAT") - True
gene_search("CATTGA", "CAT") - True
gene_search("CAAAT", "CAT") - False
gene_search("GGCACACATG", "CACAT") - True

"""

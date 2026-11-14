seq = input()
motiv = input()

f_index = seq.find(motiv)
l_index = seq.rfind(motiv)

print(seq[f_index + len(motiv):l_index])

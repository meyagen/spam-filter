from __future__ import division

total_msg = 260
correct = 0

bayes_output = open("results/bayes_output.txt", "r")
output = open("results/output.txt", "r")
results = open("results/correct/results.txt", "r")

blines = bayes_output.readlines()
olines = output.readlines()
rlines = results.readlines()

for i in range(260):
	owords = olines[i].split(" ")
	rwords = rlines[i].split(" ")
	bwords = blines[i].split(" ")

	if owords[0] == rwords[0] and owords[-1] == rwords[-1]:
		correct += 1
	else:
		print "Incorrect at", rwords[0], "\n", bwords[2], bwords[3], "\n"

print "Incorrect files:", 260-correct
print "Accuracy:", (correct/total_msg)*100, "%"

bayes_output.close()
output.close()
results.close()
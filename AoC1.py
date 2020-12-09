import AOCH


inputlist = AOCH.ril("input1-1")
inputlist = AOCH.stt(inputlist)

for i in range(0, len(inputlist)):
    for j in range(i+1, len(inputlist)):
        for k in range(j+1, len(inputlist)):
            if inputlist[i] + inputlist[j] + inputlist[k] == 2020:
                print([inputlist[i],inputlist[j],inputlist[k],inputlist[i]+inputlist[j]+inputlist[k],inputlist[i]*inputlist[j]*inputlist[k]])
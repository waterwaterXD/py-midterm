sa=list(input("sA:").split(" "))
sb=list(input("sB:").split(" "))
for i in range(len(sa)):
    if sa[i]in sb:
        print("子字串判斷為:yes")
    else:
        print("子字串判斷為:false")
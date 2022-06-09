n=int(input("請輸入筆數n:"))
dict1={}
for i in range(n):
    vocab=input(" ").split(" ")
    en=vocab[0]
    ch=vocab[1]
    dict1[en]=ch
ques=input("輸入欲查詢單字:")
if ques in dict1:
    print(ques,"中文意思為",dict1[ques])
else:
    print("字典未有此單字")
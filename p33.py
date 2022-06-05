


ch =int(input("國文:"))
en =int(input("英文:"))
ma =int(input("微積分:"))
pe =int(input("體育:"))
py=int(input("程式設計:"))
ave = (ch+en+ma+pe+py)/5
dict1={"國文":ch,"英文":en,"微積分":ma,"體育":pe,"程式設計":py}
max_dict1=max(dict1,key=dict1.get)
min_dict1=min(dict1,key=dict1.get)
print("平均分數:%3s"%(round(ave,3)))
print("最高分科目:",max_dict1,max(dict1.values()),"分")
print("最低分科目:",min_dict1,min(dict1.values()),"分")
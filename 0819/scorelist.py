scores= []
name = []
maxscores = 0
minscores = 100
total = 0
maxindex = 0
lists = ["TOM", "KAM", "JAM", "IAN", "YAN"]



     
for i in range(5):
    n = int(input("成績："))
    scores.append(n)
    
    if n > maxscores:
        maxscores = n
        maxindex = i
    if n < minscores:
        minscores = n
        maxindex = i
    total = total + n
    
s = total/len(scores)
print("總分：",total)
print("平均：",s)
print("最高分：",maxscores)
print("最低分：",minscores)
print(lists[maxindex],"是最高分",maxscores)

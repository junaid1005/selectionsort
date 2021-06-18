def selection(l):
    for i in range(len(l)-1):
        min=i
        for j in range(i+1 ,len(l)):
            if l[min]>l[j]:
                min=j
        if min!=i:
            l[i] ,l[min]=l[min] ,l[i]


a=input("Enter numbers").split()
a=list(map(int,a))
selection(a)
print(a)



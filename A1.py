def trees(n):
    tree=[]
    if n==0:
        return [""]
    if n==1:
        return["()"]
    else:
        for i in range(n):
            comb1=i
            comb2=n-i-1
            for t1 in trees(comb1):
                for t2 in trees(comb2):
                    for num in (0,len(t1)):
                        tree.append('('+t1[0:num+1]+t2+t1[num+1:len(t1)]+')')
        for t3 in trees(n-1):
            for nu in range(0,len(t3)-1):
                tree.append('('+t3[1:nu+1]+'()'+t3[nu+1:len(t3)-1]+')')
    return tree
    
def main():
    n=eval(input("n?"))
    a=set(trees(n))
    for tree in a:
      print(tree)

main()

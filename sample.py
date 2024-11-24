class solution:
    def sim(self,n1,n2):
        add  = n1+n2
        x = min(add)
        y = max(add)
        sol=(x+y)/2       
        print(sol)
if __name__ == "__main__":
    sol=solution()
    res = sol.sim(n1=[1,2,4],n2=[3])
    print(res)

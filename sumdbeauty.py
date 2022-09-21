class Solution:
    def calcBeauty(self,n,arr, s=0, e=0, b_arr=[]):
        if e == len(arr):
            return sum(b_arr)
        elif s > e:
            return self.calcBeauty(n, arr, 0, e+1, b_arr)
        else:
            subarr = arr[s:e+1]
            #print(subarr)
            b_arr.append(self.identify(subarr))
            return self.calcBeauty(n, arr, s+1, e, b_arr)
        
    # identify beauty
    def identify(self, subarr):
        d = {}
        for i in subarr:
            d[i] = d.get(i, 0) + 1
        vals = list(d.values())
        return vals.count(1)



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.calcBeauty(n,arr))
            
            T-=1


if __name__ == "__main__":
    main()
class Solution:
    def findNth(self,N):
        # code here
        if N<1: return N
        arr_func = [x for x in range(N+1)]
        for i in range(2 , N+1):
            if i%5 == 0:
                arr_func[i] = 11
            else:
                arr_func[i] = arr_func[i-1] + arr_func[i-2]
        val = (10**9) + 7
        
        return arr_func[N] %val


def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            
            ob=Solution()
            
            print(ob.findNth(n))
            
            T-=1


if __name__ == "__main__":
    main()
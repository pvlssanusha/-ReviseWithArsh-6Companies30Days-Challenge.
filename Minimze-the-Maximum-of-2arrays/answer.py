class Solution:
    answer=0
    def gcd(self,a,b):
        if(a%b==0):
            return b
        else:
            return gcd(b,a%b)
    def binarySearch(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int,low:int,high:int):
        mid=(low+high)//2
        if(low<=high):
            print("mid",mid)
            a=mid-(mid//divisor1)
            print(a)
            b=mid-(mid//divisor2)
            print(b)
            l=(divisor1*divisor2)//self.gcd(divisor1,divisor2)
            print("l",l)
            c=mid-(mid//divisor1)-(mid//divisor2) + (mid//l)
            print("c",c)
            if(a>=uniqueCnt1 and b>=uniqueCnt2 and a+b-c>=(uniqueCnt1+uniqueCnt2)):
                self.answer=mid
                print("ans",self.answer)
                answer=self.binarySearch(divisor1,divisor2,uniqueCnt1,uniqueCnt2,low,mid-1)

            else:
                self.binarySearch(divisor1,divisor2,uniqueCnt1,uniqueCnt2,mid+1,high)
            return self.answer
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        value=self.binarySearch(divisor1,divisor2,uniqueCnt1,uniqueCnt2,1,10**10)
        print("value",value)
        return value
        
        

        
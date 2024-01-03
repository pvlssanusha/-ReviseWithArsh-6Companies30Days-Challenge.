class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        dic={}
        high_access=[]
        for i in access_times:
            if i[0]  not in dic:
                dic.update({i[0]:[int(i[1])]})
            else:
                value=dic[i[0]]
                value.append(int(i[1]))
                value.sort()
                dic[i[0]]=value
        for i in dic:
            timelist=dic[i]
            for j in range(len(timelist)) :
                if j+2<len(timelist) and timelist[j+2]<=timelist[j]+99:
                    high_access.append(i)
                    break
        return high_access
        print(dic)



        
        
class Solution(object):
    def generateParenthesis(self, n):
        ans=[];
        allb=['(']
        def filterValid(str):
            right=0;
            left=0;
            for i in str:
                if (i=='('):left+=1;
                else: right+=1;
                if right>left: return False;
            if right==left: return True;
            else: return False;
        for i in range (n*2-1):
            newallb=[]
            for i in allb:
                newallb.append(i+')');
                newallb.append(i+'(');
            allb=newallb;
        for i in allb:
            if (filterValid(i)): ans.append(i);
        return ans;
class Solution(object):
    def myAtoi(self, s):
        numbers = ['1','2','3','4','5','6','7','8','9','0']
        isNegative = False;
        numberStarted = False;
        st=""
        if (s==""): return 0
        if(s[0] in numbers):
            st+=s[0];
            numberStarted=True;
        elif (s[0]=='-'): 
            st+='-';
            numberStarted=True;
        elif (s[0]==' '): True;
        elif (s[0] =='+'): numberStarted=True;
        elif (s[0]=='0'): 
            st+=s[0];
            numberStarted=True;
        else: 
            if (s[0] not in numbers): return 0;
        for i in range(1,len(s)):
            if (s[i] in numbers): st+=s[i];
            elif (s[i]==' ' and not numberStarted): True;
            elif (s[i]=='-' and not numberStarted): 
                st+=s[i];
                numberStarted=True;
            elif (s[i]=='+' and not numberStarted): 
                numberStarted=True;
            else: break
        if (st=="" or st=="-"): st="0"
        if (int(st)>2**31-1):return 2**31-1
        if (int(st)<-1*(2**31)):return -1*(2**31)
        return int(st);

                

        
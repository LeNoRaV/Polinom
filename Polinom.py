#import numpy as np
import copy
class Polinom:
    def __init__(self, coef_, value = 1):
        if type(coef_)==int or type(coef_)==float: 
            coef_list=[0 for i in range(coef_+1)]
            coef_list[-1]=value
            self.coef=coef_list
        else: self.coef = coef_

    def __init__(self, coef = []):
        self.coef = coef

    def __add__(self, other):
        sumy = []

        if type(other) != Polinom:
            other = Polinom([other])

        small = min(len(self.coef),len(other.coef))
        big = max(len(self.coef),len(other.coef))

        for i in range(small):
            sumy.append(self.coef[i]+other.coef[i])
        for i in range(small, big):
            if len(self.coef)>len(other.coef): sumy.append(self.coef[i])
            else: sumy.append(other.coef[i])
        return Polinom(sumy)

    def __radd__(self, other):
        sumy = []

        if type(other) != Polinom:
            other = Polinom([other])

        small = min(len(self.coef),len(other.coef))
        big = max(len(self.coef),len(other.coef))

        for i in range(small):
            sumy.append(self.coef[i]+other.coef[i])
        for i in range(small, big):
            if len(self.coef)>len(other.coef): sumy.append(self.coef[i])
            else: sumy.append(other.coef[i])
        return Polinom(sumy)

    def __sub__(self, other):
        sumy = []

        if type(other) != Polinom:
            other = Polinom([other])

        small = min(len(self.coef),len(other.coef))
        big = max(len(self.coef),len(other.coef))

        for i in range(small):
            sumy.append(self.coef[i]-other.coef[i])
        for i in range(small, big):
            if len(self.coef)>len(other.coef): sumy.append(self.coef[i])
            else: sumy.append(-other.coef[i])
        return Polinom(sumy)

    def __rsub__(self, other):
        sumy = []

        if type(other) != Polinom:
            other = Polinom([other])

        small = min(len(self.coef),len(other.coef))
        big = max(len(self.coef),len(other.coef))

        for i in range(small):
            sumy.append(-self.coef[i]+other.coef[i])
        for i in range(small, big):
            if len(self.coef)>len(other.coef): sumy.append(-self.coef[i])
            else: sumy.append(other.coef[i])
        return Polinom(sumy)
    
    def __mul__(self,other):
        if type(other)==Polinom:
            sumy=[]
            for i in range(len(self.coef)+len(other.coef)-1):
                sumy.append(0)
            for i in range(len(self.coef)):
                for j in range(len(other.coef)):
                    sumy[i+j]+=self.coef[i]*other.coef[j]
            return Polinom(sumy)

        elif type(other)==int:
            for i in range(len(self.coef)):
                self.coef[i] = self.coef[i] * other
            return self
        
    def __floordiv__(self,other):  
        res=Polinom([])
        while len(self.coef) >= len(other.coef):
            d = [0] * (len(self.coef) - len(other.coef)+1)
            d[len(self.coef) - len(other.coef)] = self.coef[len(self.coef)-1] / other.coef[len(other.coef)-1]
            prom = self - Polinom(d) * other
            prom.coef.pop(-1)
            res = res + Polinom(d)
            self.coef = prom.coef.copy()
        return res

    def __mod__(self, other):
        res=Polinom([])
        while len(self.coef) >= len(other.coef):
            d = [0] * (len(self.coef) - len(other.coef)+1)
            d[len(self.coef) - len(other.coef)] = self.coef[len(self.coef)-1] / other.coef[len(other.coef)-1]
            prom = self - Polinom(d) * other
            prom.coef.pop(-1)
            res = res + Polinom(d)
            self.coef = prom.coef.copy()
        return prom.coef[0]
    

    def find(self, x): # +
        ans=0
        for key, value in self.coef.items():
            ans += value*x**key
        return ans

    #def integral(self,a,b):
        #pass

    def __pow__(self, other):
        res = Polinom([1])
        if type(other) == int and other >= 0:
            for i in range(other, 0, -1):
                res = res * self
        return res
    
    def eval(self,dot):
        if type(dot) == int or type(dot) == float:
            return sum([self.coef[i]*dot**i for i in range(len(self.coef))])

    def __eq__(self,other):
        k = 1
        if len(self.coef) == len(other.coef):
            for i in range(len(self.coef)):
                if (self.coef[i] != other.coef[i]):
                    k = 0
        else:
            k = 0
        if k == 0:
            res = '!='
        else:
            res = '='
        return res
    
    def diff(self, order):
        while order > 0:
            if (len(self.coef)) == 2:
                return self.coef[1]
            else:
                res = [0] * (len(self.coef)-1)
                for i in range(len(self.coef)-1):
                    res[i] = self.coef[i+1] * (i + 1)
            order -= 1
            self.coef = res.copy()
        return Polinom(res) 
    
    def integrate(self, np, vp): 
        res = [0] * (len(self.coef)+1)
        for i in range(1, len(self.coef)+1):
            res[i] = self.coef[i - 1] / i
        return Polinom(res).eval(vp) - Polinom(res).eval(np)
    

    def __str__(self):
        ans=''
        flag=0

        if len(self.coef)==0: 
            ans='0'
            return ans
        
        k=0
        for i in range(len(self.coef)):
            if self.coef[i] != 0: k=1
        if k == 0:
            ans='0'

        if self.coef[0]!=0: ans+=str(self.coef[0])
        else: flag=1

        if self.coef[1]==1: ans+=str(' + '+'x')
        elif self.coef[1]==-1: ans+=str(' - '+'x')
        elif self.coef[1]>0: ans+=str(' + '+str(self.coef[1])+' '+'x')
        elif self.coef[1]<0: ans+=str(' - '+str(abs(self.coef[1]))+' '+'x')
        if flag==1 and self.coef[1]!=0: 
            if self.coef[1]<0: ans=ans[1:]
            else: ans=ans[3:]
            flag=0


        for i in range(2, len(self.coef)):
            if self.coef[i]==1: ans+=str(' + '+'x'+'^'+ str(i))
            elif self.coef[i]==-1: ans+=str(' - '+'x'+'^'+ str(i))
            elif self.coef[i]>0: ans+=str(' + '+str(self.coef[i])+' '+'x'+'^'+ str(i))
            elif self.coef[i]<0: ans+=str(' - '+str(abs(self.coef[i]))+' '+'x'+'^'+ str(i))
            if flag==1 and self.coef[i]!=0:
                if self.coef[1]<0: ans=ans[1:]
                else: ans=ans[3:]
                flag=0


        return ans

    def shift(self, other):
        if type(other) == int or type(other) == float:
            dot = Polinom([other,1])
            res = Polinom([])
            for i in range(len(self.coef)):
                res = res + dot**i * self.coef[i]
            
        return res
          

print(Polinom([]))
print(Polinom([0,1]))
print(Polinom([-1,0,1]))
print(Polinom([1,0,-1]))
print(Polinom([0,0,0,0,4]))
print('\n')

print('plus:', Polinom([1])+Polinom([0,1]))
print('min:', Polinom([1])-Polinom([0,1]))
print('mul:', Polinom([1,1])*Polinom([1,2]))
print('div:', Polinom([1,1,2])//Polinom([1,1]))
print('mod:', Polinom([1,1,2])%Polinom([1,1]))
print('pow:', Polinom([1,1])**4)
print('eq:', Polinom([1,1]), Polinom([1,1])==Polinom([1.0,1.0]), Polinom([1.0,1.0]))
print('ev:', Polinom([1,2]).eval(3))
print('diff:', Polinom([1,1,0,1]).diff(2))
print('int:', Polinom([1,1,1]).integrate(0,6))
print('sh:', Polinom([0,1,1]).shift(2))
print('\n')

one=Polinom([1])
x=Polinom([0,1])

print('one + x = ', one + x)
print('one - x = ', one - x)
print('x + one = ', x + one)
print('x - one = ', x - one)

p1 = 1 + x
p2 = 1 - x
print(p1*p2)
print(p1+p2)
print(p1-p2)
print(p2-p1)
print(p1**2)
print(p2**2)
print((p1*p2)**2)
print((p1*p2)**2 - p1**2 * p2**2)
print((p1**10 + 1) % p1)
print((x**10 - 1) % (x - 1))
print((x**10 - 1).diff(2))

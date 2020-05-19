import re

class calculator():
    def __init__(self, string):
        rpn = self.toRpn(string)
        print(rpn)
        rpn = rpn.split(' ')
        j = 0
        while j < len(rpn):
            if rpn[j]=='(' or rpn[j]==')':
                rpn.pop(j)
            j += 1
        self.result = self.operate(rpn)

    def toRpn(self, string):
        table = re.split(r' *([\+\-\*\^\(\)/]) *', string)
        i = 0
        while i < len(table):
            if table[i]=='':
                table.pop(i)
            i += 1
        print(table)
        tokens = [t for t in reversed(table) if t!='']
        print(tokens)
        precs = {'+':0 , '-':0, '/':1, '*':1, 'x':1, '^':2, '(':3, ')':3}

        def toRpn2(tokens, minprec):
            rpn = tokens.pop()

            while len(tokens)>0:
                try:
                    prec = precs[tokens[-1]]
                except KeyError:
                    prec = precs[tokens[-2]]
                
                if prec<minprec:
                    break
                op=tokens.pop()

                # get the argument on the operator's right
                # this will go to the end, or stop at an operator
                # with precedence <= prec
                arg2 = toRpn2(tokens,prec+1)
                rpn += " " + arg2 + " " +op
                print(rpn)
            return rpn
        
        return toRpn2(tokens, 0)

    def operate(self, rpn):
        i = 2
        print(rpn)
        limit = len(rpn)
        # print('taille+1: '+str(limit))
        if limit == 1:
            # print('fin du calcul, résultat: '+str(rpn[0]))
            return rpn[0]
        while i < limit:
            # print('position: '+str(i))
            if rpn[i] == '^':
                res = int(rpn[i-2]) ** int(rpn[i-1])
                # print(rpn[i-2]+' '+rpn[i-1])
                # print('res: '+str(res))
                rpn[i-2]=res
                rpn.pop(i-1)
                rpn.pop(i-1)
                return self.operate(rpn)

            if rpn[i]=='*' or rpn[i]=='/':
                if rpn[i] == '*':
                    res = int(rpn[i-2]) * int(rpn[i-1])
                    # print('res: '+str(res))
                    rpn[i-2]=res
                    rpn.pop(i-1)
                    rpn.pop(i-1)
                    return self.operate(rpn)
                if rpn[i] == '/':
                    res = int(rpn[i-2]) / int(rpn[i-1])
                    # print('res: '+str(res))
                    rpn[i-2]=res
                    rpn.pop(i-1)
                    rpn.pop(i-1)
                    return self.operate(rpn)

            if rpn[i]=='+' or rpn[i]=='-':
                if rpn[i] == '+':
                    res = int(rpn[i-2]) + int(rpn[i-1])
                    # print('res: '+str(res))
                    rpn[i-2]=res
                    rpn.pop(i-1)
                    rpn.pop(i-1)
                    return self.operate(rpn)
                if rpn[i] == '-':
                    res = int(rpn[i-2]) - int(rpn[i-1])
                    # print('res: '+str(res))
                    rpn[i-2]=res
                    rpn.pop(i-1)
                    rpn.pop(i-1)
                    return self.operate(rpn)
            i += 1
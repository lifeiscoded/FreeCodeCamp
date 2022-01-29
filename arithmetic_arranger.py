def arithmetic_arranger(Lst, ShowTotal = None):
    # ----- Definitions ------
    max_limit = 5
    err_max_msg = "Error : Too many problems"
    err_operator = "Error : Operator must be '+' of '-'"
    err_digit = "Error : Numbers must only contain digits"
    err_operand = "Error : Numbers cannot be more than four digits"
    op = ""
    lineList1 = []
    lineList2 = []
    LineListResult = []
    sepList = []
    # ------------------------
    
    if len(Lst) > max_limit:
        print(err_max_msg)
        return
    for t in Lst:
        item1 = "  "
        item2 = ""
        item3 = ""
        seperator = ""
        tmpList = []
        tm = t.replace(" ","")
        
        nCount = 0
        res = 0
        #Error Checks start
        # Is operator "+" or "-"
        if tm.find("+") != -1:
            tmpList = tm.split("+")
            op = "+"
        elif tm.find("-") != -1:
            tmpList = tm.split("-")
            op = "-"
        else:
            print(err_operator,"\nPlease correct :",t)
            return
        #Is digit or not?
        try:
            num1 = int(tmpList[0])
            num2 = int(tmpList[1])
            if op == "+":
                res = num1 + num2
            elif op == "-":
                res = num1 - num2
        except:
            print(err_digit,"\nPlease correct :",t)
            return
        #Is 4 digit
        if(num1 > 9999 or num2 > 9999):
            print(err_operand,"\nPlease correct :",t)
            return
        #Error Check end
                
        #Find number count and larger number
        if (len(tmpList[0].strip()) > len(tmpList[1].strip())):
            nCount = len(tmpList[0])
            item1 += tmpList[0]
            
            for i in range(nCount - len(tmpList[1])):
                item2 = item2 + " "
            item2 = item2 + tmpList[1]
                        
        else:
            nCount = len(tmpList[1])
            for i in range(len(tmpList[1]) - len(tmpList[0])):
                item1 += " "
            item1 = item1 + tmpList[0]
            
            item2 = item2 + tmpList[1]

        for i in range(nCount + 2):
            seperator += "-"
            
        if ShowTotal is True:
            for i in range(len(seperator) - len(str(res))):
                item3 += " "
            item3 += str(res)
        
        if Lst.index(t) != 3:
            lineList1.append(item1 + "    ")
            lineList2.append(op + " " + item2 + "    ")
            sepList.append(seperator + "    ")
            if ShowTotal is True: LineListResult.append(item3 + "    ")
        else:
            lineList1.append(item1)
            lineList2.append(op + " " + item2 )
            sepList.append(seperator)
            if ShowTotal is True: LineListResult.append(item3)
     
        result = ""
        for i in lineList1: result += i
        result += " \n"
        for i in lineList2: result += i
        result += " \n"
        for i in sepList: result += i
        result += " \n"
        for i in LineListResult: result += i
        
        
    
    print(result)

arithmetic_arranger(["3 + 82", "1 - 3801", "9990 + 9990", "523 - 49"], False)

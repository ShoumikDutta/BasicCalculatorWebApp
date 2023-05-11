def calc(num1,num2,btn):
    actions=["add","sub","mul","divi"]
  
    try:
        action=actions.index(btn)
    except:
        return "Wrong Action"
    if action==0:
        return num1+num2
    elif action==1:
        return num1-num2
    elif action==2:
        return num1*num2
    elif action==3:
        try:
            ans=float(float(num1)/num2)
        except:
            return "Can not devide by Zero"
        return ans
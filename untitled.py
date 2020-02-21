def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression POWER expression
                  | expression MODULO expression'''
    print("binop_reals")
    print(t[0], t[1], t[2], t[3])
    if t[2] == '+': 
        try:
            t[0] = t[1] + t[3]
        except:
            try :
                t[0] = t[1] + ' + ' + str(t[3])
            except:
                t[0] = str(t[1]) + ' + ' + t[3]
   

    elif t[2] == '-': 
        try:
            t[0] = t[1] - t[3]
        except:
            t[0] = t[1] + ' - ' + str(t[3])
   

    elif t[2] == '*': 
        if t[3] == 'i':
            t[0] = str(t[1]) + t[3]
        elif t[1] == 'i':
            t[0] = str(t[3]) + t[1] 
        else:
            t[0] = t[1] * t[3]
    

    elif t[2] == '%': t[0] = t[1] % t[3]
    elif t[2] == '^': t[0] = t[1] ** t[3]
    elif t[2] == '/': t[0] = float(t[1]) / float(t[3])

    # if t[0] % 1 == 0:
    #     t[0] = int(t[0])
    # else:
    #     t[0] = float(t[0])
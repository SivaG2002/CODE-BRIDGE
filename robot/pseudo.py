from textx.metamodel import metamodel_from_file
python_meta = metamodel_from_file('pseu.tx')
example_python_model = python_meta.model_from_file('input.txt')

class Python(object):

    # for testing the output of our model
    def _test_(self, model):
        for c in model.instruction:
            print (c)

    # we parse our code in this function
    def Instructions(self, model):

        show_declare = '\n'+'#you have not give values to these variables: '
        show_input = '\n'+'#you need to type in variable: '
        # we put the variables we have declared in the list, is easier to use and process
        declare_list = []
        input_list = []
        list_name = []  # save the list name
        need_value_list = []
        have_value_list = []
        list_already_have_value = []
        function_list = [] # save the function name which has been defined
        for_list = [] # specialized in for instruction
        if_num_ins = 0    # let us know the number of the if instruction
        for_num_1 = 0   # let us know the number of the for instruction
        error_for = 0   # let us konw if there is an error in for condition
        while_num_ins = 0
        indentation = ''

        for c in model.instruction:
            if c.__class__.__name__ == 'Declare_variable':
                var_declare = '{}'.format(c.variable.var)
                declare_list.append(var_declare)
                need_value_list.append(var_declare)

                # here we can show the user which variable they have declared
                #print ("//you have declared variable " + var_declare)
                print (indentation + var_declare+'= None')

            elif c.__class__.__name__ == 'Declare_value':
            # here we can assign the value to the variables we have declared
                var_value = '{}'.format(c.variable.var)
                if var_value not in declare_list:
                    print ('\n'+"#please declare the variable '"+var_value+"' first")
                else:
                    # isinstance function let us know the value we have assigned to the variable
                    # is a String or a integer or a float
                    if isinstance(c.value.val,int):
                        value = str(c.value.val)
                        if if_num_ins != 0:
                            print (indentation + var_value+' = '+value)
                        #elif for_num_1!=0:
                        #    print (indentation + var_value+' = '+value)
                        elif while_num_ins != 0:
                            print (indentation + var_value+' = '+value)
                        else:
                            print (indentation + var_value+' = '+value)
                        # we use the list to know which variable we have declared but not assigned value
                        if var_value not in have_value_list:
                            need_value_list.remove(var_value)
                            have_value_list.append(var_value)

                    elif isinstance(c.value.val,float):
                        value = str(c.value.val)
                        if if_num_ins != 0:
                            print (indentation + var_value+' = '+value)
                        #elif for_num_1!=0:
                        #    print (indentation + var_value+' = '+value)
                        elif while_num_ins != 0:
                            print (indentation + var_value+' = '+value)
                        else:
                            print (indentation + var_value+' = '+value)
                        # we use the list to know which variable we have declared but not assigned value
                        if var_value not in have_value_list:
                            need_value_list.remove(var_value)
                            have_value_list.append(var_value)

                    elif isinstance('{}'.format(c.value.val),str):
                        value = c.value.val
                        if value in declare_list:
                            print (indentation + var_value+' = '+value)
                        elif if_num_ins != 0:
                            print (indentation + var_value + " = '"+value+"'")
                        #elif for_num_1!= 0:
                            #print (indentation + var_value + " = '"+value+"'")
                        elif while_num_ins!= 0:
                            print (indentation + var_value + " = '"+value+"'")
                        else:
                            print (indentation + var_value+" = '"+(value)+"'")

                        if var_value not in have_value_list:
                            need_value_list.remove(var_value)
                            have_value_list.append(var_value)

                        else:
                            return

            elif c.__class__.__name__ == 'Print_words':
                content = '{}'.format(c.content.con)

                # we can use the list to help us know the variable we want to print is
                # a variable in our declare list or just a String
                if error_for!=0:
                    print("#please check the pseudocode of <for condition>")
                elif content in for_list:
                    print(indentation + 'print '+content)
                elif content in declare_list and input_list:
                    if if_num_ins != 0:
                        print (indentation + 'print '+ content)
                    elif for_num_1 != 0:
                        print (indentation + 'print '+ content)
                    elif while_num_ins != 0:
                        print (indentation + 'print '+ content)
                    else:
                        print (indentation + 'print '+ content)
                elif content in list_name:   # print list
                    if content in list_already_have_value:
                        if if_num_ins != 0:
                            print (indentation + 'print '+ content)
                        elif for_num_1 != 0:
                            print (indentation + 'print '+ content)
                        elif while_num_ins != 0:
                            print (indentation + 'print '+ content)
                        else:
                            print (indentation + 'print '+ content)
                    else:
                        if if_num_ins != 0:
                            # remind the user if the list is empty or not existed
                            print (indentation + 'print '+ content)
                            print ('# can not print empty list, please assign values first')
                        elif for_num_1 != 0:
                            print (indentation + 'print '+ content)
                            print ('# can not print empty list, please assign values first')
                        elif while_num_ins != 0:
                            print (indentation + 'print '+ content)
                            print ('# can not print empty list, please assign values first')
                        else:
                            print (indentation + 'print '+ content)
                            print ('# can not print empty list, please assign values first')

                elif content in declare_list not in input_list:
                    print ('\n'+'#'+content+' is a variable, please give a value before print.')
                else:
                    if if_num_ins != 0:
                        print (indentation + 'print "'+ content +'"')
                    elif for_num_1!= 0:
                        print (indentation + 'print "'+ content+'"')
                    elif while_num_ins!= 0:
                        print (indentation + 'print "'+ content+'"')
                    else:
                        print (indentation + 'print "'+ content +'"')

            elif c.__class__.__name__ == 'Print_string':
                content = '{}'.format(c.content_string.con)

                if if_num_ins != 0:
                    print (indentation + 'print '+'"'+content+'"')
                elif for_num_1 != 0:
                    print (indentation + 'print '+'"'+content+'"')
                elif while_num_ins != 0:
                    print (indentation + 'print '+'"'+content+'"')
                else:
                    print (indentation + 'print '+'"'+content+'"')

            elif c.__class__.__name__ == 'Print_variable':

                var_print = '{}'.format(c.variable.var)

                if if_num_ins != 0:
                    print (indentation + 'print '+''+var_print+'')
                elif for_num_1 != 0:
                    print (indentation + 'print '+''+var_print+'')
                elif while_num_ins != 0:
                    print (indentation + 'print '+''+var_print+'')
                else:
                    print (indentation + 'print '+''+var_print+'')

            elif c.__class__.__name__ == 'Calculation_instruction':

                var_o1 = '{}'.format(c.variable_op1.var_op1)
                var_o2 = '{}'.format(c.variable_op2.var_op2)
                calc = '{}'.format(c.calculation)
                right= '{}'.format(c.right)

                if calc == 'plus':
                    print (indentation + var_o1 + '+' + var_o2)
                elif calc == 'minus':
                    print (indentation + var_o1 + '-' + var_o2)
                elif calc == 'multiply':
                    print (indentation + var_o1 + '*' + var_o2)
                elif calc == 'divide':
                    print (indentation + var_o1 + '/' + var_o2)
                elif calc == 'power':
                    print (indentation + var_o1 + '**' + var_o2)
                else:
                    return;



            elif c.__class__.__name__ == 'If_startline':

                if if_num_ins == 0:
                    print ("#If instruction as below:")
                else:
                    if_num_ins = if_num_ins

                a = 0   # use a variable to know the two variables in IF are all declared
                if_num_ins = if_num_ins + 1  # let us know this is which if instruction
                variable_o1 = '{}'.format(c.expression1.variable_op1.var_op1)
                variable_o2 = '{}'.format(c.expression1.variable_op2.var_op2)
                comparasion_symbol = '{}'.format(c.expression1.comparasion)
                logic_operator = '{}'.format(c.expression1.logic)

                if variable_o1 in have_value_list:
                    a = a + 1
                elif variable_o1 in declare_list:
                    print ("#" + variable_o1 + " is not a valued variable, please give a value first.")
                else:
                    print ("#" + variable_o1 + " is not a declared variable, please declare first.")

                if variable_o2 in have_value_list:
                    a = a + 1
                elif variable_o2 in declare_list:
                    print ("#" + variable_o2 + " is not a valued variable, please give a value first.")
                else:
                    print ("#" + variable_o2 + " is not a declared variable, please declare first.")

                if a == 2:

                    # comparasion in if instruction
                    if comparasion_symbol == 'is greater than':
                        print (indentation + "if " + variable_o1 + " > " + variable_o2 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                    elif comparasion_symbol == 'is lower than':
                        print (indentation + "if " + variable_o1 + " < " + variable_o2 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                    elif comparasion_symbol == 'is more equal':
                        print (indentation + "if " + variable_o1 + " >= " + variable_o2 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                    elif comparasion_symbol == 'is less equal':
                        print (indentation + "if " + variable_o1 + " <= " + variable_o2 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                    elif comparasion_symbol == 'is equal to':
                        print (indentation + "if " + variable_o1 + " == " + variable_o2 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                    elif comparasion_symbol == 'is different from':
                        print (indentation + "if " + variable_o1 + " != " + variable_o2 + ":" + "    #number " + str(if_num_ins) + " if instruction start")

                    # logic operator in if instruction
                    elif logic_operator == 'and':
                        print (indentation + "if " + variable_o1 + " and " + variable_o2 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                    elif logic_operator == 'or':
                        print (indentation + "if " + variable_o1 + " or " + variable_o2 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                    elif logic_operator == 'not':
                        print (indentation + "if " + variable_o1 + " not " + variable_o2 + ":" + "    #number " + str(if_num_ins) + " if instruction start")

                    indentation += '    '


            elif c.__class__.__name__ == 'If_mstartline':
                a = 0   # use a variable to know the two variables in IF are all declared
                variable_o1 = '{}'.format(c.expression1.variable_op1.var_op1)
                variable_o2 = '{}'.format(c.expression1.variable_op2.var_op2)
                comparasion_symbol = '{}'.format(c.expression1.comparasion)
                logic_symbol = '{}'.format(c.logic)

                variable_o3 = '{}'.format(c.expression2.variable_op3.var_op3)
                variable_o4 = '{}'.format(c.expression2.variable_op4.var_op4)
                comparasion_symbol2 = '{}'.format(c.expression2.comparasion)


                # we need to know the variables in the if instruction have been declared or not
                # if not we remind the user to declare, if yes we go into the next step
                if variable_o1 in have_value_list:
                    a = a + 1
                elif variable_o1 in declare_list:
                    print ("#" + variable_o1 + " is not a valued variable, please give a value first.")
                else:
                    print ("#" + variable_o1 + " is not a declared variable, please declare first.")

                if variable_o2 in have_value_list:
                    a = a + 1
                elif variable_o2 in declare_list:
                    print ("#" + variable_o2 + " is not a valued variable, please give a value first.")
                else:
                    print ("#" + variable_o2 + " is not a declared variable, please declare first.")

                if variable_o3 in have_value_list:
                    a = a + 1
                elif variable_o3 in declare_list:
                    print ("#" + variable_o2 + " is not a valued variable, please give a value first.")
                else:
                    print ("#" + variable_o2 + " is not a declared variable, please declare first.")

                if variable_o4 in have_value_list:
                    a = a + 1
                elif variable_o4 in declare_list:
                    print ("#" + variable_o2 + " is not a valued variable, please give a value first.")
                else:
                    print ("#" + variable_o2 + " is not a declared variable, please declare first.")

                indentation = indentation[:-4]


                # we use the symbol "a" to know if the two variables are both declared
                # if a=4, we go into the if instruction and print the python code
                if a == 4:
                    if comparasion_symbol == 'is greater than':
                        if comparasion_symbol2 == 'is greater than':
                            print (indentation + "if " + variable_o1 + ">" + variable_o2 +" "+ logic_symbol+" "+"if " + variable_o3 + "> " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is lower than':
                            print (indentation + "if " + variable_o1 + ">" + variable_o2 + " "+ logic_symbol+" "+"if  " + variable_o3 + "< " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is greater or equal':
                            print (indentation + "if " + variable_o1 + ">" + variable_o2 + " "+ logic_symbol+" "+"if  " + variable_o3 + ">= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is less or equal':
                            print (indentation + "if " + variable_o1 + ">" + variable_o2 + " "+ logic_symbol+" "+"if  " + variable_o3 + "<= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is equal to':
                            print (indentation + "if " + variable_o1 + ">" + variable_o2 +" "+ logic_symbol+" "+"if  " + variable_o3 + "== " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is not equal to':
                            print (indentation + "if " + variable_o1 + ">" + variable_o2 +" "+ logic_symbol+" "+"if  " + variable_o3 + "!= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")

                    elif comparasion_symbol == 'is lower than':
                        if comparasion_symbol2 == 'is greater than':
                            print (indentation + "if " + variable_o1 + "< " + variable_o2 +" "+ logic_symbol+" "+"if  " + variable_o3 + "> " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is lower than':
                            print (indentation + "if " + variable_o1 + "< " + variable_o2 +" "+ logic_symbol+" "+"if  " + variable_o3 + "< " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is greater or equal':
                            print (indentation + "if " + variable_o1 + "< " + variable_o2 +" "+ logic_symbol+" "+"if  " + variable_o3 + ">= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is less or equal':
                            print (indentation + "if " + variable_o1 + "< " + variable_o2 +" "+ logic_symbol+" "+"if  " + variable_o3 + "<= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is equal to':
                            print (indentation + "if " + variable_o1 + "< " + variable_o2 +" "+ logic_symbol+" "+"if  " + variable_o3 + "== " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is not equal to':
                            print (indentation + "if " + variable_o1 + "< " + variable_o2 +" "+ logic_symbol+" "+"if  " + variable_o3 + "!= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")

                    if comparasion_symbol == 'is greater or equal':
                        if comparasion_symbol2 == 'is greater than':
                            print (indentation + "if " + variable_o1 + ">= " + variable_o2 +" "+ logic_symbol+" "+"if  " + variable_o3 + "> " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is lower than':
                            print (indentation + "if " + variable_o1 + ">=" + variable_o2 +" "+ logic_symbol+" "+"if  " + variable_o3 + "< " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is greater or equal':
                            print (indentation + "if " + variable_o1 + ">=" + variable_o2 +" "+ logic_symbol+" "+"if  " + variable_o3 + ">= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is less or equal':
                            print (indentation + "if " + variable_o1 + ">=" + variable_o2 +" "+ logic_symbol+" "+"if  " + variable_o3 + "<= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is equal to':
                            print (indentation + "if " + variable_o1 + ">=" + variable_o2 +" "+ logic_symbol+" "+"if  " + variable_o3 + "== " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is not equal to':
                            print (indentation + "if " + variable_o1 + ">=" + variable_o2 +" "+ logic_symbol+" "+"if  " + variable_o3 + "!= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")

                    elif comparasion_symbol == 'is less or equal':
                        if comparasion_symbol2 == 'is greater than':
                            print (indentation + "if " + variable_o1 + "<= " + variable_o2 +" "+ logic_symbol+" "+"if  " + variable_o3 + "> " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is lower than':
                            print (indentation + "if " + variable_o1 + "<= " + variable_o2 +" "+ logic_symbol+" "+"if  " + variable_o3 + "< " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is greater or equal':
                            print (indentation + "if " + variable_o1 + "<= " + variable_o2 +" "+ logic_symbol+" "+"if  " + variable_o3 + ">= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is less or equal':
                            print (indentation + "if " + variable_o1 + "<=" + variable_o2 +" "+ logic_symbol+" "+"if  " + variable_o3 + "<= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is equal to':
                            print (indentation + "if " + variable_o1 + "<=" + variable_o2 +" "+ logic_symbol+" "+"if  " + variable_o3 + "== " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is not equal to':
                            print (indentation + "if " + variable_o1 + "<=" + variable_o2 +" "+ logic_symbol+" "+"if  " + variable_o3 + "!= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")

                    elif comparasion_symbol == 'is equal to':
                        if comparasion_symbol2 == 'is greater than':
                            print (indentation + "if " + variable_o1 + "== " + variable_o2 +" "+ logic_symbol+" "+"if  " + variable_o3 + "> " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is lower than':
                            print (indentation + "if " + variable_o1 + "== " + variable_o2 +" "+ logic_symbol+" "+"if  " + variable_o3 + "< " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is greater or equal':
                            print (indentation + "if " + variable_o1 + "== " + variable_o2 +" "+ logic_symbol+" "+"if  " + variable_o3 + ">= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is less or equal':
                            print (indentation + "if " + variable_o1 + "==" + variable_o2 +" "+ logic_symbol+" "+"if  " + variable_o3 + "<= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is equal to':
                            print (indentation + "if " + variable_o1 + "==" + variable_o2 +" "+ logic_symbol+" "+"if  " + variable_o3 + "== " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is not equal to':
                            print (indentation + "if " + variable_o1 + "==" + variable_o2 +" "+ logic_symbol+" "+"if  " + variable_o3 + "!= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")

                    elif comparasion_symbol == 'is not equal to':
                            if comparasion_symbol2 == 'is greater than':
                                print (indentation + "if " + variable_o1 + "!= " + variable_o2 +" "+ logic_symbol+" "+"if  " + variable_o3 + "> " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                            elif comparasion_symbol2 == 'is lower than':
                                print (indentation + "if " + variable_o1 + "!= " + variable_o2 +" "+ logic_symbol+" "+"if  " + variable_o3 + "< " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                            elif comparasion_symbol2 == 'is greater or equal':
                                print (indentation + "if " + variable_o1 + "!= " + variable_o2 + " "+ logic_symbol+" "+"if  " + variable_o3 + ">= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                            elif comparasion_symbol2 == 'is less or equal':
                                print (indentation + "if " + variable_o1 + "!=" + variable_o2 +" "+ logic_symbol+" "+"if  " + variable_o3 + "<= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                            elif comparasion_symbol2 == 'is equal to':
                                print (indentation + "if " + variable_o1 + "!=" + variable_o2 + " "+ logic_symbol+" "+"if  " + variable_o3 + "== " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                            elif comparasion_symbol2 == 'is not equal to':
                                print (indentation + "if " + variable_o1 + "!=" + variable_o2 +" "+ logic_symbol+" "+"if  " + variable_o3 + "!= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")

                elif c.__class__.__name__ == 'If_melifline':
                    a = 0   # use a variable to know the two variables in IF are all declared
                    variable_o1 = '{}'.format(c.expression1.variable_op1.var_op1)
                    variable_o2 = '{}'.format(c.expression1.variable_op2.var_op2)
                    comparasion_symbol = '{}'.format(c.expression1.comparasion)

                    variable_o3 = '{}'.format(c.expression2.variable_op3.var_op3)
                    variable_o4 = '{}'.format(c.expression2.variable_op4.var_op4)
                    comparasion_symbol2 = '{}'.format(c.expression2.comparasion)


                    # we need to know the variables in the if instruction have been declared or not
                    # if not we remind the user to declare, if yes we go into the next step
                    if variable_o1 in have_value_list:
                        a = a + 1
                    elif variable_o1 in declare_list:
                        print ("#" + variable_o1 + " is not a valued variable, please give a value first.")
                    else:
                        print ("#" + variable_o1 + " is not a declared variable, please declare first.")

                    if variable_o2 in have_value_list:
                        a = a + 1
                    elif variable_o2 in declare_list:
                        print ("#" + variable_o2 + " is not a valued variable, please give a value first.")
                    else:
                        print ("#" + variable_o2 + " is not a declared variable, please declare first.")

                    if variable_o3 in have_value_list:
                        a = a + 1
                    elif variable_o3 in declare_list:
                        print ("#" + variable_o2 + " is not a valued variable, please give a value first.")
                    else:
                        print ("#" + variable_o2 + " is not a declared variable, please declare first.")

                    if variable_o4 in have_value_list:
                        a = a + 1
                    elif variable_o4 in declare_list:
                        print ("#" + variable_o2 + " is not a valued variable, please give a value first.")
                    else:
                        print ("#" + variable_o2 + " is not a declared variable, please declare first.")

                    indentation = indentation[:-4]


                    # we use the symbol "a" to know if the two variables are both declared
                    # if a=4, we go into the if instruction and print the python code
                    if a == 4:
                        if comparasion_symbol == 'is greater than':
                            if comparasion_symbol2 == 'is greater than':
                                print (indentation + "elif " + variable_o1 + ">" + variable_o2 + " and "+"elif " + variable_o3 + "> " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " elif instruction start")
                            elif comparasion_symbol2 == 'is lower than':
                                print (indentation + "elif " + variable_o1 + ">" + variable_o2 + " and "+"elif  " + variable_o3 + "< " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " elif instruction start")
                            elif comparasion_symbol2 == 'is greater or equal':
                                print (indentation + "elif " + variable_o1 + ">" + variable_o2 + " and "+"elif  " + variable_o3 + ">= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " elif instruction start")
                            elif comparasion_symbol2 == 'is less or equal':
                                print (indentation + "elif " + variable_o1 + ">" + variable_o2 + " and "+"elif  " + variable_o3 + "<= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + "elif instruction start")
                            elif comparasion_symbol2 == 'is equal to':
                                print (indentation + "elif " + variable_o1 + ">" + variable_o2 + " and "+"elif  " + variable_o3 + "== " + variable_o4 + ":" + "    #number " + str(if_num_ins) + "elif instruction start")
                            elif comparasion_symbol2 == 'is not equal to':
                                print (indentation + "elif " + variable_o1 + ">" + variable_o2 + " and "+"elif  " + variable_o3 + "!= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + "elif instruction start")

                        elif comparasion_symbol == 'is lower than':
                            if comparasion_symbol2 == 'is greater than':
                                print (indentation + "elif " + variable_o1 + "< " + variable_o2 + " and "+"elif  " + variable_o3 + "> " + variable_o4 + ":" + "    #number " + str(if_num_ins) + "elif instruction start")
                            elif comparasion_symbol2 == 'is lower than':
                                print (indentation + "elif " + variable_o1 + "< " + variable_o2 + " and "+"elif  " + variable_o3 + "< " + variable_o4 + ":" + "    #number " + str(if_num_ins) + "elif instruction start")
                            elif comparasion_symbol2 == 'is greater or equal':
                                print (indentation + "elif " + variable_o1 + "< " + variable_o2 + " and "+"elif  " + variable_o3 + ">= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + "elif instruction start")
                            elif comparasion_symbol2 == 'is less or equal':
                                print (indentation + "elif " + variable_o1 + "< " + variable_o2 + " and "+"elif  " + variable_o3 + "<= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " elif instruction start")
                            elif comparasion_symbol2 == 'is equal to':
                                print (indentation + "elif " + variable_o1 + "< " + variable_o2 + " and "+"elif  " + variable_o3 + "== " + variable_o4 + ":" + "    #number " + str(if_num_ins) + "elif instruction start")
                            elif comparasion_symbol2 == 'is not equal to':
                                print (indentation + "elif " + variable_o1 + "< " + variable_o2 + " and "+"elif  " + variable_o3 + "!= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + "elif instruction start")

                        if comparasion_symbol == 'is greater or equal':
                            if comparasion_symbol2 == 'is greater than':
                                print (indentation + "elif " + variable_o1 + ">= " + variable_o2 + " and "+"elif  " + variable_o3 + "> " + variable_o4 + ":" + "    #number " + str(if_num_ins) + "elif instruction start")
                            elif comparasion_symbol2 == 'is lower than':
                                print (indentation + "elif " + variable_o1 + ">=" + variable_o2 + " and "+"elif  " + variable_o3 + "< " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                            elif comparasion_symbol2 == 'is greater or equal':
                                print (indentation + "elif " + variable_o1 + ">=" + variable_o2 + " and "+"elif  " + variable_o3 + ">= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                            elif comparasion_symbol2 == 'is less or equal':
                                print (indentation + "elif " + variable_o1 + ">=" + variable_o2 + " and "+"elif  " + variable_o3 + "<= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                            elif comparasion_symbol2 == 'is equal to':
                                print (indentation + "elif " + variable_o1 + ">=" + variable_o2 + " and "+"elif  " + variable_o3 + "== " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                            elif comparasion_symbol2 == 'is not equal to':
                                print (indentation + "elif " + variable_o1 + ">=" + variable_o2 + " and "+"elif  " + variable_o3 + "!= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")

                        elif comparasion_symbol == 'is less or equal':
                            if comparasion_symbol2 == 'is greater than':
                                print (indentation + "if " + variable_o1 + "<= " + variable_o2 + " and "+"elif  " + variable_o3 + "> " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                            elif comparasion_symbol2 == 'is lower than':
                                print (indentation + "if " + variable_o1 + "<= " + variable_o2 + " and "+"elif  " + variable_o3 + "< " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                            elif comparasion_symbol2 == 'is greater or equal':
                                print (indentation + "if " + variable_o1 + "<= " + variable_o2 + " and "+"elif  " + variable_o3 + ">= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                            elif comparasion_symbol2 == 'is less or equal':
                                print (indentation + "if " + variable_o1 + "<=" + variable_o2 + " and "+"elif  " + variable_o3 + "<= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                            elif comparasion_symbol2 == 'is equal to':
                                print (indentation + "if " + variable_o1 + "<=" + variable_o2 + " and "+"elif  " + variable_o3 + "== " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                            elif comparasion_symbol2 == 'is not equal to':
                                print (indentation + "if " + variable_o1 + "<=" + variable_o2 + " and "+"elif  " + variable_o3 + "!= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")

                        elif comparasion_symbol == 'is equal to':
                            if comparasion_symbol2 == 'is greater than':
                                print (indentation + "if " + variable_o1 + "== " + variable_o2 + " and "+"elif  " + variable_o3 + "> " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                            elif comparasion_symbol2 == 'is lower than':
                                print (indentation + "if " + variable_o1 + "== " + variable_o2 + " and "+"elif  " + variable_o3 + "< " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                            elif comparasion_symbol2 == 'is greater or equal':
                                print (indentation + "if " + variable_o1 + "== " + variable_o2 + " and "+"elif  " + variable_o3 + ">= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                            elif comparasion_symbol2 == 'is less or equal':
                                print (indentation + "if " + variable_o1 + "==" + variable_o2 + " and "+"elif  " + variable_o3 + "<= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                            elif comparasion_symbol2 == 'is equal to':
                                print (indentation + "if " + variable_o1 + "==" + variable_o2 + " and "+"elif  " + variable_o3 + "== " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                            elif comparasion_symbol2 == 'is not equal to':
                                print (indentation + "if " + variable_o1 + "==" + variable_o2 + " and "+"elif  " + variable_o3 + "!= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")

                        elif comparasion_symbol == 'is not equal to':
                                if comparasion_symbol2 == 'is greater than':
                                    print (indentation + "if " + variable_o1 + "!= " + variable_o2 + " and "+"elif  " + variable_o3 + "> " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                                elif comparasion_symbol2 == 'is lower than':
                                    print (indentation + "if " + variable_o1 + "!= " + variable_o2 + " and "+"elif  " + variable_o3 + "< " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                                elif comparasion_symbol2 == 'is greater or equal':
                                    print (indentation + "if " + variable_o1 + "!= " + variable_o2 + " and "+"elif  " + variable_o3 + ">= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                                elif comparasion_symbol2 == 'is less or equal':
                                    print (indentation + "if " + variable_o1 + "!=" + variable_o2 + " and "+"elif  " + variable_o3 + "<= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                                elif comparasion_symbol2 == 'is equal to':
                                    print (indentation + "if " + variable_o1 + "!=" + variable_o2 + " and "+"elif  " + variable_o3 + "== " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")
                                elif comparasion_symbol2 == 'is not equal to':
                                    print (indentation + "if " + variable_o1 + "!=" + variable_o2 + " and "+"elif  " + variable_o3 + "!= " + variable_o4 + ":" + "    #number " + str(if_num_ins) + " if instruction start")


            elif c.__class__.__name__ == 'If_elifline':

                a = 0   # use a variable to know the two variables in IF are all declared
                variable_o1 = '{}'.format(c.expression1.variable_op1.var_op1)
                variable_o2 = '{}'.format(c.expression1.variable_op2.var_op2)
                comparasion_symbol = '{}'.format(c.expression1.comparasion)
                logic_operator = '{}'.format(c.expression1.logic)

                # we use the if_num_ins to control the indentation
                # if we just have 1 if instruction, we don't need indentation for "if" but one "Tab" for other basic instructions
                # if we have 2 if instructions, we need one "Tab" for "if" and two "Tabs" for basic instructions
                # if we have more than 3 instructions, we use for loop to control the indentation


                # we need to know the variables in the if instruction have been declared or not
                # if not we remind the user to declare, if yes we go into the next step
                if variable_o1 in have_value_list:
                    a = a + 1
                elif variable_o1 in declare_list:
                    print ("#" + variable_o1 + " is not a valued variable, please give a value first.")
                else:
                    print ("#" + variable_o1 + " is not a declared variable, please declare first.")

                if variable_o2 in have_value_list:
                    a = a + 1
                elif variable_o2 in declare_list:
                    print ("#" + variable_o2 + " is not a valued variable, please give a value first.")
                else:
                    print ("#" + variable_o2 + " is not a declared variable, please declare first.")

                # we use the symbol "a" to know if the two variables are both declared
                # if a=2, we go into the if instruction and print the python code

                indentation = indentation[:-4]

                if a == 2:
                    # comparasion in if instruction
                    if comparasion_symbol == 'is greater than':
                        print (indentation + "elif " + variable_o1 + " > " + variable_o2 + ":")
                    elif comparasion_symbol == 'is lower than':
                        print (indentation + "elif " + variable_o1 + " < " + variable_o2 + ":")
                    elif comparasion_symbol == 'is more equal':
                        print (indentation + "elif " + variable_o1 + " >= " + variable_o2 + ":")
                    elif comparasion_symbol == 'is less equal':
                        print (indentation + "elif " + variable_o1 + " <= " + variable_o2 + ":")
                    elif comparasion_symbol == 'is equal to':
                        print (indentation + "elif " + variable_o1 + " == " + variable_o2 + ":")
                    elif comparasion_symbol == 'is different from':
                        print (indentation + "elif " + variable_o1 + " != " + variable_o2 + ":")

                    # logic operators in if instruction
                    elif logic_operator == 'and':
                        print (indentation + "elif " + variable_o1 + " and " + variable_o2 + ":")
                    elif logic_operator == 'or':
                        print (indentation + "elif " + variable_o1 + " or " + variable_o2 + ":")
                    elif logic_operator == 'not':
                        print (indentation + "elif " + variable_o1 + " not " + variable_o2 + ":")

                    indentation += '    '

            # if we detect the "else" we can jump directly into the basic instructions
            # but we still have to control the indentations
            elif c.__class__.__name__ == 'instruction_else':
                indentation = indentation[:-4]
                print (indentation + "else:")
                indentation += '    '

            # detected end if, we will finish the corresponding if instruction
            # and remind us which if instructgion has been ended
            elif c.__class__.__name__ == 'If_endline':

                print ("#number " + str(if_num_ins) + " if instruction finished")
                if_num_ins = if_num_ins - 1
                indentation = indentation[:-4]

            elif c.__class__.__name__ == 'While_startline':

                if while_num_ins == 0:
                    print ('\n' + "# while instruction as below:")
                else:
                    while_num_ins = while_num_ins

                a = 0   # use a variable to know the two variables in while are all declared
                while_num_ins = while_num_ins + 1  # let us know this is which while instruction
                variable_o1 = '{}'.format(c.expression1.variable_op1.var_op1)
                variable_o2 = '{}'.format(c.expression1.variable_op2.var_op2)
                comparasion_symbol = '{}'.format(c.expression1.comparasion)

                if variable_o1 in have_value_list:
                    a = a + 1
                elif variable_o1 in declare_list:
                    print ("#" + variable_o1 + " is not a valued variable, please give a value first.")
                else:
                    print ("#" + variable_o1 + " is not a declared variable, please declare first.")

                if variable_o2 in have_value_list:
                    a = a + 1
                elif variable_o2 in declare_list:
                    print ("#" + variable_o2 + " is not a valued variable, please give a value first.")
                else:
                    print ("#" + variable_o2 + " is not a declared variable, please declare first.")

                # we use the symbol "a" to know if the two variables are both declared
                # if a=2, we go into the if instruction and print the python code

                #indentation = indentation[:-4]
                if a == 2:
                    if comparasion_symbol == 'is greater than':
                        print(indentation + "while " + variable_o1 + ' ' + ">" + ' ' + variable_o2 + ":")
                    elif comparasion_symbol == 'is lower than':
                        print (indentation + "while " + variable_o1 + ' ' + "<" + ' ' + variable_o2 + ":")
                    elif comparasion_symbol == 'is more equal':
                        print (indentation + "while " + variable_o1 + ' ' + ">=" + ' ' + variable_o2 + ":")
                    elif comparasion_symbol == 'is less equal':
                        print (indentation + "while " + variable_o1 + ' ' + "<=" + ' ' + variable_o2 + ":")
                    elif comparasion_symbol == 'is equal to':
                        print (indentation + "while " + variable_o1 + ' ' + "==" + ' ' + variable_o2 + ":")
                    elif comparasion_symbol == 'is different from':
                        print (indentation + "while " + variable_o1 + ' ' + "!=" + ' ' + variable_o2 + ":")

                    indentation += '    '

            elif c.__class__.__name__ == 'While_instruction_endline':
                print("# The end of while")
                indentation = indentation[:-4]

            elif c.__class__.__name__ == 'While_mstartline':

                if while_num_ins == 0:
                    print ('\n' + "# while instruction as below:")
                else:
                    while_num_ins = while_num_ins

                a = 0   # use a variable to know the two variables in IF are all declared
                variable_o1 = '{}'.format(c.expression1.variable_op1.var_op1)
                variable_o2 = '{}'.format(c.expression1.variable_op2.var_op2)
                comparasion_symbol = '{}'.format(c.expression1.comparasion)
                logic_symbol = '{}'.format(c.logic)

                variable_o3 = '{}'.format(c.expression2.variable_op3.var_op3)
                variable_o4 = '{}'.format(c.expression2.variable_op4.var_op4)
                comparasion_symbol2 = '{}'.format(c.expression2.comparasion)


                # we need to know the variables in the if instruction have been declared or not
                # if not we remind the user to declare, if yes we go into the next step
                if variable_o1 in have_value_list:
                    a = a + 1
                elif variable_o1 in declare_list:
                    print ("#" + variable_o1 + " is not a valued variable, please give a value first.")
                else:
                    print ("#" + variable_o1 + " is not a declared variable, please declare first.")

                if variable_o2 in have_value_list:
                    a = a + 1
                elif variable_o2 in declare_list:
                    print ("#" + variable_o2 + " is not a valued variable, please give a value first.")
                else:
                    print ("#" + variable_o2 + " is not a declared variable, please declare first.")

                if variable_o3 in have_value_list:
                    a = a + 1
                elif variable_o3 in declare_list:
                    print ("#" + variable_o2 + " is not a valued variable, please give a value first.")
                else:
                    print ("#" + variable_o2 + " is not a declared variable, please declare first.")

                if variable_o4 in have_value_list:
                    a = a + 1
                elif variable_o4 in declare_list:
                    print ("#" + variable_o2 + " is not a valued variable, please give a value first.")
                else:
                    print ("#" + variable_o2 + " is not a declared variable, please declare first.")

                # we use the symbol "a" to know if the two variables are both declared
                # if a=4, we go into the if instruction and print the python code
                #indentation = indentation[:-4]
                if a == 4:
                    if comparasion_symbol == 'is greater than':
                        if comparasion_symbol2 == 'is greater than':
                            print (indentation + "while " + variable_o1 + ">" + variable_o2 +" "+ logic_symbol+" "+"while " + variable_o3 + "> " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is lower than':
                            print (indentation + "while " + variable_o1 + ">" + variable_o2 +" "+ logic_symbol+" "+"while  " + variable_o3 + "< " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is greater or equal':
                            print (indentation + "while " + variable_o1 + ">" + variable_o2 + " "+ logic_symbol+" "+"while  " + variable_o3 + ">= " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is less or equal':
                            print (indentation + "while " + variable_o1 + ">" + variable_o2 + " "+ logic_symbol+" "+"while  " + variable_o3 + "<= " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is equal to':
                            print (indentation + "while " + variable_o1 + ">" + variable_o2 +" "+ logic_symbol+" "+"while  " + variable_o3 + "== " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is not equal to':
                            print (indentation + "while " + variable_o1 + ">" + variable_o2 + " "+ logic_symbol+" "+"while  " + variable_o3 + "!= " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")

                    elif comparasion_symbol == 'is lower than':
                        if comparasion_symbol2 == 'is greater than':
                            print (indentation + "while " + variable_o1 + "< " + variable_o2 +" "+ logic_symbol+" "+"while  " + variable_o3 + "> " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is lower than':
                            print (indentation + "while " + variable_o1 + "< " + variable_o2 +" "+ logic_symbol+" "+"while  " + variable_o3 + "< " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is greater or equal':
                            print (indentation + "while " + variable_o1 + "< " + variable_o2 +" "+ logic_symbol+" "+"while  " + variable_o3 + ">= " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is less or equal':
                            print (indentation + "while " + variable_o1 + "< " + variable_o2 +" "+ logic_symbol+" "+"while  " + variable_o3 + "<= " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is equal to':
                            print (indentation + "while " + variable_o1 + "< " + variable_o2 +" "+ logic_symbol+" "+"while  " + variable_o3 + "== " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is not equal to':
                            print (indentation + "while " + variable_o1 + "< " + variable_o2 + " "+ logic_symbol+" "+"while  " + variable_o3 + "!= " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")

                    if comparasion_symbol == 'is greater or equal':
                        if comparasion_symbol2 == 'is greater than':
                            print (indentation + "while " + variable_o1 + ">= " + variable_o2 +" "+ logic_symbol+" "+"while  " + variable_o3 + "> " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is lower than':
                            print (indentation + "while " + variable_o1 + ">=" + variable_o2 + " "+ logic_symbol+" "+"while  " + variable_o3 + "< " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is greater or equal':
                            print (indentation + "while " + variable_o1 + ">=" + variable_o2 + " "+ logic_symbol+" "+"while  " + variable_o3 + ">= " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is less or equal':
                            print (indentation + "while " + variable_o1 + ">=" + variable_o2 + " "+ logic_symbol+" "+"while  " + variable_o3 + "<= " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is equal to':
                            print (indentation + "while " + variable_o1 + ">=" + variable_o2 +" "+ logic_symbol+" "+"while  " + variable_o3 + "== " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is not equal to':
                            print (indentation + "while " + variable_o1 + ">=" + variable_o2 + " "+ logic_symbol+" "+"while  " + variable_o3 + "!= " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")

                    elif comparasion_symbol == 'is less or equal':
                        if comparasion_symbol2 == 'is greater than':
                            print (indentation + "while " + variable_o1 + "<= " + variable_o2 + " "+ logic_symbol+" "+"while  " + variable_o3 + "> " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is lower than':
                            print (indentation + "while " + variable_o1 + "<= " + variable_o2 + " "+ logic_symbol+" "+"while  " + variable_o3 + "< " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is greater or equal':
                            print (indentation + "while " + variable_o1 + "<= " + variable_o2 + " "+ logic_symbol+" "+"while  " + variable_o3 + ">= " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is less or equal':
                            print (indentation + "while " + variable_o1 + "<=" + variable_o2 + " "+ logic_symbol+" "+"while  " + variable_o3 + "<= " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is equal to':
                            print (indentation + "while " + variable_o1 + "<=" + variable_o2 +" "+ logic_symbol+" "+"while  " + variable_o3 + "== " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is not equal to':
                            print (indentation + "while " + variable_o1 + "<=" + variable_o2 +" "+ logic_symbol+" "+"while  " + variable_o3 + "!= " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")

                    elif comparasion_symbol == 'is equal to':
                        if comparasion_symbol2 == 'is greater than':
                            print (indentation + "while " + variable_o1 + "== " + variable_o2 +" "+ logic_symbol+" "+"while  " + variable_o3 + "> " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is lower than':
                            print (indentation + "while " + variable_o1 + "== " + variable_o2 + " "+ logic_symbol+" "+"while  " + variable_o3 + "< " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is greater or equal':
                            print (indentation + "while " + variable_o1 + "== " + variable_o2 + " "+ logic_symbol+" "+"while  " + variable_o3 + ">= " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is less or equal':
                            print (indentation + "while " + variable_o1 + "==" + variable_o2 + " "+ logic_symbol+" "+"while  " + variable_o3 + "<= " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is equal to':
                            print (indentation + "while " + variable_o1 + "==" + variable_o2 + " "+ logic_symbol+" "+"while  " + variable_o3 + "== " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")
                        elif comparasion_symbol2 == 'is not equal to':
                            print (indentation + "while " + variable_o1 + "==" + variable_o2 +" "+ logic_symbol+" "+"while  " + variable_o3 + "!= " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")

                    elif comparasion_symbol == 'is not equal to':
                            if comparasion_symbol2 == 'is greater than':
                                print (indentation + "while " + variable_o1 + "!= " + variable_o2 +" "+ logic_symbol+" "+"while  " + variable_o3 + "> " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")
                            elif comparasion_symbol2 == 'is lower than':
                                print (indentation + "while " + variable_o1 + "!= " + variable_o2 + " "+ logic_symbol+" "+"while  " + variable_o3 + "< " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")
                            elif comparasion_symbol2 == 'is greater or equal':
                                print (indentation + "while " + variable_o1 + "!= " + variable_o2 + " "+ logic_symbol+" "+"while  " + variable_o3 + ">= " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")
                            elif comparasion_symbol2 == 'is less or equal':
                                print (indentation + "while " + variable_o1 + "!=" + variable_o2 + " "+ logic_symbol+" "+"while  " + variable_o3 + "<= " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")
                            elif comparasion_symbol2 == 'is equal to':
                                print (indentation + "while " + variable_o1 + "!=" + variable_o2 +" "+ logic_symbol+" "+"while  " + variable_o3 + "== " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")
                            elif comparasion_symbol2 == 'is not equal to':
                                print (indentation + "while " + variable_o1 + "!=" + variable_o2 + " "+ logic_symbol+" "+"while  " + variable_o3 + "!= " + variable_o4 + ":" + "    #number " + str(while_num_ins) + " if instruction start")

                    indentation += '    '


pyth = Python()
pyth.Instructions(example_python_model)

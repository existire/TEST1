"""
Postcode generator
Lukasz Szulc
lukasz.szulc@op.pl

The function gets 2 variables:
x = start postcode in string format 'xx-xxx'
y = end postcode in string format 'yy-yyy'
return and print the list of postcodes in string format.
"""


def postcode_gen(x, y):
    x_list = list(map(int, x.split("-")))
    y_list = list(map(int, y.split("-")))
    main_code_differ = y_list[0] - x_list[0] + 1
    postcode_list_x =[]
    postcode_list_y =[]
    for i in range(main_code_differ):
        if (i+1) == 1 and x_list[0] == y_list[0]:
            while x_list[1] <= y_list[1]:
                if len(str(x_list[1])) < 2:
                    print("00" + str(x_list[1]))
                    postcode_list_x.append(str(x_list[0]) + "-" + "00" + str(x_list[1]))
                elif len(str(x_list[1])) < 3:
                    print("0" + str(x_list[1]))
                    postcode_list_x.append(str(x_list[0]) + "-" + "0" + str(x_list[1]))
                else:
                    postcode_list_x.append(str(x_list[0]) + "-" + str(x_list[1]))
                x_list[1] = x_list[1] + 1
        elif (i+1) == 1:
            while x_list[1] <= 999:
                if len(str(x_list[1])) < 2:
                    print("00" + str(x_list[1]))
                    postcode_list_x.append(str(x_list[0]) + "-" + "00" + str(x_list[1]))
                elif len(str(x_list[1])) < 3:
                    print("0" + str(x_list[1]))
                    postcode_list_x.append(str(x_list[0]) + "-" + "0" + str(x_list[1]))
                else:
                    postcode_list_x.append(str(x_list[0]) + "-" + str(x_list[1]))
                x_list[1] = x_list[1] + 1
        elif (i + 1) > 1 and ((i + 1) < main_code_differ):
            x_list[1] = 0
            while x_list[1] <= 999:
                if len(str(x_list[1])) < 2:
                    postcode_list_x.append(str(x_list[0]+i) + "-" + "00" + str(x_list[1]))
                elif len(str(x_list[1])) < 3:
                    postcode_list_x.append(str(x_list[0]+i) + "-" + "0" + str(x_list[1]))
                else:
                    postcode_list_x.append(str(x_list[0]+i) + "-" + str(x_list[1]))
                x_list[1] = x_list[1] + 1
        else:
            while y_list[1] >= 0:
                if len(str(y_list[1])) < 2:
                    postcode_list_y.insert(0, str(y_list[0]) + "-" + "00" + str(y_list[1]))
                elif len(str(y_list[1])) < 3:
                    postcode_list_y.insert(0, str(y_list[0]) + "-" + "0" + str(y_list[1]))
                else:
                    postcode_list_y.insert(0, str(y_list[0]) + "-" + str(y_list[1]))
                y_list[1] = y_list[1] - 1

    print(*(postcode_list_x + postcode_list_y), sep="\n")
    #print(postcode_list_x + postcode_list_y)
    return(postcode_list_x + postcode_list_y)


postcode_gen("79-900", "80-155")
def bordsetting(introverte, ekstroverte):
    # out_list = []
    # for i in range(len(ekstroverte)):
    #     out_list.append(introverte[i])
    #     out_list.append(ekstroverte[i])
    # return out_list

    out_list = []
    while introverte != []:
        out_list.append(introverte.pop())
        out_list.append(ekstroverte.pop())
    return out_list


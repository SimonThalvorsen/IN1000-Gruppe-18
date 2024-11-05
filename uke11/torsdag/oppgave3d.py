def lag_interessegrupper(personers_interesser):
    out_dict = {}
    
    for navn in personers_interesser:
        interesse = personers_interesser[navn]
        if interesse in out_dict:
            out_dict[interesse].append(navn)
        else:
            out_dict[interesse] = [navn]
            # out_dict[interesse] = []
            # out_dict[interesse].append(navn)

    return out_dict

def clean_list_using_loop(dirty_list):
    # Funkce, která vrátí list bez duplicitních dat z listu na vstupu s použitím smyčky.

    clean_list = []
    [clean_list.append(x) for x in dirty_list if x not in clean_list]
    return clean_list


def clean_list_using_set(dirty_list):
    # Funkce, která vrátí list bez duplicitních dat z listu na vstupu s použitím množiny (set).

    return list(set(dirty_list))
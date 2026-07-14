def search(var,element):
    #step1 : sorted structure ?
    sorted_var = var.sort()

    #step2 : finfthe mid value :
    mid_index = len(sorted_var) // 2

    #step3 : check the condition :
    if sorted_var[mid_index] < element:
        #this is to check for the right structure

        search(sorted_var[mid_index : ],element)

    elif sorted_var[mid_index] > element:
        #this is to check for the left structure

        search(sorted_var[ : mid_index+1],element)

    else:
        print(f'{element} found on the index {mid_index}')
        
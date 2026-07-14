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


#....................................................................................................      


def search(var, element):

    var.sort()          

    low = 0
    high = len(var) - 1

    while low <= high:

        mid = (low + high) // 2

        if var[mid] == element:
            print(f"{element} found at index {mid}")
            return

        elif var[mid] < element:
            low = mid + 1

        else:
            high = mid - 1

    print("Element not found")

numbers = [10, 2, 8, 15, 5, 20]
search(numbers, 15)





from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    print("Hello World")
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    result_list = []
    counter = 0
   
    while counter < len(USERS):
        match_bool = False
        if args.get('id') == USERS[counter].get('id'):
            match_bool = True
            
        if args.get('name', "N/A").lower() in USERS[counter].get('name').lower():
            match_bool = True
            
        if int(args.get('age', 0)) in range( int(USERS[counter].get('age')) - 1, int(USERS[counter].get('age')) + 2):
            match_bool = True
            
        if args.get('occupation', "N/A").lower() in USERS[counter].get('occupation').lower():
            match_bool = True
            
        if match_bool == True:
            result_list.append(USERS[counter])
        counter += 1

    #sort
    sorted_list = []
    sorted_list_temp = result_list.copy()
    num = int(len(result_list))
    loop_sort = 0
    
    while loop_sort < num:
        counter2 = 0
        while counter2 < len(sorted_list_temp):
            if args.get('id') == sorted_list_temp[counter2].get('id'):
                sorted_list.append(sorted_list_temp[counter2])
                sorted_list_temp.pop(counter2)
                break
            counter2 +=1
        loop_sort +=1
        
    loop_sort = 0

    while loop_sort < num:       
        counter2 = 0
        while counter2 < len(sorted_list_temp):
            if args.get('name', "N/A").lower() in sorted_list_temp[counter2].get('name').lower():
                sorted_list.append(sorted_list_temp[counter2])
                sorted_list_temp.pop(counter2)
                break
            counter2 +=1
        loop_sort +=1
        
    loop_sort = 0

    while loop_sort < num:        
        counter2 = 0
        while counter2 < len(sorted_list_temp):
            if int(args.get('age', 0)) in range( int(sorted_list_temp[counter2].get('age')) - 1, int(sorted_list_temp[counter2].get('age')) + 2):
                sorted_list.append(sorted_list_temp[counter2])
                sorted_list_temp.pop(counter2)
                break
            counter2 +=1
        loop_sort +=1

    loop_sort = 0
    
    while loop_sort < num:         
        counter2 = 0
        while counter2 < len(sorted_list_temp):
            if args.get('occupation', "N/A").lower() in sorted_list_temp[counter2].get('occupation').lower():
                sorted_list.append(sorted_list_temp[counter2])
                sorted_list_temp.pop(counter2)
                break
            counter2 +=1

        loop_sort +=1
        
    if args:
        return sorted_list
    return USERS




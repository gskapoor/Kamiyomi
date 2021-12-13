import manganelo


def init():
    print("Initializing Manga File")
    try:
        f = open("mangalist.txt", "a")
        print("mangalist.txt found, now entering manage mode")
    except:
        print("mangalist.txt not found, creating new mangalist")
        f = open("mangalist.txt", "w")
    print("\n\n\n\n\n")
    print("Kamiyomi AlphaV1 is licensed under the GNU Public License V3")
    print("I don't know what that means, but it's not my problem")
    print("\n\n\n\nType 'help' for help with commands")
    f.close()

    return True

def add(command):
    # TODO add the adder function and implement in scan.py

    if len(command) < 3:
        print("Invalid length, returning null")
        return False
    
    if command[1] == "url":
        add_url(command[2])
    elif command[1] == "name":
        add_nam(command)
    else:
        print("Command modifier '", command[1], "'invalid")
        print("Please use either 'url' for urls or 'name' for manga names")
    
    return True


def add_url(command):
    f = open("mangalist.txt", "a")
    try:
        print("Manga ", manganelo.get_story_page(url = command).title, "successfully added")
        f.write(command + "\n")
    except:
        print("Invalid URL error, please try again with a different URL")
    return True


def add_nam(command):
    #TODO complete function
    '''
    k = 0
    found = False
    while found == False:
        res = manganelo.search(command[2])
        for r in res:
            print(r.title, r.views)
        if k + 5 > len(res):
            found = True
        iter_list = res[0+k:4+k]
        for j,i in enumerate(iter_list):
            print("Manga #", j+1,": ", i.title)
        user_sorc = input("Insert number if manga found or something else if not found")
        if user_sorc in ["1","2","3","4","5"]:
            add_url(iter_list[int(user_sorc)])
            found = True
        k += 5
    '''
    print("Please use url, function unavailible at this time")
    return


def delr(command):
    #TODO add the remover function
    return


def helpr():
    #TODO support per command help statements
    print("Commands")
    print("'add' - adds manga to file")
    print("'del' - removes manga from file")
    print("'exit' - allows you to escape from my program :D7")
    


def main():
    init()
    no_exit = True

    while no_exit:
        c = input(":D> ")

        c = c.split()

        if c[0] == "add":
            add(c)
        elif c[0] == "del":
            delr(c)
        elif c[0] == "exit":
            no_exit = False
        elif c[0] == "help":
            helpr()
        else:
            print("No command found")
        


################
main()

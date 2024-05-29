def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return
    happy_new_year()
    
    print("Happy New Year!")
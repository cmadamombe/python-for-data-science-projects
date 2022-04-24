#
# Example file for working with loops
# LinkedIn Learning Python course by Joe Marini
#


def main():
    x = 0

    # # TODO: define a while loop
    # while(x < 11):
    #     print(x)
    #     x+= 1

    # # # TODO: define a for loop
    # for x in range(0,11):
    #     print(x)


    # TODO: use a for loop over a collection
    years = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
    for y in years:
        if y == 'January':
            break
        print(y)

    # TODO: use the break and continue statements
    years = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
    for y in years:
        if y == 'January':
            break
        print(y)


    # TODO: using the enumerate() function to get index 
    years = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
    for i,y in enumerate(years):
        print(i,y)

  
if __name__ == "__main__":
    main()

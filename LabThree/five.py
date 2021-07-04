'''
 Write a function called show_stars(rows).If rows is 5, it should print the following:
 *
 **
 ***
 ****
 *****
'''
def show_stars():
    for row in range(5):
        for col in range(row + 1):
            print('*', end=' ')
        print()
show_stars()

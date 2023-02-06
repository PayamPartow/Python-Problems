import time as t
from os import path


def createFile(dest):
    '''
  the script creates a text file at the passed in location,
  names file based on date

    '''

    date = t.localtime(t.time())  # grab the current time and convert to usable format
    list_of_names = []
    for i in range(5):  # creating a loop to create five files with different names
        list_of_names.append('file' + str(i) + '.c')
    # name = '%d_%d_%d.c' % (date[1], date[2], (date[0] % 100))  # fileName = month_day_year.txt format
    # just want to get the last two digits of the year hence we did %100
    for i in range(5):
        if not (path.isfile(dest + list_of_names[i])):  # if the file does not exist create the file
            f = open(dest + list_of_names[i], 'w')  # creates the file in a writable format hence the 'w'
            f.write('hello!')  # write a new line 30 times
            f.close()


if __name__ == '__main__':  # if this file is the main file that's being run then call the createfile function
    destination = '//Users//payampartow//Documents//Python-Problems//'
    createFile(destination)
    input("done!")

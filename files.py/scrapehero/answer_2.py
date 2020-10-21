def find_duplicates():
    number = 0
    comparing_file = 1  
    file = "/home/akshays/Downloads/Compressed/data/" + number + ".txt"
    comparingfile = "/home/akshays/Downloads/Compressed/data/" + comparing_file + ".txt"
   
    with open(file) as fp:
        for line in fp:
            print(line)
            with open(comparingfile) as fp1:
                for line1 in fp1:
                    line1 = line1.rstrip()
                    if line == line1:
                        print (line1 + "Ip is Already Present")
                    else:
                        print ("Processing Ip:"+ line)



    return 0 
   
if __name__ == '__main__':
    result = find_duplicates()
    for row in result:
        print(" ".join(str(i) for i in row))
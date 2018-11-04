from creat_base import BDD 
import file_thread as ft
def loader():   
    path = ft.pwd() + "//..//file"
    print(path)
    way = ft.ls(path)
    return way,path

def main():
    B = BDD()
    direfile = loader()
    for filename in direfile[0]:
        
        try:
            new_line = ""
            file = direfile[1] + "//" + filename
            text = ft.my_open(file)
            text_line = parser(text)
            for line in text_line:
                res = ""
                for i in B.request(line):
                    res += str(i) + '\n'
                new_line += line + '\n' + res + '\n'
            new_name = direfile[1] + "\\..\\res//" + filename[0:-4] + "_c.txt"
            ft.my_write( new_name , new_line)
            print(filename + " succesfully threat " + filename[0:-4] + "_c.txt" + " created")
        except Exception as e:
            print("error during read or write " + filename + " type: " + e)


        
def parser(text):
    lst = []
    line = ""
    for char in text:
        line += char
        if char == ';':
            lst.append(line)
            line = ""
    lst.append(line)
    return lst
            
    
    
main()
input("\nPRESS ENTER TO CLOSE\n")

print("*** CLOSE ***")
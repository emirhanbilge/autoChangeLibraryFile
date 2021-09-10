import os , sys 

versionPython = (sys.version)
pymodbusVersion = 0
cwd = os.getcwd()+"/tcp.py"
cwd2 = os.getcwd()+"/asynchronous.py"

print("Current Director : " , cwd)

try : 
    import pymodbus
    pymodbusVersion = pymodbus.__version__
except:
    sys.exit("Please install pymodbus module ")

if float(versionPython[0:3]) >= 3.5 :
    if float(pymodbusVersion[0:3]) >= 2.5:
        try:
            fileUrl = str(pymodbus.__file__)[0:-11]
            pathTcp = (fileUrl+"client/asynchronous/tcp.py")
            pathAsync = (fileUrl + "server/asynchronous.py")
            print("Tcp Path : " ,  pathTcp)
            print("Async Path : " , pathAsync)
            os.replace(cwd , pathTcp) # ip alma kısmındaki değişiklikler için
            os.replace(cwd2 , pathAsync) # async içerisindeki değişiklikler için
            print("successfully transfered")
        except:
            print("File already transferred")
    else:
        sys.exit("pymodbus version must be bigger than >=2.5 ")

else:
    sys.exit("Python version must be bigger than >=3.5 ")
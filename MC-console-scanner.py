from genericpath import exists
import os,time,sys
#import timestamp
from progressbar import progressbar
#summary description
name = ["errors","warns","shop","disconnects","joins","commands","chat"]
#scanner filters
filters = ['[Server thread/ERROR]',"[Server thread/WARN]:",'[Server thread/INFO]: [EconomyShopGUI]',"lost connection: ","logged in with entity id ","issued server command: /","[Async Chat Thread - #"]
#output filenames
filenames = ["errors","warns","shoplog","disclog","joinlog","cmdlog","chatlog"]
#do not touch
res = [0,0,0,0,0,0,0]
x = 1
path="./output/"
dupe = None

def save(f,file:str,x):
    if dupe is False: #file unico
        file = open(f"{path}{txtfile}/{file}.txt", "a") #0
        file.write(f)
        file.close()
    else: #run n di uno stesso file
        file = open(f"{path}{txtfile}-{x}/{file}.txt", "a") #0
        file.write(f)
        file.close()
    return

def finish():
    os.system("cls")
    print('3')
    print("\nRiepilogo:\n")
    for x in range(len(res)):
        print(f"{name[x]}: {res[x]}")
    print("\n\nOperazione completata")
    sys.exit()

def read(x,file):
    f = open(file, 'r+', encoding="utf8")
    print("L'operazione potrebbe richiedere alcuni minuti...\n\n")
    for line in progressbar(f.readlines(), redirect_stdout=True):
        line.split('\n')
        for d in range(len(filters)):
            if filters[d] in line:
                if "lost connection: " == filters[d]:
                    if "[Async Chat Thread - #" in line:
                        pass
                if '[Server thread/ERROR]: null' in line:
                        pass
                if "[Server thread/INFO]:" in line:
                    line.split("[Server thread/INFO]:")
                res[d] += 1
                save(line,filenames[d],x)
    finish()  
                
  


def check(x):
    file = txtfile
    for folder in os.listdir('./output'): 
        if os.path.exists(f"{path}{file}"):
            if os.path.exists(f"{path}{file}-{x}"): 
                x += 1 
                print('Skip') #dir uguale esistente,skippata
                check(x)
            else:
                os.mkdir(f"{path}{file}-{x}")
                print('creato') #dir creato,inzio lettura
                dupe = True
                read(x,txtfile)

        else:
            os.mkdir(f"{path}{file}")
            print('creato') #file unico
            dupe = False
            read(x,txtfile)

#check function backup copy
# PER EVITARE UNA SCOMUNICA (di nuovo) v2
#    for folder in os.listdir('./output'): #
#        if os.path.exists(f"{path}{file}"):
#            if os.path.exists(f"{path}{file}-{x}"):
#                x += 1
#                print('Skip')
#                check(x)
#            else:
#                os.mkdir(f"{path}{file}-{x}")
#                print('creato')
#                sys.exit()

# PER EVITARE UNA SCOMUNICA (di nuovo)
#    for folder in os.listdir('./output'): 
#        if os.path.exists(f"{path}Run-#{x}"):
#            x += 1
#            print('Skip')
#            check(x)
#        else:
#            os.mkdir(f"{path}Run-#{x}")
#            print('creato')
#            sys.exit()
            

#main code
print("IL FILE DEVE ESSERE NELLA STESSA CARTELLA DI reader.py\n")
#txtfile = "latest.txt" #uncomment this for testing, 
txtfile = input("inserisci il nome del file da leggere: ") 
os.system("cls")
if not os.path.exists(txtfile):
    print(f'txt file {txtfile} not found')
    sys.exit()
if not os.path.isdir('./output'): #first run setup
    os.mkdir('output')
    os.mkdir(f'{path}{txtfile}')
    print('setup completato')0
    dupe = False
    read(x,txtfile)
else:
    check(x)



        

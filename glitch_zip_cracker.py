import os

try:
    from tqdm import tqdm
except ModuleNotFoundError:
    os.system("pip3 install tqdm")
try:
    import zipfile
except MoudleNotFoundError:
    os.system("pip3 install unzip")
    os.system("pip3 install zipfile")

# Regular Colors
Black="\033[0;30m" # Black 
Red="\033[0;31m" # Red 
Green="\033[0;32m" # Green 
Yellow="\033[0;33m" # Yellow 
Blue="\033[0;34m" # Blue 
Purple="\033[0;35m" # Purple 
Cyan="\033[0;36m" # Cyan
White="\033[0;37m" # White




# Background
On_Black="\033[40m" # Black 
On_Red="\033[41m" # Red 
On_Green="\033[42m" # Green
On_Yellow="\033[43m" # Yellow 
On_Blue="\033[44m" # Blue 
On_Purple="\033[45m" # Purple 
On_Cyan="\033[46m" # Cyan
On_White="\033[47m" # White



try:
    global zip_file
    os.system("clear")
    zip_show=On_Red+" Not Selected [!]  "
    word_show=On_Red+" Not Selected [!]  "

    def banner():
        os.system("clear")
        print (Blue +"      _    _                                         ")
        print (Green+"   ,-(|)--(|)-.                                      ")
        print (Blue +"   \_   ..   _/"+Cyan+" .--. .-.   _  .-.      .-.           ")
        print (Green+"     \______/  "+Cyan+": .--': :  :_;.' `.     : :           ")
        print (Red + "       V  V    "+Cyan+": : _ : :  .-.`. .'.--. : `-. "+Blue+"   ___  ")
        print (Green+"       `.^^`.  "+Cyan+": :; :: :_ : : : :'  ..': .. :"+Green+" /^,--' ")
        print (Blue +"         \^^^\ "+Cyan+"`.__.'`.__;:_; :_;`.__.':_;:_;"+Blue +"(^^\    ")
        print (Green+"         |^^^|                  _,-._        \^^\    ")
        print (Blue +"        (^^^^\      __      _,-'^^^^^`.    _,'^^)    ")
        print (Green+"         \^^^^`._,-'^^`-._.'^^^^__^^^^ `--'^^^_/     ")
        print (Blue +"          \^^^^^ ^^^_^^^^^^^_,-'  `.^^^^^^^^_/       ")
        print (Green+"           `.____,-' `-.__.'        `-.___.'         ")
        print (Green+"               coded by Abdo Sleem (*__^)            ")
        print (Purple+"   |------------------------------------------------|")
        print (Black +"    "+On_Yellow+"   File ==> "+zip_show+On_Black)
        print (Purple+"   |------------------------------------------------|")
        print (Black +"    "+On_Yellow+"   wordlist ==> "+word_show+On_Black)
        print (Purple+"   |------------------------------------------------|"+White)
    banner()
    print("      ")

#    zip_file = input("   Enter Zip File path : ")
#    file = os.path.exists(zip_file)
#&^*€^£€%*€^*&^*&*(^&^?*^?*^(*^(*^€(^€*^*€^*€^€*^
#    if zip_file.endswith('.zip'):
#        file = os.path.exists(zip_file)

    def hack():
        zip_file = input(Yellow+"   Enter Zip File path : "+Green)
        if zip_file.endswith('.zip'):
 #           zip_file = input("   Enter Zip File path : ")
            file = os.path.exists(zip_file)
            while file == False:

                print("  ")
                print (Red+"   File Not Found [!]                                   ")
                print("   ")
                zip_file = input(Yellow+"   Enter Zip File path : "+Green )
                file = os.path.exists(zip_file)
            else:
#                global str(zip_file)
#                os.system ("rm -rf data.txt")
                print(" ")
                data=open('data.txt', 'a', newline=None)
             #   data.write("   ")
                data.write('\r' + "file : " + zip_file)
                data.close()
                file_use=open('.file.txt', 'w')
                file_use.write(zip_file)
                file_use.close()
 #               zzip_file=zip_file
#                print("   file ==> ", zip_file)
#                global zip_file
            ####    banner()
###            pass
   #     if zip_file.endswith('.zip'):
    #        hack()

        else:
            print("  ")
            print (Red+"   File Must Have "+Green+".zip ")
            print("  ")
        #    zip_file = input("   Enter Zip File path : ")
            hack()
    hack()
##&*^*&^€*^*&^&*^*&^*&^*&^€^*&^(&(&^(*^(^**(^**(
    file_use=open('.file.txt', 'r')
    zip_file=file_use.readlines()[-1]
    zip_file=str(zip_file)
    file_use.close()
    zip_show=On_Green+" "+zip_file+"  "
    banner()



    print("    ")
    userinput = input(Yellow+"   Do You Want To Use Wordlist.txt ["+Green+"y"+Yellow+"/"+Green+"n"+Yellow+"]:"+Green)
#    print("    ")
    if userinput == "y":
        print("   ")
        wordlist = "wordlist.txt"
        #!;#*^*#*&#**×*#*&*#*×(×&*&×*×&*×(€
        word_path = os.path.exists(wordlist)
        if word_path == True:
            word_show=On_Green+" "+wordlist+"  "
            o=os.getcwd()
            banner()
   # data=open('data.txt', 'r')
  #  zip_path=data.read()
 #   zip_path=str(zip_path)
#    banner()
#            print("   Wordlist ==> ",o+"/Wordlist.txt")
#            print("  ")
#            pass
        if word_path == False:
          #  print("  ")
            banner()
            print("   ")
            print(Red+"   Wordlist.txt Not Found [!] ")
            print(" ")
            down=input(Yellow+"   Do You Want To Download Wordlist.txt ["+Green+"y"+Yellow+"/"+Green+"n"+Yellow+"] : "+Green)
            if down == "y":
                try:
                    import mediafire_dl
                except ModuleNotFoundError:
                    os.system("pip3 install git+https://github.com/scriptvip/mediafire_dl")
                try:
                    import mediafire_dl
                    url="https://www.mediafire.com/file/w6zi9jim4d4q6ux/wordlist.txt/file"
                    output="wordlist.txt"
                    mediafire_dl.download(url, output, quiet=False)
                except requests.exceptions.ConnectionError:
                    print("  ")
                    print("   Connection Error [!]")
            pass
#    data=open('data.txt', 'r')
 #   zip_path=data.read()
  #  zip_path=str(zip_path)

    else:

        print("   ")
        wordlist = input(Yellow+"   Enter Wordlist path : "+Green)
        print("  ")
        word_path = os.path.exists(wordlist)
        while word_path == False:
            print(Red+"   Wordlist Not Found [!]")
            print("  ")
            wordlist = input(Yellow+"   Enter Wordlist path : "+Green)
            word_path = os.path.exists(wordlist)
            print("  ")
            pass


        if word_path == True:
            word_show=On_Green+" "+wordlist+"  "
            banner()
        #    print("   Wordlist ==> ",wordlist)
            pass
#    if word_path == True:
#        o=os.getcwd()
#        print("   Wordlist ==> ",o,"wordlist.txt")
#        print("  ")
#        pass


        #*^*^**^**&*&*&*&*&*^*^*^*^*&*;**;*;*;*;*;*
#    else:
#        wordlist = input("   Enter Wordlist: ")
#        print("    ")
    zip_file = zipfile.ZipFile(zip_file)
#    print("  ")
#    print("   file selected [!] ")

    nwords = len(list(open(wordlist,"rb")))
#    print("  ")
#    print("   wordlist selected [!]")
#    print("   ")





    print("  ")
    nn=0
    print(Yellow+"   Number of passwords to test : "+Green+str(nwords))
    print("     ")
    with open(wordlist, "rb") as wordlist:
        for word in tqdm(wordlist, total=nwords, unit="word"):
            try:
#                nn=nn+1
#                print(" [",nn,"]==> ",word.decode().strip())
                zip_file.extractall(pwd=word.strip())
            except:
                continue

            else:
                print(Yellow+" [+] Password found : "+Green+word.decode().strip())
                password=open('data.txt', 'a', newline=None)
                pass_word = word.decode().strip()
                password.write('\r' + "pass : " + pass_word + '\r')
                exit(0)
    print(Yellow+"[!] Password not found, try other wordlist.")
except FileNotFoundError:
    print("      file not found [!]")
    print("  ")
except KeyboardInterrupt:
    print(" ")
    print(Red+"   script stop !")
    print("  ")
except zipfile.BadZipFile:
    print(" ")
    print("  File Not Found")
    print("  ")
print("                                       ")

#coded by oussea Aloui && cybereagle2001
#python code

# import lib
import base64
import os
import time
import random 
from string import maketrans


rot13trans= maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')
# banners
banner1 =("""
                                           
                         _____                    _____            _____                    _____            _____                  _______         
                        /\    \                  /\    \          |\    \                  /\    \          /\    \                /::\    \        
                       /::\    \                /::\    \         |:\____\                /::\    \        /::\    \              /::::\    \       
                      /::::\    \              /::::\    \        |::|   |               /::::\    \       \:::\    \            /::::::\    \      
                     /::::::\    \            /::::::\    \       |::|   |              /::::::\    \       \:::\    \          /::::::::\    \     
                    /:::/\:::\    \          /:::/\:::\    \      |::|   |             /:::/\:::\    \       \:::\    \        /:::/~~\:::\    \    
                   /:::/  \:::\    \        /:::/__\:::\    \     |::|   |            /:::/__\:::\    \       \:::\    \      /:::/    \:::\    \   
                  /:::/    \:::\    \      /::::\   \:::\    \    |::|   |           /::::\   \:::\    \      /::::\    \    /:::/    / \:::\    \  
                 /:::/    / \:::\    \    /::::::\   \:::\    \   |::|___|______    /::::::\   \:::\    \    /::::::\    \  /:::/____/   \:::\____\ 
                /:::/    /   \:::\    \  /:::/\:::\   \:::\____\  /::::::::\    \  /:::/\:::\   \:::\____\  /:::/\:::\    \|:::|    |     |:::|    |
               /:::/____/     \:::\____\/:::/  \:::\   \:::|    |/::::::::::\____\/:::/  \:::\   \:::|    |/:::/  \:::\____\:::|____|     |:::|    |
               \:::\    \      \::/    /\::/   |::::\  /:::|____/:::/~~~~/~~      \::/    \:::\  /:::|____/:::/    \::/    /\:::\    \   /:::/    / 
                \:::\    \      \/____/  \/____|:::::\/:::/    /:::/    /          \/_____/\:::\/:::/    /:::/    / \/____/  \:::\    \ /:::/    /  
                 \:::\    \                    |:::::::::/    /:::/    /                    \::::::/    /:::/    /            \:::\    /:::/    /   
                  \:::\    \                   |::|\::::/    /:::/    /                      \::::/    /:::/    /              \:::\__/:::/    /    
                   \:::\    \                  |::| \::/____/\::/    /                        \::/____/\::/    /                \::::::::/    /     
                    \:::\    \                 |::|  ~|       \/____/                          ~~       \/____/                  \::::::/    /      
                     \:::\    \                |::|   |                                                                           \::::/    /       
                      \:::\____\               \::|   |                                                                            \::/____/        
                       \::/    /                \:|   |                                                                             ~~              
                        \/____/                  \|___|                                                                                             
                                                                                                                                                                                                                                                     
                                                                                                                                                                                                      """)

banner2=("""                                                                                
  ,   ################        (                      *        (##############  * 
  ,   ################     . *                       /      ###############(  / 
  ,   #################*  #  /                  #      ,  .################(  / 
  ,   ###################,   *   .              #       //###############(#(  / 
  ,   ####################   /   .              #       ###################(  / 
  ,   #####################, *   .              #     .####################(  / 
  ,   #######################*   .              #    (#####################(  / 
  ,   ###########(############   .              #   ###########(###########(  / 
  ,   ###########*#############  .              #  ###########*.####(######(  / 
  ,   ###########(  (###########*.              #.#(#####(((#.  ###########(  / 
  ,   ###########*   *(###########              ############    ####(######(  / 
  ,   ###########*    .############.           ############  ./ ###########(  / 
  ,   ##########(*     (############(        /###########/      ###########(  / 
  ,   ########(#(*   (   (############      #######(####.       ###########(  / 
  ,   ###########* /      .############.   ############.        ###########(  / 
  ,   ########(##*         .############/*###########*  /       ############  / 
  ,   ###########*        *  (####################((     ( *//. ############  / 
  ,   ####((#####*        /  * ###################*      *   /* ############  / 
  ,   ###########*       .   *  (################       .       ############  / 
  ,   ###########*       /   *   .###############       /       ############  / 
  ,   ###########*       .   /   . ###########/ #       .       ############  / 
  ,   ###########*      /    *   .  #########.  #      (        #####(######  / 
  ,   ############,     /    /   .   .######    #      ,        ############  / 
  ,   ###########*    ,#     *   .     ###*     #     .         ############  / 
  ,   ##########(*      /    /   .      (       #     (         ############  / 
  ,   #####(#((#(*       /   *   .              #             ,.############  / 
  ,   ##########(*       .   /   .              #    /      (   ############  / 
  ,   ###########*        /  *   .              #    ,    #     ############  / 
  ,   ############.        / /   .              #   ,   /       ############  / 
  ,   ###########*   (       *   .              #   ( .         ############  / 
  ,   ###########*       #  /*   .              #   #,          ############  * 
  """)

banner3 =("""
     .--------.
    / .------. \***************************************************************
   / /        \ \*****************  CRYPTO THE BEST WAY TO SECURE YOUR MESSAGE
   | |        | |
  _| |________| |_
.' |_|        |_| '.
'._____ ____ _____.'
|     .'____'.     |
'.__.'.'    '.'.__.'
'.__  | LOCK |  __.'
|   '.'.____.'.'   |
'.____'.____.'____.'
'.________________.'  """)



# function of encoding && decoding
def rot13(s):
    return s.translate(rot13trans)

def crypto1(message):
       message_bytes= message.encode('ascii')
       base64_bytes= base64.b64encode(message_bytes)
       base64_message= base64_bytes.decode('ascii') 
       str_base64= repr(base64_message)
       text_rot13= rot13(str_base64)
       longs= len(text_rot13)
       text= text_rot13[2:longs-1]
       return text

# main program
os.system('clear')
choix=(banner1,banner2,banner3)
print(random.choice(choix))
time.sleep(5)
os.system("clear")
print("<c> All Right Reserved")
os.system('figlet "Crypto"')
menu=raw_input("choose one option (enc/dec): ")
if (menu == "enc"):
   os.system("clear")   
   print("\033[1;33m")
   os.system("espeak 'Hello. Crypto is. the best way. To secure. your files.'")
   os.system("clear")
   print("* /******************* Crypto ******************\ *")
   print("*|*                                             *|*")
   print("*|*                   Welcome                   *|*")
   print("*|*       authors: oussama ben hadj dahman      *|*")
   print("*|*                      &&                     *|*")                   
   print("*|*                oussema Aloui                *|*")
   print("*|*                                             *|*")
   print("*|*        emails: cybereagle592@gmail.com      *|*")
   print("*|*               alouioussema697@gmail.com     *|*")
   print("*|*                                             *|*")
   print("*|*            project : Crypto v0.2            *|*")
   print("*|*                                             *|*")
   print(" *\**********************************************/*")
   print("\033[0m")
   main1 = raw_input("choose your option (base64/rot13/crypto1): ")
   if (main1 == "base64"):
       os.system("clear")
       print("\033[1;34m")
       os.system('figlet "BASE64"')
       print("\033[0m")
       message=raw_input("write your text: ")
       message_bytes= message.encode('ascii')
       base64_bytes= base64.b64encode(message_bytes)
       base64_message= base64_bytes.decode('ascii')
       file= open("encode.txt","w")
       file.write("your encoded text is :" + "\n" + base64_message + "\n")
       file.close()
       print("\033[1;31m you will find the encoded text in encode.txt")

   elif main1 == "rot13":
       os.system("clear")
       print("\033[0;36m")
       os.system("figlet 'ROT13'")
       print("\033[0m")
       message = raw_input("write your text: ")
       rot13_message= rot13(message)
       file = open("encode.txt","w")
       file.write("your encoded text is : "+"\n"+ rot13_message + "\n")
       file.close()
       print("\033[1;31m you will find the encoded text in encode.txt")

   elif main1 == "crypto1":
       os.system("clear")
       print("\033[0;35m")
       os.system('figlet "CRYPTO1"')
       print("\033[0m")
       message = raw_input("write your text : ")
       crypto1_text= crypto1(message)
       file = open("encode.txt","w")
       file.write("your encoded text is : "+"\n"+ crypto1_text+"\n")
       file.close()
       print("\033[1;31m you will find the encoded text in encode.txt")

elif menu == "dec":
    os.system("clear")
    print("\033[1;33m")
    print("* /******************* Crypto ******************\ *")
    print("*|*                                             *|*")
    print("*|*                   Welcome                   *|*")
    print("*|*       authors: oussama ben hadj dahman      *|*")
    print("*|*                      &&                     *|*")                   
    print("*|*                oussema Aloui                *|*")
    print("*|*                                             *|*")
    print("*|*        emails: cybereagle592@gmail.com      *|*")
    print("*|*               alouioussema697@gmail.com     *|*")
    print("*|*                                             *|*")
    print("*|*            project : Crypto v0.2            *|*")
    print("*|*                                             *|*")
    print(" *\**********************************************/*")
    print("\033[1;31m")
    print("To decode your file please follow the instructions bellow ")
    print("\033[0m")
    main2= raw_input("choose your option (base64/rot13/crypto1): ")
    if main2 == 'base64':
       os.system('clear')
       print("\033[1;34m")
       os.system('figlet "BASE64"')
       print("\033[0m")
       base64_message = raw_input("write the text to decrypt: ")
       base64_bytes = base64_message.encode('ascii')
       message_bytes = base64.b64decode(base64_bytes)
       message = message_bytes.decode('ascii')
       file = open("decode.txt","w")
       file.write("your decoded text is : " +"\n" + message + "\n")
       file.close()
       print("\033[1;31m you will find the decoded text in decode.txt")

    elif main2 == 'rot13':
       os.system("clear")
       print("\033[0;36m")
       os.system("figlet 'ROT13'")
       print("\033[0m")
       message = raw_input("write the text to decrypt: ")
       rot13_message= rot13(message)
       file = open("decode.txt","w")
       file.write("your decoded text is : "+"\n"+ rot13_message + "\n")
       file.close()
       print("\033[1;31m you will find the decoded text in decode.txt")

    elif main2 == 'crypto1':
       os.system("clear")
       print("\033[0;35m")
       os.system("figlet 'CRYPTO1'")
       print("\033[0m")
       message = raw_input("write the text to decrypt: ")
       rot13_message= rot13(message)
       base64_message = rot13_message
       base64_bytes = base64_message.encode('ascii')
       message_bytes = base64.b64decode(base64_bytes)
       final_message = message_bytes.decode('ascii')
       file = open("decode.txt","w")
       file.write("your decoded text is : "+"\n"+ final_message + "\n")
       file.close()
       print("\033[1;31m you will find the decoded text in decode.txt")
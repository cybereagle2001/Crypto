#coded by cybereagle2001 
#last time edited :Thu 16 Apr 2020 12:54:09 PM UTC 
#!
clear
sudo apt-get update 
sudo apt-get install festival
sudo apt-get install espeak
sudo apt-get install figlet
sudo apt-get install pv
clear
echo "©All Right Reserved to cybereagle2001(Oussama Ben Hadj Dahman)"
figlet "Crypto"
read -p "choose one option (enc/dec): " MrRobot
if [ "$MrRobot" == "enc" ]; then
clear
espeak "CRYPTO BY CYBER EAGLE"
echo "//////////////// CRYPTO BY CYBER EAGLE ///////////////" |pv -qL 10
echo "THE BEST CHOICE TO SECURE YOUR DOCUMENTS"> the
festival --tts the
echo "////// THE BEST CHOICE TO SECURE YOUR DOCUMENTS ///// " |pv -qL 10
read -p "write your text: " Eliot
echo  $Eliot | base64 > encode
echo "end. you will found your encrypted text in encode.txt"
fi

if [ "$MrRobot" == "dec" ]; then
clear
espeak "CRYPTO BY CYBER EAGLE"
echo "//////////////// CRYPTO BY CYBER EAGLE ///////////////" |pv -qL 10
echo "THE BEST CHOICE TO SECURE YOUR DOCUMENTS"> the
festival --tts the
echo "////// THE BEST CHOICE TO SECURE YOUR DOCUMENTS ///// " |pv -qL 10
read -p "write your text: " Robot
echo $Robot | base64 -d > decode
echo "end. you will found your decoded text in decode.txt"
fi

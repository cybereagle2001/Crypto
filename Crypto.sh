#coded by cybereagle2001 
#last time edited :Sat 25 Apr 2020 05:21:18 PM UTC 
#!
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
read -p "choose your option (base64/rot13): " oussama
if [ "$oussama" == "base64" ]; then
read -p "whrite your text: " MrRobot
echo $MrRobot | base64 > encode
echo "end. you will found your encrypted text in encode.txt"
fi
if [ "$oussama" == "rot13" ];then
function rot13 {
tr 'A-Za-z' 'N-ZA-Mn-za-m' 
}
read -p "write your text: " Robot3
echo $Robot3 |rot13 > decode
echo "end. you will found your decoded text in decode.txt"
fi
fi

if [ "$MrRobot" == "dec" ]; then
clear
espeak "CRYPTO BY CYBER EAGLE"
echo "//////////////// CRYPTO BY CYBER EAGLE ///////////////" |pv -qL 10
echo "THE BEST CHOICE TO SECURE YOUR DOCUMENTS"> the
festival --tts the
echo "////// THE BEST CHOICE TO SECURE YOUR DOCUMENTS ///// " |pv -qL 10
read -p "choose your option(base64/rot13): " Robot
if [ "$Robot" == "base64" ]; then
read -p "write your text: " Robot2
echo $Robot2 | base64 -d > decode
echo "end. you will found your decoded text in decode.txt"
fi
if [ "$Robot" == "rot13" ]; then
function rot13 {
tr 'A-Za-z' 'N-ZA-Mn-za-m' 
}
read -p "write your text: " Robot3
echo $Robot3 |rot13 > decode
echo "end. you will found your decoded text in decode.txt"
fi
fi

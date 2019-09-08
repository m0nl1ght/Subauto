rm -f /waf/waf.txt 2>/dev/null
waf() {
MY_PATH="`dirname \"$0\"`"
MY_PATH="`( cd \"$MY_PATH\" && pwd )`"
echo -e "\033[1;32m [+] \033[0m" "\033[1;36m Checking Waf please wait......\033[0m"
cd waf
for r3m0t3 in $(python whatwaf.py -u hawamer.com > waf.txt)
do
$r3m0t3
cat $(pwd)/waf/waf.txt|grep -R "FIREWALL"|cut -d ":" -f 4|cut -d "[" -f 5|cut -d "]" -f 2
done
}
waf

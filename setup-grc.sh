if [ "$(whoami)" != root ]; then
    echo "[-] Please run this script as root or using sudo"
    exit 1
fi

apt install grc
GRCCONF=/etc/grc.conf
CONFTAIL=/usr/share/grc/conf.tail

if grep -q conf.tail ${GRCCONF}; then
    echo "[!] File 'conf.tail' already changed... skipping"
else
    cat >> ${GRCCONF} << EOF
# tail command
(^|[/\w\.]+/)?tail\s?
conf.tail
EOF
    echo "[+] File 'conf.tail updated"
fi
if [ -e ${CONFTAIL} ]; then
    echo "[!] File 'conf.tail' already exists... skipping"
else
    cat > ${CONFTAIL} << EOF
======
# date
regexp=^... (\d| )\d \d\d:\d\d:\d\d(\s[\w\d]+?\s)
colours=green, green, red
count=once
======
# parentheses
regexp=\(.+?\)
colours=green
count=more
======
# pathname
regexp=/[\w/\.]+
colours=bold green
count=more
======
# ip number
regexp=\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}
colours=bold magenta
count=more
======
# success
regexp=(?i)\w*success\w*
colours=on_green
count=more
======
# fail
regexp=(?i)\w*(fail|error)\w*
colours=on_red
count=more
EOF
    echo "[+] File 'conf.tail' created"
fi
echo
echo "Use the following command to view logs:"
echo "  grc tail -f <file>"
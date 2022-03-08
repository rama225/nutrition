#!C:\bin\python\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'ablog==0.6.4','console_scripts','ablog'
__requires__ = 'ablog==0.6.4'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('ablog==0.6.4', 'console_scripts', 'ablog')()
    )

#!C:\bin\python\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'invoke==0.10.1','console_scripts','inv'
__requires__ = 'invoke==0.10.1'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('invoke==0.10.1', 'console_scripts', 'inv')()
    )

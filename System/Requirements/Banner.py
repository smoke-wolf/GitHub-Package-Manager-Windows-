import datetime
import time
try:
    import System.Requirements.FTD
except:
    pass
Launcher = '''
  _                            _               
| |                          | |              
| |     __ _ _   _ _ __   ___| |__   ___ _ __ 
| |    / _` | | | | '_ \ / __| '_ \ / _ \| __|
| |___| (_| | |_| | | | | (__| | | |  __/ |   
\_____/\__,_|\__,_|_| |_|\___|_| |_|\___|_|    
================================================
'''
try:
    import User.UserProfile

    User = User.UserProfile.Username
except:
    pass
red = '\033[0;36m'
green ='\033[0;32m'
purple = '\033[0;35m'
cyan = '\033[0;36m'

FunctionListn =f'''
{red}|  |   SSSSSSSSSSSSSSS                                        AAA         TTTTTTTTTTTTTTTTTTTTTTT
{green}|  | SS:::::::::::::::S                                      A:::A        T:::::::::::::::::::::T
{purple}|  |S:::::SSSSSS::::::S                                     A:::::A       T:::::::::::::::::::::T
{cyan}|  |S:::::S     SSSSSSS                                    A:::::::A      T:::::TT:::::::TT:::::T
{red}|  |S:::::S      wwwwwww           wwwww           wwwwwwwA:::::::::A     TTTTTT  T:::::T  TTTTTT
{green}|  |S:::::S       w:::::w         w:::::w         w:::::wA:::::A:::::A            T:::::T        
{purple}|  | S::::SSSS     w:::::w       w:::::::w       w:::::wA:::::A A:::::A           T:::::T        
{cyan}|  |  SS::::::SSSSS w:::::w     w:::::::::w     w:::::wA:::::A   A:::::A          T:::::T        
{red}|  |    SSS::::::::SSw:::::w   w:::::w:::::w   w:::::wA:::::A     A:::::A         T:::::T        
{green}|  |       SSSSSS::::Sw:::::w w:::::w w:::::w w:::::wA:::::AAAAAAAAA:::::A        T:::::T        
{purple}|  |            S:::::Sw:::::w:::::w   w:::::w:::::wA:::::::::::::::::::::A       T:::::T        
{cyan}|  |            S:::::S w:::::::::w     w:::::::::wA:::::AAAAAAAAAAAAA:::::A      T:::::T        
{red}|  |SSSSSSS     S:::::S  w:::::::w       w:::::::wA:::::A             A:::::A   TT:::::::TT      
{green}|  |S::::::SSSSSS:::::S   w:::::w         w:::::wA:::::A               A:::::A  T:::::::::T      
{purple}|  |S:::::::::::::::SS     w:::w           w:::wA:::::A                 A:::::A T:::::::::T      
{cyan}|  | SSSSSSSSSSSSSSS        www             wwwAAAAAAA                   AAAAAAATTTTTTTTTTT
\033[1;37m===============================================================================================
|/|             What's up {User}!       
|/|             Today: {datetime.datetime.today()}
|/|             From The Devs! {System.Requirements.FTD.Version}
===============================================================================================
|/|             |-------------------------------|-------------------------------| 
|/|             | 1:: SwAT Information          | 5:: Package Launcher          |
|/|             |-------------------------------|-------------------------------|
|/|             | 2:: Manual Cache management   | 6:: Package Uninstaller       |
|/|             |-------------------------------|-------------------------------|
|/|             | 3:: Package Settings          | 7:: Exit                      |
|/|             |-------------------------------|-------------------------------|
|/|             | 4:: Package Compiler          | Why are snails slow?          |
|/|             |-------------------------------|-------------------------------|
'''
FunctionList = f'''
\033[1m ______                ______             
    |          |   |      |   |      |\ /| 
    | +-       |-+-|      |-+-       | + | 
    |   |      |   |      |          |   | 
     ---  \033[0m                                                                                                                                                                                                                                                                                                                    
==========================================
What's up \033[1m\033[1m{User}!\033[0m      
Today: {datetime.datetime.today()}
From The Devs! {System.Requirements.FTD.Version}
Check out the GUI it's option 9!
===========================================
\033[0;32m|-------------------------------| 
\033[0;32m| \033[0;31m1:: GHPM Information          \033[0;32m| 
\033[0;32m|-------------------------------|
\033[0;32m| \033[0;33m2:: Manual Cache management   \033[0;32m| 
\033[0;32m|-------------------------------|
\033[0;32m| \033[0;36m3:: Package Settings          \033[0;32m|          
\033[0;32m|-------------------------------|
\033[0;32m| \033[1;33m4:: Package Compiler          \033[0;32m|
\033[0;32m|-------------------------------|
\033[0;32m| \033[0;34m5:: Package Launcher          \033[0;32m|
\033[0;32m|-------------------------------|
\033[0;32m| \033[0;31m6:: Package Uninstaller       \033[0;32m|
\033[0;32m|-------------------------------|
\033[0;32m| \033[0;32m7:: DataLock Encrypt          \033[0;32m|
\033[0;32m|-------------------------------|
\033[0;32m| \033[0;35m8:: Exit                      \033[0;32m|
\033[0;32m|-------------------------------|
\033[0;32m| \033[1;37m0 -> Update                   \033[0;32m|
\033[0;32m|-------------------------------|
\033[0;32m| \033[0;31m9::GraphicUI                  \033[0;32m|
\033[0;32m|-------------------------------|\033[1;35m
'''

Function_Settings = '''
|==================================|        
|            Settings              |
|==================================|
|1 | Info                          |
|==================================|
|2 | User Settings                 |
|==================================|
'''

'''
|3 | System Settings               |
|==================================|'''
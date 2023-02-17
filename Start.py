# Main Launch File
import sys

try:
    import System.Drive.FirstUse
    import System.Drive.ModuleVerifier
    import os
except ImportError:
    pass

cwd = os.getcwd()
import System
try:
    print(System.Requirements.Banner.Launcher)
except:
    print('''    
 _                            _               
| |                          | |              
| |     __ _ _   _ _ __   ___| |__   ___ _ __ 
| |    / _` | | | | '_ \ / __| '_ \ / _ \| __|
| |___| (_| | |_| | | | | (__| | | |  __/ |   
\_____/\__,_|\__,_|_| |_|\___|_| |_|\___|_|    
================================================''')
try:    # Loads banner
    exec('System.Drive.FirstUse')
except:
    pass

exec('System.Drive.ModuleVerifier')


try:
    import User
    print(f'Welcome Back {User.UserProfile.Username}!')  # forces userLogin
    import System.Drive.Login

    import System.Drive.Errors_Events.EventMan as EV
    EV.NewEvent(event=f'{User.UserProfile.Username} Logged In\n', Pol=1)
except:

   pass

try:
    exec('System.Drive.Login')
except:
    sys.exit(0)

import System.Drive.FunctionRequest
System.Drive.FunctionRequest.checkpoint()

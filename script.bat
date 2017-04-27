:loop

For /f "tokens=1-2" %%a in ('date /t') do (set newDate_=%%b)
For /f "tokens=1-3 delims=/" %%a in ('echo %newDate_%') do (set date_=%%a-%%b-%%c)

For /f "tokens=1-2 delims=." %%a in ('echo %TIME%') do (set otherTime_=%%a)
For /f "tokens=1-3 delims=:" %%a in ('echo %otherTime_%') do (set time_=%%a-%%b-%%c)

md %date_%
cd %date_%

nmap -sP 192.168.104.9/21 > %time_%.txt

timeout /t 30 /nobreak

cd ..
goto :loop
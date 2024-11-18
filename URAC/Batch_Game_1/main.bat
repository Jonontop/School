@echo off
set stvar_01 = False
set stvar_02 = False
set klet2 = False
cls

echo Dobrodosel v igri!
echo Pritisni kateri koli gumb za nadaljevanje!
echo -------------------------------------------
pause
cls

echo Nahajas se v Slovenski obvescevalno-varnostna agenciji!
echo Iscejo te varnostniki ter agenti zbezi preden te ujamejo!

:main
goto :vnos_check
echo KONEC!

exit /b 0

:klet
echo Nahajas se v kleti!
echo Pojdi LEVO, DESNO, NAPREJ ali NAZAJ
set /p vnos="Vnos: "
if /i "%vnos%" == "LEVO" (
	pause
) else if /i "%vnos%" == "DESNO" (
	pause
) else if /i "%vnos%" == "NAPREJ" (
	pause
) else if /i "%vnos%" == "NAZAJ" (
	pause
) 

pause

:prtlicje
echo Nahajas se v pritlicju!
echo pojdi LEVO, DESNO, NAPREJ ali NAZAJ

:prvonad
echo Nahajate se v 1. nadstorpju!

:drugonad
echo drugo nadaljevanje

:tretjenad
echo tretje nadstorpju

:vnos_check
echo Nahajas se v skaldiscu SOVE!
echo Vnesi stevilo med -1 in 3 za nadaljevanje!
set /p vnos="Vnos: "

if /i "%vnos%" == "-1" (
	call :klet
) else if /i "%vnos%" == "0" (
	call :prtlicje
) else if /i "%vnos%" == "1" (
	call :prvonad
) else if /i "%vnos%" == "2" (
	call :drugonad
) else if /i "%vnos%" == "3" (
	call :tretjenad
)



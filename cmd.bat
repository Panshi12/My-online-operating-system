@echo off
cls
title COMMAND COMPEST - THE CC
echo (c) COPYRIGHT MAGMA.
echo.
:cmd
set /p "cmd=%cd%>"
%cmd%
echo.
goto cmd
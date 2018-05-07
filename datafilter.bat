@echo off
set routine=%cd%
I:
cd I:\Sec\tools\datafilter
python datafilter.py %1
cd %routine%


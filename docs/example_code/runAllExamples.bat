@echo off
setlocal enabledelayedexpansion

cd /d "%~dp0"
set "target_path=%cd%"

if not exist "%target_path%" (
    echo Target path "%target_path%" does not exist. Exiting.
    exit /b 1
)

cd /d "%target_path%"
echo Running example scripts in %target_path%
echo NOTE: RocSlope2 must be available / startable for these examples to succeed.
echo.

for %%f in (*.py) do (
    echo Running %%f ...
    python "%%f" > "%%~nf_result.txt" 2> "%%~nf_error.log"
    if !ERRORLEVEL! EQU 0 (
        del "%%~nf_error.log" >nul 2>&1
        echo Successfully finished %%f
    ) else (
        echo Failed to process %%f. See %%~nf_error.log for details.
    )
)

echo.
echo Done. Result files written as *_result.txt
endlocal

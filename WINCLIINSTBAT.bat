@echo off

:: Define the Startup folder path
set startupFolder=%AppData%\Microsoft\Windows\Start Menu\Programs\Startup

:: Display the Startup folder path for debugging
echo Startup folder path: "%startupFolder%"

:: Check if the Startup folder exists
if not exist "%startupFolder%" (
    echo ERROR: Startup folder does not exist!
    echo Please check your system configuration.
    pause
    exit /b
)

:: Check if the source file exists
if not exist "win11clientexportedition.py" (
    echo ERROR: Source file "win11clientexportedition.py" not found in the current directory!
    echo Ensure the file is in the same directory as this script or provide the correct path.
    pause
    exit /b
)

:: Copy the file to the Startup folder
echo Copying "win11clientexportedition.py" to the Startup folder...
copy "win11clientexportedition.py" "%startupFolder%\win11clientexportedition.py" >nul

:: Check if the copy was successful
if exist "%startupFolder%\win11clientexportedition.py" (
    echo File successfully copied to the Startup folder!
) else (
    echo ERROR: Failed to copy the file to the Startup folder.
    echo Please check your permissions or try running this script as an administrator.
    pause
    exit /b
)

echo Startup folder installation complete.
pause

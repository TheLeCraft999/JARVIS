@echo off
setlocal

REM Define the Python version you want to install
set PYTHON_VERSION=3.12.3

REM Define the URL to download the Python installer
set DOWNLOAD_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe

REM Define the path to save the installer (same directory as the script)
set INSTALLER_PATH=%~dp0python-installer.exe

REM Download the Python installer
echo Downloading Python %PYTHON_VERSION% installer...
powershell -Command "Invoke-WebRequest -Uri %DOWNLOAD_URL% -OutFile %INSTALLER_PATH%"

REM Check if the download was successful
if exist %INSTALLER_PATH% (
    echo Download successful. Installing Python %PYTHON_VERSION%...

    REM Install Python silently
    %INSTALLER_PATH% /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

    REM Check if the installation was successful
    if %ERRORLEVEL% equ 0 (
        echo Python %PYTHON_VERSION% installed successfully.

        REM Ensure pip is installed and upgraded
        echo Installing/upgrading pip...
        python -m ensurepip
        python -m pip install --upgrade pip

        REM Verify pip installation
        if %ERRORLEVEL% equ 0 (
            echo pip installed and upgraded successfully.
        ) else (
            echo pip installation/upgrade failed.
        )
    ) else (
        echo Python installation failed.
    )

    REM Delete the installer file
    del %INSTALLER_PATH%
) else (
    echo Download failed.
)

endlocal
pause
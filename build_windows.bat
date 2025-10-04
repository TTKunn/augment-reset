@echo off
chcp 65001 > nul
echo ====================================
echo  FreeAugmentCode - Windows 打包工具
echo ====================================
echo.

echo [1/4] 检查 Python 环境...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 错误: 未找到 Python，请先安装 Python 3.10+
    echo.
    echo 下载地址: https://www.python.org/downloads/
    pause
    exit /b 1
)
python --version

echo.
echo [2/4] 检查 PyInstaller...
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo 未安装 PyInstaller，正在安装...
    pip install pyinstaller
    if errorlevel 1 (
        echo ❌ 安装 PyInstaller 失败
        pause
        exit /b 1
    )
) else (
    echo ✓ PyInstaller 已安装
)

echo.
echo [3/4] 开始打包...
echo 这可能需要 30-60 秒，请耐心等待...
echo.
pyinstaller --onefile --console --name "FreeAugmentCode-Windows" index.py

if errorlevel 1 (
    echo.
    echo ❌ 打包失败！请检查错误信息
    pause
    exit /b 1
)

echo.
echo [4/4] 打包完成！
echo ====================================
echo ✓ 可执行文件位于: dist\FreeAugmentCode-Windows.exe
echo ====================================
echo.
echo 提示: 您可以删除 build 文件夹和 .spec 文件以节省空间
echo.
pause

#!/bin/bash

echo "===================================="
echo " FreeAugmentCode - Unix/Linux 打包工具"
echo "===================================="
echo ""

echo "[1/4] 检查 Python 环境..."
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误: 未找到 Python3，请先安装 Python 3.10+"
    echo ""
    echo "安装方法:"
    echo "  macOS: brew install python3"
    echo "  Ubuntu/Debian: sudo apt install python3"
    echo "  Fedora: sudo dnf install python3"
    exit 1
fi
python3 --version

echo ""
echo "[2/4] 检查 PyInstaller..."
if ! pip3 show pyinstaller > /dev/null 2>&1; then
    echo "未安装 PyInstaller，正在安装..."
    pip3 install pyinstaller
    if [ $? -ne 0 ]; then
        echo "❌ 安装 PyInstaller 失败"
        exit 1
    fi
else
    echo "✓ PyInstaller 已安装"
fi

echo ""
echo "[3/4] 开始打包..."
echo "这可能需要 30-60 秒，请耐心等待..."
echo ""

# 检测操作系统
OS_NAME=$(uname -s)
if [ "$OS_NAME" = "Darwin" ]; then
    PLATFORM="macOS"
elif [ "$OS_NAME" = "Linux" ]; then
    PLATFORM="Linux"
else
    PLATFORM="Unix"
fi

pyinstaller --onefile --console --name "FreeAugmentCode-${PLATFORM}" index.py

if [ $? -ne 0 ]; then
    echo ""
    echo "❌ 打包失败！请检查错误信息"
    exit 1
fi

echo ""
echo "[4/4] 打包完成！"
echo "===================================="
echo "✓ 可执行文件位于: dist/FreeAugmentCode-${PLATFORM}"
echo "===================================="
echo ""
echo "提示: 您可以删除 build 文件夹和 .spec 文件以节省空间"
echo ""

# 添加执行权限
chmod +x "dist/FreeAugmentCode-${PLATFORM}"
echo "✓ 已添加执行权限"

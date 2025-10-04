# 跨平台打包指南

本文档详细说明如何在 Windows、macOS、Linux 三个平台上使用 PyInstaller 将 FreeAugmentCode 打包成独立的可执行文件。

## 目录

1. [准备工作](#准备工作)
2. [Windows 系统打包](#windows-系统打包)
3. [macOS 系统打包](#macos-系统打包)
4. [Linux 系统打包](#linux-系统打包)
5. [打包文件命名规范](#打包文件命名规范)
6. [测试打包结果](#测试打包结果)
7. [常见问题](#常见问题)
8. [高级配置](#高级配置)
9. [发布检查清单](#发布检查清单)
10. [完整打包流程示例](#完整打包流程示例)

---

## 准备工作

### 所有平台通用步骤

#### 1. 确保 Python 版本

```bash
# Windows
python --version

# macOS/Linux
python3 --version
```

**要求**: Python 3.10 或更高版本

#### 2. 安装 PyInstaller

```bash
# Windows
pip install pyinstaller

# macOS/Linux
pip3 install pyinstaller
```

#### 3. 清理之前的打包文件（如果存在）

```bash
# 删除 build/ 文件夹
# 删除 dist/ 文件夹
# 删除 *.spec 文件（除了 pyinstaller_config.spec 模板）
```

---

## Windows 系统打包

### 方法 1: 使用自动化脚本（推荐）

1. 双击运行 `build_windows.bat`
2. 等待打包完成（约 30-60 秒）
3. 在 `dist/` 目录找到 `FreeAugmentCode-Windows.exe`

### 方法 2: 手动命令行打包

#### 步骤 1: 打开命令提示符

打开 CMD 或 PowerShell

#### 步骤 2: 进入项目目录

```cmd
cd E:\Code\project\augmentcode-reset
```

#### 步骤 3: 安装 PyInstaller（如果未安装）

```cmd
pip install pyinstaller
```

#### 步骤 4: 执行打包命令

```cmd
pyinstaller --onefile --console --name "FreeAugmentCode-Windows" index.py
```

#### 步骤 5: 等待打包完成

打包过程约需 30-60 秒，完成后会显示 "successfully created"

#### 步骤 6: 查找生成的文件

```
dist/FreeAugmentCode-Windows.exe  ← 这是最终的可执行文件
```

### 命令参数说明

| 参数 | 说明 |
|------|------|
| `--onefile` | 打包成单个 exe 文件（而非文件夹） |
| `--console` | 保留控制台窗口（显示程序输出） |
| `--name "xxx"` | 指定输出的可执行文件名 |
| `index.py` | 程序入口文件 |

### 可选参数

```cmd
# 添加图标
--icon=icon.ico

# 隐藏控制台窗口（不推荐，因为需要看输出）
--noconsole

# 指定输出目录
--distpath ./release

# 使用 UPX 压缩（减小文件体积，需要先安装 UPX）
--upx-dir=C:\path\to\upx

# 排除特定模块（减小体积）
--exclude-module tkinter
```

### 示例：带所有常用参数的打包命令

```cmd
pyinstaller ^
  --onefile ^
  --console ^
  --name "FreeAugmentCode-Windows" ^
  --distpath ./dist ^
  --workpath ./build ^
  index.py
```

---

## macOS 系统打包

### 方法 1: 使用自动化脚本（推荐）

#### 步骤 1: 打开终端（Terminal）

#### 步骤 2: 添加执行权限

```bash
chmod +x build_unix.sh
```

#### 步骤 3: 运行脚本

```bash
./build_unix.sh
```

#### 步骤 4: 查找生成的文件

```
dist/FreeAugmentCode-macOS  ← Unix 可执行文件
```

### 方法 2: 手动命令行打包

#### 步骤 1: 打开终端

#### 步骤 2: 进入项目目录

```bash
cd /path/to/augmentcode-reset
```

#### 步骤 3: 安装 PyInstaller

```bash
pip3 install pyinstaller
```

#### 步骤 4: 执行打包命令

```bash
pyinstaller --onefile --console --name "FreeAugmentCode-macOS" index.py
```

#### 步骤 5: 生成的文件位置

```
dist/FreeAugmentCode-macOS  ← Unix 可执行文件
```

### macOS 特殊注意事项

#### 1. 代码签名（可选但推荐）

macOS Catalina (10.15) 及更高版本对未签名的应用有严格限制。

**查看可用的签名标识：**
```bash
security find-identity -v -p codesigning
```

**签名可执行文件：**
```bash
codesign -s "Your Developer ID" dist/FreeAugmentCode-macOS
```

**验证签名：**
```bash
codesign -v dist/FreeAugmentCode-macOS
spctl -a -v dist/FreeAugmentCode-macOS
```

#### 2. 打包成 .app 应用（可选）

如果希望打包成传统的 macOS 应用：

```bash
pyinstaller --onefile --windowed --name "FreeAugmentCode" index.py
```

这会生成 `dist/FreeAugmentCode.app`

#### 3. 解决 Gatekeeper 警告

首次运行时可能提示"无法打开，因为无法验证开发者"。

**解决方案 1: 移除隔离属性**
```bash
xattr -cr dist/FreeAugmentCode-macOS
```

**解决方案 2: 通过系统设置**
1. 打开"系统偏好设置" → "安全性与隐私"
2. 在"通用"标签下点击"仍要打开"

#### 4. 针对不同架构打包

```bash
# Intel (x86_64)
pyinstaller --onefile --target-arch x86_64 index.py

# Apple Silicon (arm64)
pyinstaller --onefile --target-arch arm64 index.py

# 通用二进制（同时支持两种架构，文件较大）
pyinstaller --onefile --target-arch universal2 index.py
```

---

## Linux 系统打包

### 方法 1: 使用自动化脚本（推荐）

#### 步骤 1: 打开终端

#### 步骤 2: 添加执行权限

```bash
chmod +x build_unix.sh
```

#### 步骤 3: 运行脚本

```bash
./build_unix.sh
```

#### 步骤 4: 查找生成的文件

```
dist/FreeAugmentCode-Linux  ← Unix 可执行文件
```

### 方法 2: 手动命令行打包

#### 步骤 1: 打开终端

#### 步骤 2: 进入项目目录

```bash
cd /path/to/augmentcode-reset
```

#### 步骤 3: 安装 PyInstaller

```bash
# Debian/Ubuntu
sudo apt update
sudo apt install python3-pip
pip3 install pyinstaller

# Fedora/RHEL
sudo dnf install python3-pip
pip3 install pyinstaller

# Arch Linux
sudo pacman -S python-pip
pip3 install pyinstaller
```

#### 步骤 4: 执行打包命令

```bash
pyinstaller --onefile --console --name "FreeAugmentCode-Linux" index.py
```

#### 步骤 5: 生成的文件位置

```
dist/FreeAugmentCode-Linux  ← Unix 可执行文件
```

### Linux 特殊注意事项

#### 1. 依赖库问题

某些发行版可能缺少必要的动态库。

**查看依赖：**
```bash
ldd dist/FreeAugmentCode-Linux
```

**常见缺失库及安装方法：**

```bash
# Ubuntu/Debian
sudo apt install libxcb1 libxkbcommon-x11-0

# Fedora
sudo dnf install libxcb libxkbcommon-x11

# Arch Linux
sudo pacman -S libxcb libxkbcommon-x11
```

#### 2. 添加可执行权限

```bash
chmod +x dist/FreeAugmentCode-Linux
```

#### 3. 针对特定发行版打包

PyInstaller 打包的程序会依赖打包时系统的 glibc 版本。**建议在目标发行版的较旧版本上打包**，以获得最大兼容性。

例如：
- 在 Ubuntu 20.04 上打包 → 兼容 Ubuntu 20.04 及更新版本
- 在 Ubuntu 22.04 上打包 → 仅兼容 Ubuntu 22.04 及更新版本

#### 4. 静态链接（高级）

如需更好的跨发行版兼容性，可以考虑：

```bash
# 使用 staticx（需要额外安装）
pip3 install staticx
pyinstaller --onefile index.py
staticx dist/FreeAugmentCode-Linux dist/FreeAugmentCode-Linux-static
```

---

## 打包文件命名规范

### 推荐的命名格式

```
FreeAugmentCode-{Platform}-{Version}.{ext}
```

### 示例

**带版本号：**
```
FreeAugmentCode-Windows-v1.0.0.exe
FreeAugmentCode-macOS-v1.0.0
FreeAugmentCode-Linux-v1.0.0
```

**简化版：**
```
FreeAugmentCode-Windows.exe
FreeAugmentCode-macOS
FreeAugmentCode-Linux
```

### 架构标识（可选）

如果针对特定架构：

```
FreeAugmentCode-Windows-x64-v1.0.0.exe
FreeAugmentCode-macOS-arm64-v1.0.0
FreeAugmentCode-Linux-x86_64-v1.0.0
```

---

## 测试打包结果

### Windows 测试

```cmd
cd dist
FreeAugmentCode-Windows.exe
```

### macOS/Linux 测试

```bash
cd dist
./FreeAugmentCode-macOS    # macOS
./FreeAugmentCode-Linux    # Linux
```

### 测试清单

运行程序后，检查以下项目：

- [ ] 程序正常启动（无报错）
- [ ] 控制台输出正确显示
- [ ] 路径识别正确（显示系统路径）
- [ ] 显示所有功能模块的输出信息
- [ ] 备份功能正常工作
- [ ] 程序正常退出（无崩溃）

### 在干净系统上测试

**重要**: 打包后的程序应在**没有安装 Python** 的系统上测试，以确保真正的独立性。

可以使用：
- 虚拟机
- 其他用户的电脑
- Docker 容器（Linux）

---

## 常见问题

### Q1: 打包后文件很大（>20MB）

**原因**: PyInstaller 会打包所有依赖库，包括不需要的模块。

**解决方案 1: 使用 UPX 压缩**
```bash
# 安装 UPX
# Windows: 从 https://github.com/upx/upx/releases 下载
# macOS: brew install upx
# Linux: sudo apt install upx-ucl

# 打包时启用 UPX
pyinstaller --onefile --upx-dir=/path/to/upx index.py
```

**解决方案 2: 排除不需要的模块**
```bash
pyinstaller --onefile --exclude-module matplotlib --exclude-module numpy index.py
```

**解决方案 3: 使用虚拟环境**
```bash
# 在干净的虚拟环境中打包
python -m venv clean_env
source clean_env/bin/activate  # Linux/macOS
clean_env\Scripts\activate      # Windows
pip install pyinstaller
pyinstaller --onefile index.py
```

### Q2: Windows 杀毒软件误报

**原因**: PyInstaller 打包的程序常被误报为病毒或恶意软件。

**解决方案 1: 提交白名单申请**
- Windows Defender: https://www.microsoft.com/en-us/wdsi/filesubmission
- 其他杀毒软件: 访问各厂商的误报提交页面

**解决方案 2: 添加数字签名**
```bash
# 需要购买代码签名证书（约 $100-500/年）
signtool sign /f certificate.pfx /p password /t http://timestamp.digicert.com dist/FreeAugmentCode-Windows.exe
```

**解决方案 3: 在 README 中说明**
```markdown
## 杀毒软件误报说明
由于本程序使用 PyInstaller 打包，可能被部分杀毒软件误报。
本项目完全开源，您可以审查源码并自行打包。
```

### Q3: macOS 提示"无法验证开发者"

**解决方案 1: 移除隔离属性**
```bash
xattr -cr dist/FreeAugmentCode-macOS
```

**解决方案 2: 通过系统设置允许**
1. 打开"系统偏好设置" → "安全性与隐私"
2. 在"通用"标签下点击"仍要打开"

**解决方案 3: 代码签名**
```bash
codesign -s "Developer ID Application: Your Name" dist/FreeAugmentCode-macOS
```

### Q4: Linux 报错 "cannot execute binary file"

**原因**: 在不同架构的机器上打包（如 ARM vs x86_64）。

**解决方案**: 在目标架构的机器上重新打包。

```bash
# 查看当前架构
uname -m

# x86_64: Intel/AMD 64位
# aarch64: ARM 64位
# armv7l: ARM 32位
```

### Q5: 导入模块失败

**错误示例**:
```
ModuleNotFoundError: No module named 'xxx'
```

**解决方案 1: 手动指定隐藏导入**
```bash
pyinstaller --onefile --hidden-import=模块名 index.py
```

**解决方案 2: 使用 .spec 文件**
```python
# 编辑 .spec 文件
hiddenimports=['module1', 'module2']
```

### Q6: 打包后路径找不到

**原因**: 相对路径在打包后失效。

**解决方案**: 在代码中使用以下模式：

```python
import sys
import os

def get_base_path():
    """获取程序基础路径"""
    if getattr(sys, 'frozen', False):
        # 打包后的路径
        return sys._MEIPASS
    else:
        # 开发时的路径
        return os.path.dirname(os.path.abspath(__file__))

# 使用示例
base_path = get_base_path()
config_file = os.path.join(base_path, 'config.json')
```

### Q7: 程序启动很慢

**原因**: PyInstaller 需要解压临时文件。

**解决方案 1: 使用 --onedir 模式**
```bash
pyinstaller --onedir index.py
# 生成文件夹而非单文件，启动更快但体积更大
```

**解决方案 2: 优化导入**
```python
# 延迟导入大型库
def heavy_function():
    import large_library  # 仅在需要时导入
    large_library.do_something()
```

### Q8: UnicodeDecodeError 编码错误

**解决方案**: 在代码中明确指定编码：

```python
# 读取文件时
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 写入文件时
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
```

---

## 高级配置

### 使用 .spec 文件自定义打包

#### 1. 生成默认 spec 文件

```bash
pyi-makespec --onefile index.py
```

这会生成 `index.spec` 文件。

#### 2. 编辑 .spec 文件

```python
# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['index.py'],
    pathex=[],
    binaries=[],
    datas=[
        # 添加额外的数据文件
        ('config.json', '.'),
        ('assets/*', 'assets'),
    ],
    hiddenimports=[
        # 手动添加隐藏导入
        'pkg_resources.py2_warn',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # 排除不需要的模块
        'matplotlib',
        'numpy',
        'tkinter',
    ],
    noarchive=False,
    optimize=0,
)

exe = EXE(
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='FreeAugmentCode',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico',  # 添加图标
)
```

#### 3. 使用 spec 文件打包

```bash
pyinstaller index.spec
```

### 添加额外的资源文件

如果程序需要配置文件、图片等资源：

```python
# .spec 文件中
datas=[
    ('config.json', '.'),           # 单个文件
    ('assets/*', 'assets'),         # 整个文件夹
    ('data/*.csv', 'data'),         # 特定类型文件
],
```

### 自定义图标

```bash
# Windows (.ico 格式)
pyinstaller --onefile --icon=app.ico index.py

# macOS (.icns 格式)
pyinstaller --onefile --icon=app.icns index.py

# Linux (.png 格式转换为 .ico)
# 使用在线工具或 ImageMagick
convert icon.png -define icon:auto-resize=256,128,64,48,32,16 icon.ico
```

### 添加版本信息（Windows）

创建 `version_info.txt`：

```
VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=(1, 0, 0, 0),
    prodvers=(1, 0, 0, 0),
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
  ),
  kids=[
    StringFileInfo([
      StringTable(
        u'040904B0',
        [StringStruct(u'CompanyName', u'Your Company'),
        StringStruct(u'FileDescription', u'FreeAugmentCode'),
        StringStruct(u'FileVersion', u'1.0.0.0'),
        StringStruct(u'InternalName', u'FreeAugmentCode'),
        StringStruct(u'LegalCopyright', u'Copyright (c) 2025'),
        StringStruct(u'OriginalFilename', u'FreeAugmentCode.exe'),
        StringStruct(u'ProductName', u'FreeAugmentCode'),
        StringStruct(u'ProductVersion', u'1.0.0.0')])
    ]),
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)
```

打包时使用：

```bash
pyinstaller --onefile --version-file=version_info.txt index.py
```

---

## 发布检查清单

打包完成后，发布前请逐项检查：

### 功能测试

- [ ] 在干净的系统上测试（无 Python 环境）
- [ ] 所有核心功能正常工作
- [ ] 错误处理机制有效
- [ ] 备份功能正常
- [ ] 日志输出清晰

### 文件管理

- [ ] 文件命名规范清晰
- [ ] 包含版本号
- [ ] 压缩打包（可选）
  ```bash
  # Windows
  tar -a -c -f FreeAugmentCode-Windows-v1.0.0.zip dist/FreeAugmentCode-Windows.exe

  # macOS/Linux
  zip FreeAugmentCode-macOS-v1.0.0.zip dist/FreeAugmentCode-macOS
  tar -czf FreeAugmentCode-Linux-v1.0.0.tar.gz dist/FreeAugmentCode-Linux
  ```

### 安全性

- [ ] 创建 SHA256 校验和
  ```bash
  # Windows
  certutil -hashfile FreeAugmentCode-Windows.exe SHA256 > checksum.txt

  # macOS/Linux
  shasum -a 256 FreeAugmentCode-macOS > checksum.txt
  sha256sum FreeAugmentCode-Linux > checksum.txt
  ```
- [ ] 代码签名（推荐）
- [ ] 病毒扫描（VirusTotal）

### 文档

- [ ] 更新 README.md 中的下载链接
- [ ] 创建 Release Notes
- [ ] 说明系统要求
- [ ] 添加使用说明

### 发布平台

- [ ] GitHub Releases
- [ ] 版本标签（git tag）
  ```bash
  git tag -a v1.0.0 -m "Release version 1.0.0"
  git push origin v1.0.0
  ```
- [ ] 下载统计

---

## 完整打包流程示例

### Windows 完整流程

```cmd
:: ========================================
:: FreeAugmentCode Windows 打包流程
:: ========================================

:: 1. 清理旧文件
rmdir /s /q build
rmdir /s /q dist
del FreeAugmentCode-Windows.spec 2>nul

:: 2. 安装/更新 PyInstaller
pip install --upgrade pyinstaller

:: 3. 打包
pyinstaller --onefile --console --name "FreeAugmentCode-Windows-v1.0.0" index.py

:: 4. 测试
cd dist
FreeAugmentCode-Windows-v1.0.0.exe
cd ..

:: 5. 生成校验和
certutil -hashfile dist\FreeAugmentCode-Windows-v1.0.0.exe SHA256 > dist\checksum.txt

:: 6. 压缩
tar -a -c -f FreeAugmentCode-Windows-v1.0.0.zip dist\FreeAugmentCode-Windows-v1.0.0.exe dist\checksum.txt

:: 7. 完成
echo 打包完成！文件位于: FreeAugmentCode-Windows-v1.0.0.zip
pause
```

### macOS 完整流程

```bash
#!/bin/bash
# ========================================
# FreeAugmentCode macOS 打包流程
# ========================================

# 1. 清理旧文件
rm -rf build dist *.spec

# 2. 安装/更新 PyInstaller
pip3 install --upgrade pyinstaller

# 3. 打包
pyinstaller --onefile --console --name "FreeAugmentCode-macOS-v1.0.0" index.py

# 4. 添加执行权限
chmod +x dist/FreeAugmentCode-macOS-v1.0.0

# 5. 移除隔离属性
xattr -cr dist/FreeAugmentCode-macOS-v1.0.0

# 6. （可选）代码签名
# codesign -s "Developer ID Application: Your Name" dist/FreeAugmentCode-macOS-v1.0.0

# 7. 测试
cd dist
./FreeAugmentCode-macOS-v1.0.0
cd ..

# 8. 生成校验和
shasum -a 256 dist/FreeAugmentCode-macOS-v1.0.0 > dist/checksum.txt

# 9. 压缩
zip -j FreeAugmentCode-macOS-v1.0.0.zip dist/FreeAugmentCode-macOS-v1.0.0 dist/checksum.txt
# 或
tar -czf FreeAugmentCode-macOS-v1.0.0.tar.gz -C dist FreeAugmentCode-macOS-v1.0.0 checksum.txt

# 10. 完成
echo "打包完成！文件位于: FreeAugmentCode-macOS-v1.0.0.zip"
```

### Linux 完整流程

```bash
#!/bin/bash
# ========================================
# FreeAugmentCode Linux 打包流程
# ========================================

# 1. 清理旧文件
rm -rf build dist *.spec

# 2. 安装/更新 PyInstaller
pip3 install --upgrade pyinstaller

# 3. 打包
pyinstaller --onefile --console --name "FreeAugmentCode-Linux-v1.0.0" index.py

# 4. 添加执行权限
chmod +x dist/FreeAugmentCode-Linux-v1.0.0

# 5. 测试
cd dist
./FreeAugmentCode-Linux-v1.0.0
cd ..

# 6. 检查依赖
echo "检查动态库依赖:"
ldd dist/FreeAugmentCode-Linux-v1.0.0

# 7. 生成校验和
sha256sum dist/FreeAugmentCode-Linux-v1.0.0 > dist/checksum.txt

# 8. 压缩
tar -czf FreeAugmentCode-Linux-v1.0.0.tar.gz -C dist FreeAugmentCode-Linux-v1.0.0 checksum.txt

# 9. 完成
echo "打包完成！文件位于: FreeAugmentCode-Linux-v1.0.0.tar.gz"
```

---

## 附录

### PyInstaller 常用选项速查表

| 选项 | 说明 |
|------|------|
| `--onefile` | 打包成单个文件 |
| `--onedir` | 打包成文件夹（默认） |
| `--console` | 显示控制台窗口 |
| `--noconsole` / `--windowed` | 隐藏控制台窗口 |
| `--name NAME` | 指定输出文件名 |
| `--icon=ICON.ico` | 添加图标 |
| `--add-data SRC:DEST` | 添加数据文件 |
| `--hidden-import MODULE` | 添加隐藏导入 |
| `--exclude-module MODULE` | 排除模块 |
| `--upx-dir DIR` | 使用 UPX 压缩 |
| `--clean` | 清理临时文件 |
| `--version-file FILE` | 添加版本信息（Windows） |
| `--distpath DIR` | 指定输出目录 |
| `--workpath DIR` | 指定临时工作目录 |
| `--specpath DIR` | 指定 .spec 文件目录 |

### 参考资源

- **PyInstaller 官方文档**: https://pyinstaller.org/
- **GitHub 仓库**: https://github.com/pyinstaller/pyinstaller
- **常见问题**: https://github.com/pyinstaller/pyinstaller/wiki
- **UPX 下载**: https://github.com/upx/upx/releases

---

## 更新日志

- **2025-01-XX**: 创建本文档
- 包含 Windows、macOS、Linux 完整打包指南
- 添加常见问题解答
- 提供完整打包流程示例

---

**祝您打包顺利！如有问题，请参考本文档的"常见问题"章节或访问 PyInstaller 官方文档。**

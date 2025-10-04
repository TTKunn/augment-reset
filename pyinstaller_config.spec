# -*- mode: python ; coding: utf-8 -*-
# PyInstaller 高级配置文件模板
#
# 使用方法:
#   1. 根据需要修改此文件
#   2. 运行: pyinstaller pyinstaller_config.spec
#
# 注意: 此文件为模板，默认打包脚本不使用此文件

a = Analysis(
    ['index.py'],
    pathex=[],
    binaries=[],
    datas=[],  # 添加额外的数据文件: [('source', 'destination')]
    hiddenimports=[],  # 如果导入失败，在这里手动添加模块名
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],  # 排除不需要的模块以减小体积
    noarchive=False,
    optimize=0,
)

pyi_splash = None

exe = EXE(
    pyi_splash,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='FreeAugmentCode',
    debug=False,  # 设为 True 可显示调试信息
    bootloader_ignore_signals=False,
    strip=False,  # Linux/macOS: 移除符号表以减小体积
    upx=True,  # 使用 UPX 压缩（需要安装 UPX）
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # 保留控制台窗口
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,  # macOS: 代码签名标识
    entitlements_file=None,  # macOS: 权限文件
    # icon='icon.ico',  # 取消注释并指定图标文件路径
)

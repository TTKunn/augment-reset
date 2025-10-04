# AugmentCode Reset

[English](#english) | [中文](#chinese)

# <a name="chinese"></a>中文版

AugmentCode Reset 是一个用于清理AugmentCode相关数据的工具，可以在同一台电脑上无限次登录不同的账号，避免账号被锁定。

## 功能特性

- 📝 修改Telemetry ID
  - 重置设备 ID 和机器 ID
  - 自动备份原始数据
  - 生成新的随机 ID

- 🗃️ 数据库清理
  - 清理 SQLite 数据库中的特定记录
  - 自动备份数据库文件
  - 删除包含 'augment' 关键字的记录

- 💾 工作区存储管理
  - 清理工作区存储文件
  - 自动备份工作区数据

## 安装说明

1. 确保你的系统已安装 Python 3.10及以上
2. 克隆此仓库到本地：
   ```bash
   git clone https://github.com/yourusername/augmentcode-reset.git
   cd augmentcode-reset
   ```

## ⚠️ 重要提醒

**使用前请注意：**

1. ⚡ **备份重要**: 本工具会自动创建备份，但仍建议手动备份重要数据
2. 🚫 **完全退出**: 使用前必须完全退出 VS Code，确保没有相关进程运行
3. 🔄 **仅限个人**: 此工具仅用于在个人设备上重置登录状态，请勿用于其他用途
4. 📁 **可恢复性**: 所有修改都可通过备份文件恢复（备份文件格式：`*.bak.<timestamp>`）

## 使用方法

1. 退出AugmentCode插件
2. 完全退出 VS Code
3. 执行脚本：

```bash
python index.py
```

4. 重新启动 VS Code
5. AugmentCode 插件中使用新的邮箱进行登录

## 🔨 从源码打包

如果您想自己打包成可执行文件，请参阅 [BUILD.md](BUILD.md) 获取详细的跨平台打包教程。

### 快速打包

**Windows:**
```batch
# 双击运行或在命令行执行
build_windows.bat
```

**macOS/Linux:**
```bash
# 添加执行权限
chmod +x build_unix.sh

# 运行打包脚本
./build_unix.sh
```

打包后的可执行文件位于 `dist/` 目录。

## 项目结构

```
augmentcode-reset/
├── index.py                    # 主程序入口
├── augutils/                   # AugmentCode 工具模块
│   ├── __init__.py
│   ├── json_modifier.py        # JSON 文件修改工具
│   ├── sqlite_modifier.py      # SQLite 数据库修改工具
│   └── workspace_cleaner.py    # 工作区清理工具
├── utils/                      # 通用工具模块
│   ├── __init__.py
│   ├── paths.py                # 跨平台路径管理
│   └── device_codes.py         # ID 生成工具
├── build_windows.bat           # Windows 打包脚本
├── build_unix.sh               # macOS/Linux 打包脚本
├── pyinstaller_config.spec     # PyInstaller 配置模板
├── BUILD.md                    # 打包教程文档
├── README.md                   # 项目说明文档
└── LICENSE                     # MIT 许可证
```

## 🔍 故障排查

### 问题 1: 提示"文件不存在"

**原因**: VS Code 未安装或路径不标准

**解决方案**:
- 确认已安装 VS Code
- Windows 用户检查 `%APPDATA%\Code` 是否存在
- macOS 用户检查 `~/Library/Application Support/Code` 是否存在
- Linux 用户检查 `~/.config/Code` 是否存在

### 问题 2: 运行后仍无法登录新账号

**解决方案**:
1. 确认完全退出了 VS Code（检查任务管理器）
2. 删除浏览器中 AugmentCode 相关的 Cookie
3. 清除浏览器缓存
4. 重启电脑后再试

### 问题 3: 权限错误

**Windows 解决方案**:
- 以管理员身份运行命令提示符
- 右键 `index.py` → 以管理员身份运行

**macOS/Linux 解决方案**:
```bash
sudo python3 index.py
```

## ❓ 常见问题

**Q: 这个工具安全吗？**

A: 完全安全。本项目完全开源，您可以审查所有源代码。工具仅修改本地配置文件，不涉及网络通信。所有修改前都会创建备份。

**Q: 备份文件在哪里？**

A: 备份文件与原文件在同一目录，格式为 `原文件名.bak.时间戳`。例如：
- `storage.json.bak.1640000000`
- `state.vscdb.bak.1640000000`

**Q: 如何恢复备份？**

A: 删除修改后的文件，将备份文件重命名为原文件名即可。例如：
```bash
# 恢复 storage.json
rm storage.json
mv storage.json.bak.1640000000 storage.json
```

**Q: 支持哪些操作系统？**

A: 支持 Windows、macOS、Linux 三大平台。Python 3.10+ 即可运行。

**Q: 会影响其他 VS Code 插件吗？**

A: 不会。本工具仅清理 AugmentCode 相关数据，不影响其他插件。

## 贡献

欢迎提交 Issue 和 Pull Request 来帮助改进这个项目。

## 📜 免责声明

本工具仅供学习和个人使用。使用本工具造成的任何后果由用户自行承担。建议使用前仔细阅读代码并理解其工作原理。

- ✅ 仅用于个人设备上重置 AugmentCode 登录状态
- ✅ 使用前会自动创建备份文件
- ❌ 不用于绕过任何服务条款或商业限制
- ❌ 不保证在所有环境下都能正常工作

## 许可证

此项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

---

# <a name="english"></a>English Version

AugmentCode Reset is a tool for cleaning AugmentCode-related data, allowing unlimited logins with different accounts on the same computer while avoiding account lockouts.

## Features

- 📝 Telemetry ID Modification
  - Reset device ID and machine ID
  - Automatic backup of original data
  - Generate new random IDs

- 🗃️ Database Cleanup
  - Clean specific records in SQLite database
  - Automatic database file backup
  - Remove records containing 'augment' keyword

- 💾 Workspace Storage Management
  - Clean workspace storage files
  - Automatic workspace data backup

## Installation

1. Ensure Python 3.10 or above is installed on your system
2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/augmentcode-reset.git
   cd augmentcode-reset
   ```

## ⚠️ Important Notes

**Before using, please note:**

1. ⚡ **Backup Important**: This tool automatically creates backups, but it's still recommended to manually backup important data
2. 🚫 **Complete Exit**: You must completely exit VS Code before use, ensuring no related processes are running
3. 🔄 **Personal Use Only**: This tool is only for resetting login status on personal devices, do not use for other purposes
4. 📁 **Recoverability**: All modifications can be restored through backup files (backup file format: `*.bak.<timestamp>`)

## Usage

1. Exit the AugmentCode plugin
2. Completely close VS Code
3. Run the script:

```bash
python index.py
```

4. Restart VS Code
5. Log in to the AugmentCode plugin with a new email

## 🔨 Building from Source

If you want to build executables yourself, please refer to [BUILD.md](BUILD.md) for detailed cross-platform packaging instructions.

### Quick Build

**Windows:**
```batch
# Double-click to run or execute in command line
build_windows.bat
```

**macOS/Linux:**
```bash
# Add execute permission
chmod +x build_unix.sh

# Run the build script
./build_unix.sh
```

The built executable will be located in the `dist/` directory.

## Project Structure

```
augmentcode-reset/
├── index.py                    # Main program entry
├── augutils/                   # AugmentCode utilities module
│   ├── __init__.py
│   ├── json_modifier.py        # JSON file modification tool
│   ├── sqlite_modifier.py      # SQLite database modification tool
│   └── workspace_cleaner.py    # Workspace cleanup tool
├── utils/                      # Common utilities module
│   ├── __init__.py
│   ├── paths.py                # Cross-platform path management
│   └── device_codes.py         # ID generation tool
├── build_windows.bat           # Windows build script
├── build_unix.sh               # macOS/Linux build script
├── pyinstaller_config.spec     # PyInstaller configuration template
├── BUILD.md                    # Build instructions
├── README.md                   # Project documentation
└── LICENSE                     # MIT License
```

## 🔍 Troubleshooting

### Issue 1: "File not found" error

**Cause**: VS Code is not installed or path is non-standard

**Solutions**:
- Confirm VS Code is installed
- Windows users check if `%APPDATA%\Code` exists
- macOS users check if `~/Library/Application Support/Code` exists
- Linux users check if `~/.config/Code` exists

### Issue 2: Still unable to login with new account after running

**Solutions**:
1. Confirm VS Code is completely closed (check task manager)
2. Delete AugmentCode-related cookies in browser
3. Clear browser cache
4. Restart computer and try again

### Issue 3: Permission error

**Windows Solutions**:
- Run command prompt as administrator
- Right-click `index.py` → Run as administrator

**macOS/Linux Solutions**:
```bash
sudo python3 index.py
```

## ❓ FAQ

**Q: Is this tool safe?**

A: Completely safe. This project is fully open source, you can review all source code. The tool only modifies local configuration files, no network communication involved. All modifications are backed up before changes.

**Q: Where are the backup files?**

A: Backup files are in the same directory as the original files, with format `original_filename.bak.timestamp`. For example:
- `storage.json.bak.1640000000`
- `state.vscdb.bak.1640000000`

**Q: How to restore from backup?**

A: Delete the modified file and rename the backup file to the original filename. For example:
```bash
# Restore storage.json
rm storage.json
mv storage.json.bak.1640000000 storage.json
```

**Q: Which operating systems are supported?**

A: Supports Windows, macOS, and Linux. Requires Python 3.10+.

**Q: Will it affect other VS Code extensions?**

A: No. This tool only cleans AugmentCode-related data and does not affect other extensions.

## Contributing

Issues and Pull Requests are welcome to help improve this project.

## 📜 Disclaimer

This tool is for learning and personal use only. Users are responsible for any consequences of using this tool. It is recommended to carefully read the code and understand how it works before use.

- ✅ Only for resetting AugmentCode login status on personal devices
- ✅ Automatically creates backup files before modifications
- ❌ Not for bypassing any terms of service or commercial restrictions
- ❌ Not guaranteed to work in all environments

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details. 
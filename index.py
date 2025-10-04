from utils.paths import get_home_dir, get_app_data_dir, get_storage_path, get_db_path, get_machine_id_path,get_workspace_storage_path
from augutils.json_modifier import modify_telemetry_ids
from augutils.sqlite_modifier import clean_augment_data
from augutils.workspace_cleaner import clean_workspace_storage

if __name__ == "__main__":
    print("System Paths:")
    print(f"Home Directory: {get_home_dir()}")
    print(f"App Data Directory: {get_app_data_dir()}")
    print(f"Storage Path: {get_storage_path()}")
    print(f"DB Path: {get_db_path()}")
    print(f"Machine ID Path: {get_machine_id_path()}")
    print(f"Workspace Storage Path: {get_workspace_storage_path()}")

    print("\n" + "="*50)
    print("Step 1: Modifying Telemetry IDs")
    print("="*50)
    result = modify_telemetry_ids()

    if result.get('skipped'):
        print(f"⚠️  SKIPPED: {result['reason']}")
        print("   This step requires VS Code to be installed.")
    else:
        print("✓ Backup created at:")
        print(f"  - Storage backup: {result['storage_backup_path']}")
        if result['machine_id_backup_path']:
            print(f"  - Machine ID backup: {result['machine_id_backup_path']}")

        print("\n✓ Old IDs:")
        print(f"  - Machine ID: {result['old_machine_id']}")
        print(f"  - Device ID: {result['old_device_id']}")

        print("\n✓ New IDs:")
        print(f"  - Machine ID: {result['new_machine_id']}")
        print(f"  - Device ID: {result['new_device_id']}")

    print("\n" + "="*50)
    print("Step 2: Cleaning SQLite Database")
    print("="*50)
    db_result = clean_augment_data()

    if db_result.get('skipped'):
        print(f"⚠️  SKIPPED: {db_result['reason']}")
        print("   This step requires VS Code to be installed.")
    else:
        print(f"✓ Database backup created at: {db_result['db_backup_path']}")
        print(f"✓ Deleted {db_result['deleted_rows']} rows containing 'augment'")

    print("\n" + "="*50)
    print("Step 3: Cleaning Workspace Storage")
    print("="*50)
    ws_result = clean_workspace_storage()

    if ws_result.get('skipped'):
        print(f"⚠️  SKIPPED: {ws_result['reason']}")
        print("   This step requires VS Code to be installed.")
    else:
        print(f"✓ Workspace backup created at: {ws_result['backup_path']}")
        print(f"✓ Deleted {ws_result['deleted_files_count']} files from workspace storage")

    print("\n" + "="*50)
    print("Summary")
    print("="*50)

    # Count skipped steps
    skipped_count = sum([
        result.get('skipped', False),
        db_result.get('skipped', False),
        ws_result.get('skipped', False)
    ])

    if skipped_count == 3:
        print("⚠️  All steps were skipped (VS Code not found)")
        print("   This tool requires VS Code to be installed to work.")
        print("   Please install VS Code and try again.")
    elif skipped_count > 0:
        print(f"⚠️  {skipped_count} step(s) were skipped")
        print("✓  Other steps completed successfully")
        print("\n   You can now run VS Code and login with a new email.")
    else:
        print("✓  All steps completed successfully!")
        print("   Now you can run VS Code and login with a new email.")
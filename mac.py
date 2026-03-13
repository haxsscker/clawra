#!/usr/bin/env python3
from pyicloud import PyiCloudService
import json, sys

def main():
    apple_id  = input("Apple ID: ")
    password  = input("密码(App专用密码): ")

    print("\n🔐 正在登录...")
    api = PyiCloudService(apple_id, password)

    # ── 双重认证处理 ──────────────────────────────
    if api.requires_2fa:
        print("📱 需要双重认证")
        code = input("请输入设备上显示的6位验证码: ")
        if not api.validate_2fa_code(code):
            print("❌ 验证码错误")
            sys.exit(1)
        print("✅ 验证成功")

    elif api.requires_2sa:
        print("📱 需要两步验证")
        devices = api.trusted_devices
        for i, d in enumerate(devices):
            print(f"  [{i}] {d.get('deviceName', '手机号码')}: {d.get('phoneNumber','')}")
        idx = int(input("选择设备编号: "))
        device = devices[idx]
        if not api.send_verification_code(device):
            print("❌ 发送失败")
            sys.exit(1)
        code = input("请输入收到的验证码: ")
        if not api.validate_verification_code(device, code):
            print("❌ 验证码错误")
            sys.exit(1)

    # ── 获取所有设备 ──────────────────────────────
    print(f"\n{'='*55}")
    print(f"  账号 {apple_id} 下的所有设备")
    print(f"{'='*55}")

    for i, device in enumerate(api.devices):
        try:
            status   = device.status()
            location = device.location()

            name     = status.get('name', '未知设备')
            model    = status.get('deviceDisplayName', 'N/A')
            battery  = status.get('batteryLevel', 0)
            charging = status.get('batteryStatus', '')
            online   = status.get('deviceStatus') == '200'

            bat_icon = '🔋' if charging != 'Charging' else '⚡'
            net_icon = '🟢' if online else '🔴'

            print(f"\n[{i+1}] {net_icon} {name}")
            print(f"     型号:  {model}")
            print(f"     电量:  {bat_icon} {battery*100:.0f}%")
            print(f"     状态:  {'在线' if online else '离线'}")

            if location:
                lat  = location.get('latitude')
                lon  = location.get('longitude')
                acc  = location.get('horizontalAccuracy', 0)
                ts   = location.get('timeStamp', 0)

                from datetime import datetime
                time_str = datetime.fromtimestamp(ts/1000).strftime('%Y-%m-%d %H:%M:%S') \
                           if ts else '未知'

                print(f"     纬度:  {lat}")
                print(f"     经度:  {lon}")
                print(f"     精度:  ±{acc:.0f}米")
                print(f"     更新:  {time_str}")
                print(f"     地图:  https://maps.apple.com/?ll={lat},{lon}&z=16")
            else:
                print(f"     位置:  ❓ 无法获取（设备离线或位置未开启）")

        except Exception as e:
            print(f"     ⚠️  获取失败: {e}")

    print(f"\n{'='*55}")

    # ── 操作菜单 ──────────────────────────────────
    while True:
        print("\n操作:")
        print("  p <编号>  播放声音")
        print("  l <编号>  标记丢失")
        print("  r         刷新位置")
        print("  q         退出")
        cmd = input("\n> ").strip().split()

        if not cmd:
            continue

        if cmd[0] == 'q':
            break

        elif cmd[0] == 'r':
            main()
            break

        elif cmd[0] == 'p' and len(cmd) > 1:
            idx = int(cmd[1]) - 1
            dev = list(api.devices)[idx]
            dev.play_sound()
            print(f"🔊 已向 {list(api.devices)[idx].status().get('name')} 发送播放声音指令")

        elif cmd[0] == 'l' and len(cmd) > 1:
            idx    = int(cmd[1]) - 1
            dev    = list(api.devices)[idx]
            number = input("联系电话: ")
            msg    = input("留言信息: ")
            dev.lost_device(number=number, text=msg)
            print("✅ 已标记为丢失模式")

if __name__ == '__main__':
    main()

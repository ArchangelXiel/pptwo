from pathlib import Path
import json


file_path = Path(__file__).parent / 'sample-data.json'


with open(file_path, 'r') as file:
    data = json.load(file)


col_dn = 50
col_desc = 20
col_speed = 8
col_mtu = 6

print("Interface Status")
print("=" * (col_dn + col_desc + col_speed + col_mtu + 3))
print(f"{'DN':<{col_dn}} {'Description':<{col_desc}} {'Speed':<{col_speed}} {'MTU':<{col_mtu}}")
print(f"{'-' * col_dn} {'-' * col_desc} {'-' * col_speed} {'-' * col_mtu}")


for item in data.get("imdata", []):
    attrs = item.get("l1PhysIf", {}).get("attributes", {})
    dn = attrs.get("dn", "")
    desc = attrs.get("descr", "")
    speed = attrs.get("speed", "")
    mtu = attrs.get("mtu", "")
    print(f"{dn:<{col_dn}} {desc:<{col_desc}} {speed:<{col_speed}} {mtu:<{col_mtu}}")
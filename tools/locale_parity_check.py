#!/usr/bin/env python3
"""Key-parity check for data/locales.lua: every locale block must carry exactly
the base key set, with no value equal to enUS except documented exceptions."""
import re, sys

src = open("data/locales.lua", encoding="utf-8").read()

base_m = re.search(r"local L = \{(.*?)\n\}", src, re.S)
base = dict(re.findall(r'\["([A-Z_]+)"\]\s*=\s*"((?:[^"\\]|\\.)*)"', base_m.group(1)))

# Split blocks by locale guards
blocks = {}
guard_iter = list(re.finditer(r'(?:if|elseif) locale == "(\w+)"(?: or locale == "(\w+)")? then', src))
for i, g in enumerate(guard_iter):
    start = g.end()
    end = guard_iter[i+1].start() if i+1 < len(guard_iter) else src.index("\nend\n\nLOLLU.L")
    name = g.group(1) + (("/" + g.group(2)) if g.group(2) else "")
    blocks[name] = dict(re.findall(r'L\["([A-Z_]+)"\]\s*=\s*"((?:[^"\\]|\\.)*)"', src[start:end]))

EXCEPTIONS = {"RGX_MODS_PREFIX"}  # brand string kept English by MR decision
# Documented locale-invariant cognates (correct native word identical to enUS):
COGNATE_EXCEPTIONS = {
    ("deDE","STATUS_HEADER"), ("deDE","STATUS_STATUS"), ("deDE","STATUS_VERSION"),
    ("esES/esMX","NO"), ("itIT","NO"), ("ptBR","STATUS_STATUS"),
}
ok = True
print(f"base keys: {len(base)}")
for name in ["ruRU","deDE","frFR","esES/esMX","itIT","koKR","ptBR","ptPT","zhCN","zhTW"]:
    blk = blocks.get(name, {})
    missing = set(base) - set(blk)
    extra = set(blk) - set(base)
    equal = {k for k in blk if k in base and blk[k] == base[k] and k not in EXCEPTIONS
             and (name, k) not in COGNATE_EXCEPTIONS}
    fmt_bad = {k for k in blk if k in base and blk[k].count("%s") != base[k].count("%s")}
    status = "OK" if not (missing or extra or equal or fmt_bad) else "FAIL"
    if status == "FAIL":
        ok = False
    print(f"{name}: keys={len(blk)} missing={sorted(missing)} extra={sorted(extra)} equal-to-enUS={sorted(equal)} fmt-mismatch={sorted(fmt_bad)} -> {status}")
sys.exit(0 if ok else 1)

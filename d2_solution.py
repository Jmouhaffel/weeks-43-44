#!/usr/bin/env python3
"""
Deliverable 2 — Single-file solution
Authors:
- Joudy Mouhaffel
- Rami Alter (alter ego for solo workflow)
"""

import argparse
import sys
from typing import List, Any

def parse_args(argv: List[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="D2 single-file program.")
    p.add_argument("--input", type=str, required=False, help="Path to input file.")
    p.add_argument("--mode", type=str, default="fast", choices=["fast", "safe"])
    p.add_argument("--verbose", action="store_true")
    return p.parse_args(argv)

def load_data(path: str | None) -> List[str]:
    # يقرأ من ملف إذا path موجود، أو من stdin إذا ما في ملف
    if path:
        with open(path, "r", encoding="utf-8") as f:
            return [line.rstrip("\n") for line in f]
    data = sys.stdin.read().splitlines()
    return data

def core_logic(lines: List[str], mode: str = "fast") -> Any:
    # مؤقتاً: fast = أحرف كبيرة، safe = ترتيب
    if mode == "fast":
        return [s.upper() for s in lines]
    return sorted(lines)

def format_output(result: Any) -> str:
    if isinstance(result, list):
        return "\n".join(result)
    return str(result)

def main(argv: List[str] | None = None) -> int:
    args = parse_args(argv)
    lines = load_data(args.input)
    out = format_output(core_logic(lines, mode=args.mode))
    print(out)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

# TODO(Rami): refine core_logic later
# TODO(Rami): refine core_logic later

#!/usr/bin/env python3
"""Convert `noctalia theme --both` JSON on stdin to Noctalia's m* custom-palette schema.

Usage:
  noctalia theme IMAGE --scheme m3-rainbow --both | ./make-palette.py OUT.json
"""
import json
import sys

out = sys.argv[1]
data = json.load(sys.stdin)


def convert(c):
    return {
        "mError": c["error"],
        "mHover": c["hover"],
        "mOnError": c["on_error"],
        "mOnHover": c["on_hover"],
        "mOnPrimary": c["on_primary"],
        "mOnSecondary": c["on_secondary"],
        "mOnSurface": c["on_surface"],
        "mOnSurfaceVariant": c["on_surface_variant"],
        "mOnTertiary": c["on_tertiary"],
        "mOutline": c["outline"],
        "mPrimary": c["primary"],
        "mSecondary": c["secondary"],
        "mShadow": c["shadow"],
        "mSurface": c["surface"],
        "mSurfaceVariant": c["surface_variant"],
        "mTertiary": c["tertiary"],
        "terminal": {
            "background": c["terminal_background"],
            "bright": {
                "black": c["terminal_bright_black"],
                "blue": c["terminal_bright_blue"],
                "cyan": c["terminal_bright_cyan"],
                "green": c["terminal_bright_green"],
                "magenta": c["terminal_bright_magenta"],
                "red": c["terminal_bright_red"],
                "white": c["terminal_bright_white"],
                "yellow": c["terminal_bright_yellow"],
            },
            "cursor": c["terminal_cursor"],
            "cursorText": c["terminal_cursor_text"],
            "foreground": c["terminal_foreground"],
            "normal": {
                "black": c["terminal_normal_black"],
                "blue": c["terminal_normal_blue"],
                "cyan": c["terminal_normal_cyan"],
                "green": c["terminal_normal_green"],
                "magenta": c["terminal_normal_magenta"],
                "red": c["terminal_normal_red"],
                "white": c["terminal_normal_white"],
                "yellow": c["terminal_normal_yellow"],
            },
            "selectionBg": c["terminal_selection_bg"],
            "selectionFg": c["terminal_selection_fg"],
        },
    }


result = {"dark": convert(data["dark"]), "light": convert(data["light"])}
with open(out, "w", encoding="utf-8") as handle:
    json.dump(result, handle, separators=(",", ":"))
    handle.write("\n")

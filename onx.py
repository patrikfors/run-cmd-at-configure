#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
# ]
# ///

import shutil
import sys
import time

frames = [
    "[=     ]",
    "[ =    ]",
    "[  =   ]",
    "[   =  ]",
    "[    = ]",
    "[     =]",
    "[    = ]",
    "[   =  ]",
    "[  =   ]",
    "[ =    ]",
]

if __name__ == "__main__":
    try:
        for _ in range(5):
            for frame in frames:
                sys.stdout.write(f"\rRunning command at configure {frame}")
                sys.stdout.flush()
                time.sleep(0.15)
        sys.stdout.write("\r                                        \n")
        shutil.copy("foo.cpp", "bar.cpp")
        print("File copied.")
    except KeyboardInterrupt:
        sys.stdout.write("\rInterrupted.                                 \n")
        sys.stdout.flush()
        sys.exit(1)

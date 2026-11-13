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
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <target path>")
        sys.exit(1)
    target_path = sys.argv[1]
    cmake_phase = "build" if len(sys.argv) > 2 else "configure"
    print(f"Generating {target_path}.")
    
    try:
        for _ in range(5):
            for frame in frames:
                sys.stdout.write(f"\rRunning command at {cmake_phase} {frame}")
                sys.stdout.flush()
                time.sleep(0.15)
        sys.stdout.write("\r                                        \n")
        shutil.copy("foo.cpp.in", target_path)
        print("File copied.")
    except KeyboardInterrupt:
        sys.stdout.write("\rInterrupted.                                 \n")
        sys.stdout.flush()
        sys.exit(1)

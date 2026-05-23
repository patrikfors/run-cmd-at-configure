Testing how to call an executable during cmake configure stage.

CMakeLists.txt adds an executable that builds from source file bar.cpp, which doesn't exist unless the python script is run first.

```
cmake -S . -B build
```

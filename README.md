Testing how to call an executable during cmake configure stage.

CMakeLists.txt adds an executable that builds from source file bar.cpp, which doesn't exist unless the python script is run first.

This was made just to test that I could run something during configure stage. A real application
of this would of course also check if the run is necessary.

```
cmake -B build . -G Ninja   # will generate bar.cpp
cd build
ninja                       # builds onx, no file generation
ninja onx2                  # generates baz.cpp, builds onx2
```

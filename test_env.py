# python
import sys, os
print("exe:", sys.executable)
print("cwd:", os.getcwd())
try:
    import pygame
    print("pygame version:", pygame.__version__)
except Exception as e:
    print("pygame import error:", repr(e))
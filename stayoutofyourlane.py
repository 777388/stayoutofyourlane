import sys
import linecache
import _locale
try:
    _locale.setlocale("C:\Windows\System32\agentactivationruntime.dll")
    linecache.getline(sys.argv[1])
except:
    _locale.setlocale.__delattr__
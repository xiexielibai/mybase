import os

BASE = "/Users/baby/Downloads/basesoft"

check = ["bin/autoconf",
         "bin/pkg-config",
         "bin/openssl",
         "include/freetype2",
         "python/bin/python3",
         "mysql/bin/mysqld"]

for f in check:
    t = os.path.join("/usr/local", f)
if not os.path.exists(t):
    raise IOError("not find")

if not os.path.exists(
        f"{BASE}/jdk8/corretto-8-8.352.08.1/build/macosx-x86_64-normal-server-release/jdk/bin/java"):
    raise IOError("not find")

if not os.path.exists(
        f"{BASE}/jdk11/corretto-11-11.0.17.8.1/build/macosx-x86_64-normal-server-release/jdk/bin/java"):
    raise IOError("not find")

if not os.path.exists(
        f"{BASE}/jdk17/corretto-17-17.0.5.8.1/build/macosx-x86_64-server-release/jdk/bin/java"):
    raise IOError("not find")

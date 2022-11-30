import os
import shutil

TARGET = "/Users/baby/Downloads/basesoft"

map = {
    "pkg-config-0.29.2.tar.gz": ("pkg-config", "sh configure --with-internal-glib", False),
    "redis-7.0.5.tar.gz": ("redis", False, True),
    "lua-5.4.4.tar.gz": ("lua", False, True),
    "autoconf-2.69.tar.gz": ("autoconf", "sh configure", False),
    "freetype-2.12.1.tar.gz": ("freetype", "sh configure", False),
    "openssl-1.1.1s.tar.gz": ("openssl", "./config", False)
}

os.chdir("/usr/local")
os.system("sudo -S rm -rf *")

os.chdir(TARGET)

for key, value in map.items():
    to = value[0]
    folder = os.path.join(TARGET, to)
    if (os.path.exists(folder)):
        shutil.rmtree(folder)
    os.system(f"mkdir {to}")
    os.system(f"tar -zxf {key} -C {to}")

for key, value in map.items():
    os.chdir(os.path.join(TARGET, value[0], key.replace(".tar.gz", "")))
    os.system("pwd")
    if value[1]:
        os.system(value[1])
        os.system("make")
        os.system("sudo -S make install")
    else:
        os.system("make")
        if value[2]:
            os.system("make test")



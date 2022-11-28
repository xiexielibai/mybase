import os
import shutil

TARGET = "/Users/baby/Downloads/basesoft"

map = {

    # "Python-3.11.0.tar.xz": ("python3", "sh configure --prefix=/usr/local/python --enable-optimizations", True),

    # "mysql-boost-5.7.39.tar.gz": ("mysql",
    #                               f"cmake -DCMAKE_INSTALL_PREFIX=/usr/local/mysql -DMYSQL_UNIX_ADDR=/tmp/mysql.sock -DDEFAULT_CHARSET=utf8 -DDEFAULT_COLLATION=utf8_general_ci -DWITH_INNOBASE_STORAGE_ENGINE=1-DWITH_ARCHIVE_STORAGE_ENGINE=1 -DWITH_BLACKHOLE_STORAGE_ENGINE=1 -DWITH_PARTITION_STORAGE_ENGINE=1 -DENABLED_LOCAL_INFILE=1 -DMYSQL_USER=_mysql -DMYSQL_TCP_PORT=3306 -DMYSQL_DATADIR=/usr/local/mysql/db_data -DDOWNLOAD_BOOST=1 -DWITH_BOOST={TARGET}/mysql/mysql-5.7.39/boost",
    #                               True),

    "corretto-8-8.352.08.1.tar.gz": ("jdk8",
                                     "sh configure --with-boot-jdk=../../amazon-corretto-8.jdk/Contents/Home --with-freetype-include=/usr/local/include/freetype2 --with-freetype-lib=/usr/local/lib",
                                     False),

    "corretto-11-11.0.17.8.1.tar.gz": (
        "jdk11", "sh configure --with-boot-jdk=../../amazon-corretto-11.jdk/Contents/Home", False),

    "corretto-17-17.0.5.8.1.tar.gz": (
        "jdk17", "sh configure --with-boot-jdk=../../amazon-corretto-17.jdk/Contents/Home", False)

}

os.chdir(TARGET)

for key, value in map.items():
    to = value[0]
    folder = os.path.join(TARGET, to)
    if (os.path.exists(folder)):
        shutil.rmtree(folder)
    os.system(f"mkdir {to}")
    os.system(f"tar -zxf {key} -C {to}")

for key, value in map.items():
    os.chdir(os.path.join(TARGET, value[0], key.replace(".tar.gz", "").replace(".tar.xz", "").replace("boost-", "")))
    os.system("pwd")
    if value[1]:
        os.system("export PATH=/Applications/CMake.app/Contents/bin:$PATH && " + value[1])
        os.system("make")
        os.system("make images")
        if value[2]:
            os.system("sudo -S make install")

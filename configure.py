import os
import shutil

TARGET = "/Users/keke/Downloads/basesoft"

python = "sh configure --prefix=/usr/local/python --enable-optimizations"
mysql = f"cmake -DCMAKE_INSTALL_PREFIX=/usr/local/mysql -DMYSQL_UNIX_ADDR=/tmp/mysql.sock -DDEFAULT_CHARSET=utf8 -DDEFAULT_COLLATION=utf8_general_ci -DWITH_INNOBASE_STORAGE_ENGINE=1-DWITH_ARCHIVE_STORAGE_ENGINE=1 -DWITH_BLACKHOLE_STORAGE_ENGINE=1 -DWITH_PARTITION_STORAGE_ENGINE=1 -DENABLED_LOCAL_INFILE=1 -DMYSQL_USER=_mysql -DMYSQL_TCP_PORT=3306 -DMYSQL_DATADIR=/usr/local/mysql/db_data -DDOWNLOAD_BOOST=1 -DWITH_BOOST={TARGET}/mysql/mysql-5.7.39/boost"
jdk8 = "sh configure --with-boot-jdk=../../jdk/amazon-corretto-8.jdk/Contents/Home --with-freetype-include=/usr/local/include/freetype2 --with-freetype-lib=/usr/local/lib"
jdk11 = "sh configure --with-boot-jdk=../../jdk/amazon-corretto-11.jdk/Contents/Home"
jdk17 = "sh configure --with-boot-jdk=../../jdk/amazon-corretto-17.jdk/Contents/Home"

app = {

    "Python-3.11.0.tar.xz": ("python3", python),
    # "mysql-boost-5.7.39.tar.gz": ("mysql", mysql),
    # "corretto-8-8.352.08.1.tar.gz": ("jdk8", jdk8),
    # "corretto-11-11.0.17.8.1.tar.gz": ("jdk11", jdk11),
    # "corretto-17-17.0.5.8.1.tar.gz": ("jdk17", jdk17)

}

os.chdir(TARGET)

for key, value in app.items():
    to = value[0]
    folder = os.path.join(TARGET, to)
    if (os.path.exists(folder)):
        shutil.rmtree(folder)
    os.system(f"mkdir {to}")
    os.system(f"tar -zxf {key} -C {to}")

for key, value in app.items():
    name = key.replace(".tar.gz", "").replace(".tar.xz", "").replace("boost-", "")
    os.chdir(os.path.join(TARGET, value[0], name))
    if value[1]:
        os.system(value[1])

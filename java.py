import os

TARGET = "/Users/baby/Project/"
MAVEN = "/Applications/IntelliJ\ IDEA\ CE.app/Contents/plugins/maven/lib/maven3"
JDK8 = "/Users/baby/Downloads/basesoft/jdk/amazon-corretto-8.jdk/Contents/Home"

maven_projects = ["nacos-2.1.2", "clojure-1.11.1", "zookeeper-3.5.8"]

JAVA_PATH = "export PATH=$JAVA_HOME/bin:$PATH"
MAVEN_PATH = "export PATH=$JAVA_HOME/bin:$M2_HOME/bin:$PATH"

for m in maven_projects:
    os.chdir(f"{TARGET}{m}")
    os.system(f"export JAVA_HOME={JDK8} && export M2_HOME={MAVEN} && {MAVEN_PATH} && mvn clean package -DskipTests")

gradle_projects = ["springboot-2.6.6"]
for g in gradle_projects:
    os.chdir(f"{TARGET}{g}")
    os.system(f"export JAVA_HOME={JDK8} && {JAVA_PATH} && sh gradlew build -x test")

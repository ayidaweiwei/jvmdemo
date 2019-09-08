#!/usr/bin/env sh
java -jar lib/jvmshare-0.0.1-SNAPSHOT.jar >> /tmp/service.log 2>&1 &
java -jar lib/arthas-boot-demo-3.1.2-SNAPSHOT.jar &
tail -f /tmp/service.log
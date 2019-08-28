FROM openjdk:8-jdk-alpine

EXPOSE 8888

ADD build/libs/jvmshare-0.0.1-SNAPSHOT.jar app.jar
# copy arthas
COPY --from=ayidaweiwei/arthas:latest /opt/arthas /opt/arthas

#option 1   to avoid pid = 1

# Add Tini
RUN apk add --no-cache tini
#Tini is now available at /sbin/tini
ENTRYPOINT ["/sbin/tini", "--"]
#Run demo program under Tini
CMD ["java","-jar","/app.jar"]


#option 2 to avoid pid = 1

#CMD ["/bin/sh","java -jar /app.jar"]










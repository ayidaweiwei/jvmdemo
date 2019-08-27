FROM openjdk:8-jdk-alpine

EXPOSE 8888

ADD app.jar app.jar
# copy arthas
COPY --from=ayidaweiwei/arthas:latest /opt/arthas /opt/arthas

#option 1   to avoid pid = 1

## Add Tini
#RUN apk add --no-cache tini
##Tini is now available at /sbin/tini
#ENTRYPOINT ["/sbin/tini", "--"]
##Run demo program under Tini
#CMD ["java","-jar","/opt/arthas/arthas-demo.jar"]


#option 2 to avoid pid = 1

CMD ["/bin/sh","java -jar /app.jar"]










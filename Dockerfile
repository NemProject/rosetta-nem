FROM ubuntu:20.04

RUN apt-get update \
  && apt-get -y install openjdk-8-jdk-headless curl \
  && rm -rf /var/lib/apt/lists/*

RUN curl -L http://bob.nem.ninja/nis-0.6.97.tgz -o nis-0.6.97.tgz \
  && tar -xzf nis-0.6.97.tgz \
  && rm -rf nis-0.6.97.tgz

RUN apt-get update && apt-get install -y ca-certificates && update-ca-certificates

RUN mkdir -p /app \
  && mv /package /app \
  && chown -R nobody:nogroup /app

COPY config/config.properties /app

WORKDIR /app

CMD [ "/usr/bin/java", "-Xms6G", "-Xmx6G", "-cp", "/app/*:package/nis/*:package/libs/*", "org.nem.deploy.CommonStarter" ]



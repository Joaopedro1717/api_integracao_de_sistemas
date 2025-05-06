# Build stage - usando a mesma versão do JDK que você definiu no toolchain
FROM gradle:8.6-jdk21-jammy AS build
WORKDIR /app

# Cache de dependências (executa apenas se build.gradle ou settings.gradle mudarem)
COPY build.gradle settings.gradle ./
RUN gradle dependencies --no-daemon

# Copia o resto do código e faz o build
COPY src ./src
RUN gradle build --no-daemon -x test

# Run stage - usando JRE mais leve
FROM eclipse-temurin:21-jre-jammy
WORKDIR /app

# Copia o JAR construído
COPY --from=build /app/build/libs/*.jar app.jar

# Configurações de saúde e execução
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:8080/actuator/health || exit 1

EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
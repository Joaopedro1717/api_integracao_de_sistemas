package com.rebelatto.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.redis.connection.RedisConnectionFactory;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.serializer.GenericJackson2JsonRedisSerializer;
import org.springframework.data.redis.serializer.StringRedisSerializer;

@Configuration
public class RedisConfig {

    @Bean
    public RedisTemplate<String, Object> redisTemplate(RedisConnectionFactory connectionFactory) {
        RedisTemplate<String, Object> template = new RedisTemplate<>();
        template.setConnectionFactory(connectionFactory);

        // Serializer para chaves (String)
        template.setKeySerializer(new StringRedisSerializer());

        // Serializer para valores (JSON)
        template.setValueSerializer(new GenericJackson2JsonRedisSerializer());

        // Serializer para hash keys
        template.setHashKeySerializer(new StringRedisSerializer());

        // Serializer para hash values
        template.setHashValueSerializer(new GenericJackson2JsonRedisSerializer());

        return template;
    }
}
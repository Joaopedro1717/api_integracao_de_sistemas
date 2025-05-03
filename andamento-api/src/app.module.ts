import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { TypeOrmModule } from '@nestjs/typeorm';
import { ConfigModule, ConfigService } from '@nestjs/config';
import { Usuario } from './models/usuario';
import { Equipe } from './models/equipe';
import { Tarefas } from './models/tarefas';
import { Andamento } from './models/andamento';

@Module({
  imports: [
    ConfigModule.forRoot({
      isGlobal: true,
    }),
    TypeOrmModule.forRootAsync({
        imports: [ConfigModule],
        inject: [ConfigService],
        useFactory: (ConfigService: ConfigService) => ({
          type: 'postgres',
          host: ConfigService.get('DB_HOST'),
          port: ConfigService.get('DB_PORT'),
          username: ConfigService.get('DB_USERNAME'),
          password: ConfigService.get('DB_PASSWORD'),
          database: ConfigService.get('DB_NAME'),
          entities: [Usuario, Equipe, Tarefas, Andamento],
          synchronize: true
        })
    }),
    TypeOrmModule.forFeature([Usuario, Equipe, Tarefas, Andamento]),
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}

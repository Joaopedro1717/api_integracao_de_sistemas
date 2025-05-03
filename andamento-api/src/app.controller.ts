import { Body, Controller, Get, NotFoundException, Post } from '@nestjs/common';
import { AppService } from './app.service';
import { usuarioDTO } from './DTOs/usuarioDTO';
import { InjectRepository } from '@nestjs/typeorm';
import { Usuario } from './models/usuario';
import { Equipe } from './models/equipe';
import { Repository } from 'typeorm';


@Controller()
export class AppController {
  constructor(
    private readonly appService: AppService,
    @InjectRepository(Usuario)
    private readonly usuarioRepository: Repository<Usuario>,
    @InjectRepository(Equipe)
    private readonly equipeRepository: Repository<Equipe>,
  ) {}

  @Get()
  getHello(): string {
    return this.appService.getHello();
  }

  @Post('/createUsuario')
  async createUser(@Body() usuarioDTO: usuarioDTO) {
    const equipe = await this.equipeRepository.findOne({ where: { nome: usuarioDTO.equipe }});

    if(!equipe) { throw new NotFoundException("nenhuma equipe escontrada")}

    const newUsuario =  await this.usuarioRepository.create({
      nome: usuarioDTO.nome,
      email: usuarioDTO.email,
      cargo: usuarioDTO.cargo,
      equipe: equipe,
    });

    return this.usuarioRepository.save(newUsuario)
  }
}

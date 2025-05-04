import { Inject, Body, Controller, Get, NotFoundException, Post, Param } from '@nestjs/common';
import { AppService } from './app.service';
import { InjectRepository } from '@nestjs/typeorm';
import { Usuario } from './models/usuario';
import { Equipe } from './models/equipe';
import { Repository } from 'typeorm';
import { andamentoDTO } from './DTOs/andamentoDTO';
import { Andamento } from './models/andamento';
import { Tarefas } from './models/tarefas';
import { Cache } from 'cache-manager';
import { CACHE_MANAGER, CacheKey } from '@nestjs/cache-manager';


@Controller()
export class AppController {
  constructor(
    private readonly appService: AppService,
    @InjectRepository(Usuario)
    private readonly usuarioRepository: Repository<Usuario>,
    @InjectRepository(Equipe)
    private readonly equipeRepository: Repository<Equipe>,
    @InjectRepository(Andamento)
    private readonly andamentoRepository: Repository<Andamento>,
    @InjectRepository(Tarefas)
    private readonly tarefaRepository: Repository<Tarefas>,
    @Inject(CACHE_MANAGER) private cacheManager: Cache
  ) { }


  @Post('/notificacao-tarefa')
  async notificacao(@Body() andamentoDTO: andamentoDTO) {

    const cacheKey = `andamento:${andamentoDTO.idTarefa}`;
    const cachedMensagem = await this.cacheManager.get<string>(cacheKey);

    if (cachedMensagem) {
      return cachedMensagem;
    }

    const equipe = await this.equipeRepository.findOne({ where: { id: andamentoDTO.idEquipe } });
    const usuario = await this.usuarioRepository.findOne({ where: { id: andamentoDTO.idUsuarioResponsavel } });
    if (!equipe || !usuario) { throw new NotFoundException("Equipe ou Usuario não encontrado") }

    const tarefa = await this.tarefaRepository.findOne({ where: { id: andamentoDTO.idTarefa } });
    if (!tarefa) { throw new NotFoundException("nenhum tarefa escontrado") }

    const novaTarefa = await this.andamentoRepository.findOne({
      where: {
        tarefa: { id: andamentoDTO.idTarefa },
      },
      order: { data_criacao: 'DESC' },
      relations: ['tarefa']
    });

    let newAndamento: Andamento;

    if (!novaTarefa) {
      newAndamento = this.andamentoRepository.create({
        mensagem: `${usuario.nome} que pertence a equipe: ${equipe.nome} criou a ${tarefa.titulo}`,
        tarefa: tarefa,
        usuario: usuario,
        status_atual: tarefa.status,
        status_antigo: 'Tarefa nova',
      });

    } else {

      newAndamento = this.andamentoRepository.create({
        mensagem: `${usuario.nome} que pertence a equipe: ${equipe.nome} alterou o status da ${tarefa.titulo} de ${novaTarefa.status_atual} para ${andamentoDTO.status}`,
        tarefa: tarefa,
        usuario: usuario,
        status_atual: andamentoDTO.status,
        status_antigo: novaTarefa.status_atual,

      });
    }


    await this.andamentoRepository.save(newAndamento);
    console.log(newAndamento.mensagem)

    return newAndamento.mensagem
  }

  @Get('/historico-tarefa/:titulo')
  async getHistoricoTarefa(@Param('titulo') titulo: string) {
    const cacheKey = `historico-tarefa-${titulo}`
    const cached = await this.cacheManager.get<string>(cacheKey);

    if (cached) { return cached }

    const historicoTarefa = await this.andamentoRepository.find({
      where: { tarefa: { titulo: titulo } },
      relations: ['usuario', 'tarefa'],
      order: { data_criacao: 'DESC' }
    });

    await this.cacheManager.set(cacheKey, historicoTarefa);

    return historicoTarefa;
  }





}


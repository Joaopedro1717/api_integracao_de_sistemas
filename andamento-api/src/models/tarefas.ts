import { Entity, Column, PrimaryGeneratedColumn, ManyToOne, JoinColumn, OneToMany } from 'typeorm';
import { Equipe } from './equipe';
import { Usuario } from './usuario';
import { Andamento } from './andamento';

@Entity('tarefas')
export class Tarefas {
    @PrimaryGeneratedColumn()
    id: number;

    @Column()
    titulo: string;

    @Column()
    descricao: string;

    @Column()
    status: string;

    @Column()
    prazo: Date;

    @ManyToOne(() => Equipe, equipe => equipe.tarefas)
    @JoinColumn({ name: 'id_equipe' })
    equipe: Equipe;

    @ManyToOne(() => Usuario, usuario => usuario.tarefasResponsaveis)
    @JoinColumn({ name: 'id_usuario_responsavel' })
    responsavel: Usuario;

    @OneToMany(() => Andamento, andamento => andamento.tarefa)
    andamentos: Andamento[];

}
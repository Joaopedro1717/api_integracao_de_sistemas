import { Entity, Column, PrimaryGeneratedColumn, ManyToOne, JoinColumn, OneToMany } from 'typeorm';
import { Equipe } from './equipe';
import { Tarefas } from './tarefas';
import { Andamento } from './andamento';

@Entity('usuarios')
export class Usuario {
    @PrimaryGeneratedColumn()
    id: number;

    @Column()
    nome: string;

    @Column()
    email: string;

    @Column()
    cargo: string;

    @ManyToOne(() => Equipe, equipe => equipe.usuarios)
    @JoinColumn({ name: 'id_equipe' })
    equipe: Equipe;

    @OneToMany(() => Tarefas, tarefa => tarefa.responsavel)
    tarefasResponsaveis: Tarefas[];

    @OneToMany(() => Andamento, andamento => andamento.usuario)
    andamentos: Andamento[];

}
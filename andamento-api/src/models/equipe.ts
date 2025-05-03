import { Entity, Column, PrimaryGeneratedColumn, ManyToOne, OneToMany } from 'typeorm';
import { Usuario } from './usuario';
import { Tarefas } from './tarefas';

@Entity('equipe')
export class Equipe {
    @PrimaryGeneratedColumn()
    id: number;

    @Column()
    nome: string;

    @OneToMany(() => Usuario, usuario => usuario.equipe)
    usuarios: Usuario[];

    @OneToMany(() => Tarefas, tarefas => tarefas.equipe)
    tarefas: Tarefas[];
}
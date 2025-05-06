import { Entity, Column, PrimaryGeneratedColumn, ManyToOne, JoinColumn } from 'typeorm';
import { Usuario } from './usuario';
import { Tarefas } from './tarefas';

@Entity('andamento')
export class Andamento {
    @PrimaryGeneratedColumn()
    id: number;

    @Column()
    mensagem: string;

    @Column()
    status_antigo: string;

    @Column()
    status_atual: string;

    @Column({ type: 'timestamp', default: () => 'CURRENT_TIMESTAMP' })
    data_criacao: Date;

    @ManyToOne(() => Usuario, usuario => usuario.andamentos)
    @JoinColumn({ name: 'id_usuario' })
    usuario: Usuario;

    @ManyToOne(() => Tarefas, tarefa => tarefa.andamentos)
    @JoinColumn({ name: 'id_tarefa' })
    tarefa: Tarefas;

}
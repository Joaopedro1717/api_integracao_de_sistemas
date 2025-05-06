import { IsNumber, IsString, IsOptional } from 'class-validator';

export class andamentoDTO {
    @IsOptional()
    @IsString()
    status_antigo?: string;
    
    @IsString()
    status: string;
    
    @IsNumber()
    idUsuarioResponsavel: number;
    
    @IsNumber()
    idEquipe: number;
    
    @IsNumber()
    idTarefa: number;
}
package com.rebelatto.dto;

import java.time.LocalDate;

public record TarefaDTO(
        Long id,
        String titulo,
        String descricao,
        String status,
        LocalDate prazo,
        Integer idEquipe,
        Integer idUsuarioResponsavel
) {}

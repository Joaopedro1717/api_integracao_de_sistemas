package com.rebelatto.controller;

import com.rebelatto.dto.TarefaDTO;
import com.rebelatto.model.Tarefa;
import com.rebelatto.service.TarefaService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

@RestController
@RequestMapping("/tarefas")
public class TarefaController {

    @Autowired
    private TarefaService tarefaService;

    @GetMapping
    public List<TarefaDTO> listarTodas() {
        return tarefaService.listarTodas()
                .stream()
                .map(this::toDTO)
                .collect(Collectors.toList());
    }

    @GetMapping("/{id}")
    public ResponseEntity<TarefaDTO> buscarPorId(@PathVariable Long id) {
        Optional<Tarefa> tarefa = tarefaService.buscarPorId(id);
        return tarefa.map(value -> ResponseEntity.ok(toDTO(value)))
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public ResponseEntity<TarefaDTO> criar(@RequestBody TarefaDTO dto) {
        Tarefa nova = tarefaService.salvar(fromDTO(dto));
        return ResponseEntity.ok(toDTO(nova));
    }

    @PutMapping("/{id}")
    public ResponseEntity<TarefaDTO> atualizar(@PathVariable Long id, @RequestBody TarefaDTO dto) {
        try {
            Tarefa atualizada = tarefaService.atualizar(id, fromDTO(dto));
            return ResponseEntity.ok(toDTO(atualizada));
        } catch (RuntimeException e) {
            return ResponseEntity.notFound().build();
        }
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deletar(@PathVariable Long id) {
        tarefaService.deletar(id);
        return ResponseEntity.noContent().build();
    }

    // Métodos de conversão entre Entity e DTO
    private TarefaDTO toDTO(Tarefa tarefa) {
        return new TarefaDTO(
                tarefa.getId(),
                tarefa.getTitulo(),
                tarefa.getDescricao(),
                tarefa.getStatus(),
                tarefa.getPrazo(),
                tarefa.getIdEquipe(),
                tarefa.getIdUsuarioResponsavel()
        );
    }

    private Tarefa fromDTO(TarefaDTO dto) {
        Tarefa tarefa = new Tarefa();
        tarefa.setId(dto.id());
        tarefa.setTitulo(dto.titulo());
        tarefa.setDescricao(dto.descricao());
        tarefa.setStatus(dto.status());
        tarefa.setPrazo(dto.prazo());
        tarefa.setIdEquipe(dto.idEquipe());
        tarefa.setIdUsuarioResponsavel(dto.idUsuarioResponsavel());
        return tarefa;
    }
}

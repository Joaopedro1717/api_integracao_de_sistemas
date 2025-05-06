package com.rebelatto.controller;

import com.rebelatto.dto.TarefaDTO;
import com.rebelatto.model.Tarefa;
import com.rebelatto.service.TarefaService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.*;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.stream.Collectors;

@RestController
@RequestMapping("/tarefas")
public class TarefaController {

    @Autowired
    private TarefaService tarefaService;

    private final RestTemplate restTemplate = new RestTemplate();

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
        TarefaDTO novaDTO = toDTO(nova);
        enviarNotificacao(novaDTO);
        return ResponseEntity.ok(novaDTO);
    }

    @PutMapping("/{id}")
    public ResponseEntity<TarefaDTO> atualizar(@PathVariable Long id, @RequestBody TarefaDTO dto) {
        try {
            Tarefa atualizada = tarefaService.atualizar(id, fromDTO(dto));
            TarefaDTO atualizadaDTO = toDTO(atualizada);
            enviarNotificacao(atualizadaDTO);
            return ResponseEntity.ok(atualizadaDTO);
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

    // Envio de notificação para a API externa
    private void enviarNotificacao(TarefaDTO dto) {
        try {
            // Criar um mapa com a estrutura que a API Nest.js espera
            Map<String, Object> payload = new HashMap<>();
            payload.put("idTarefa", dto.id());
            payload.put("status", dto.status());
            payload.put("idEquipe", dto.idEquipe());
            payload.put("idUsuarioResponsavel", dto.idUsuarioResponsavel());

            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);

            HttpEntity<Map<String, Object>> request = new HttpEntity<>(payload, headers);
            String NOTIFICACAO_API_URL = "http://localhost:3000/notificacao-tarefa";
            ResponseEntity<String> response = restTemplate.postForEntity(NOTIFICACAO_API_URL, request, String.class);

            if (!response.getStatusCode().is2xxSuccessful()) {
                System.err.println("Falha ao enviar notificação: " + response.getStatusCode());
            }

        } catch (Exception e) {
            System.err.println("Erro ao tentar notificar outra API: " + e.getMessage());
        }
    }
}

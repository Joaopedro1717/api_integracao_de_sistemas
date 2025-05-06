package com.rebelatto.service;

import com.rebelatto.model.Tarefa;
import com.rebelatto.repository.TarefaRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class TarefaService {

    @Autowired
    private TarefaRepository tarefaRepository;

    @Cacheable(value = "tarefas")
    public List<Tarefa> listarTodas() {
        return tarefaRepository.findAll();
    }


    @Cacheable(value = "tarefa", key = "#id")
    public Optional<Tarefa> buscarPorId(Long id) {
        return tarefaRepository.findById(id);
    }

    @CacheEvict(value = {"tarefas", "tarefa"}, allEntries = true)
    public Tarefa salvar(Tarefa tarefa) {
        return tarefaRepository.save(tarefa);
    }

    @CacheEvict(value = {"tarefa", "tarefas"}, key = "#id")
    public void deletar(Long id) {
        tarefaRepository.deleteById(id);
    }

    @CacheEvict(value = {"tarefa", "tarefas"}, key = "#id")
    public Tarefa atualizar(Long id, Tarefa novaTarefa) {
        if (!tarefaRepository.existsById(id)) {
            throw new RuntimeException("Tarefa não encontrada com id " + id);
        }
        novaTarefa.setId(id);
        return tarefaRepository.save(novaTarefa);
    }
}

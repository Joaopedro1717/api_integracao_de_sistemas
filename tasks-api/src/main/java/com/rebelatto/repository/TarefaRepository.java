package com.rebelatto.repository;

import com.rebelatto.model.Tarefa;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface TarefaRepository extends JpaRepository<Tarefa, Long> {
    // Aqui você pode adicionar métodos customizados se precisar, como:
    // List<Tarefa> findByStatus(String status);
}

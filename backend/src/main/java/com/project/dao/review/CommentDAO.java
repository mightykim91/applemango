package com.project.dao.review;

import org.springframework.data.jpa.repository.JpaRepository;

import com.project.model.CommentEntity;

public interface CommentDAO extends JpaRepository<CommentEntity, Long>{
 
}
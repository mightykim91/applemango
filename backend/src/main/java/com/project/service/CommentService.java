package com.project.service;

import com.project.dao.review.CommentDAO;
import com.project.model.CommentEntity;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

@Service
public class CommentService {

    @Autowired //DI
    CommentDAO dao;

    public Object getAllComments(){
        List<CommentEntity> comments = dao.findAll();
        return new ResponseEntity<List<CommentEntity>>(comments, HttpStatus.OK);
    }

    public Object createComment(CommentEntity request){
        CommentEntity comment = new CommentEntity();
        comment.setReviewId(request.getReviewId());
        comment.setUserId(request.getUserId());
        comment.setContent(request.getContent());
        comment.setCreatedDate(LocalDateTime.now());
        comment.setModifiedDate(LocalDateTime.now());
        dao.save(comment);
        return new ResponseEntity<CommentEntity>(comment, HttpStatus.OK);
    }

    public Object deleteComment(long commentId){
        dao.deleteById(commentId);
        return new ResponseEntity<String>(HttpStatus.OK);
    }

    public Object modifyComment(CommentEntity request){
        Optional<CommentEntity> comment = dao.findById(request.getId());
        comment.ifPresent(c -> {
            c.setContent(request.getContent());
            c.setModifiedDate(LocalDateTime.now());
            dao.save(c);
        });
        return new ResponseEntity<Optional<CommentEntity>>(comment, HttpStatus.OK);

    }
    
}
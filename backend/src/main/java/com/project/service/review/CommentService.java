package com.project.service.review;

import com.project.dao.review.CommentDAO;
import com.project.dao.review.ReviewDAO;
import com.project.model.review.*;

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

    @Autowired
    ReviewDAO reviewdao;

    public Object getAllComments(){
        List<CommentEntity> comments = dao.findAll();
        return new ResponseEntity<List<CommentEntity>>(comments, HttpStatus.OK);
    }

    public Object createComment(CommentCreationRequest request){
        //Get review Object
        ReviewEntity review = reviewdao.findReviewById(request.getReviewId());
        System.out.println(request.getReviewId());
        CommentEntity comment = new CommentEntity(review, request.getUserId(), request.getContent());
        comment.setCreatedDate(LocalDateTime.now());
        comment.setModifiedDate(LocalDateTime.now());
        dao.save(comment);
        
        // CommentEntity comment = new CommentEntity();
        // comment.setReview(request.getReview());
        // comment.setUserId(request.getUserId());
        // comment.setContent(request.getContent());
        // comment.setCreatedDate(LocalDateTime.now());
        // comment.setModifiedDate(LocalDateTime.now());
        // CommentEntity comment = new CommentEntity(
        //     request.getReview(), request.getUserId(),request.getContent()
        // );
        // dao.save(comment);
        return new ResponseEntity<CommentEntity>(comment, HttpStatus.OK);
    }

    public Object deleteComment(long commentId){
        dao.deleteById(commentId);
        return new ResponseEntity<List<CommentEntity>>(dao.findAll(),HttpStatus.OK);
    }

    public Object modifyComment(CommentEntity request){
        Optional<CommentEntity> comment = dao.findById(request.getId());
        comment.ifPresent(c -> {
            c.setContent(request.getContent());
            c.setModifiedDate(LocalDateTime.now());
            dao.save(c);
        });
        return new ResponseEntity<List<CommentEntity>>(dao.findAll(), HttpStatus.OK);

    }
    
}
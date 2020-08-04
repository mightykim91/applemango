package com.project.controller.review;

import com.project.model.review.CommentEntity;
import com.project.service.review.*;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@CrossOrigin
@RestController
@RequestMapping(value = "/comment")
public class CommentController {

    @Autowired
    CommentService service;
    
    @GetMapping("/all")
    public Object getAllComments(){
        return service.getAllComments();
    }

    @PostMapping("/new")
    public Object createComment(@RequestBody CommentEntity request){
        return service.createComment(request);
    }

    @DeleteMapping("/delete")
    public Object deleteComment(@RequestParam long commentId){
        return service.deleteComment(commentId);
    }

    @PutMapping("/modify")
    public Object modifyComment(@RequestBody CommentEntity commentEntity){
        return service.modifyComment(commentEntity);
    }

}
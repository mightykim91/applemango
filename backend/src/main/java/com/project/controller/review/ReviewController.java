package com.project.controller.review;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

import javax.servlet.http.HttpServletRequest;

import com.project.dao.user.UserDAO;

import com.project.model.review.*;
import com.project.service.review.*;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@CrossOrigin
@RestController
@RequestMapping("/review")
public class ReviewController {

    @Autowired
    ReviewService reviewservice;

    // @GetMapping(value="/userinfo")
    // public Object getUserInfo(HttpServletRequest request){
    //     return request.getHeader("auth-token");
    // }

    @GetMapping(value = "")
    public Object getAllReview(){
        List<ReviewEntity> allReview = reviewservice.findAll();
        return new ResponseEntity<List<ReviewEntity>>(allReview, HttpStatus.OK);
        
    }

    @PostMapping(value = "/new")
    public Object createPost(@RequestBody ReviewEntity newReview){
        ReviewEntity review = new ReviewEntity(
            newReview.getUserId(),
            newReview.getTitle(),
            newReview.getDescription(),
            newReview.getStar()
        );
        review.setRestaurantId(newReview.getRestaurantId());

        if (reviewservice.save(review) == review){
            return new ResponseEntity<Object>(HttpStatus.OK);
        };

        return new ResponseEntity<Object>(HttpStatus.BAD_REQUEST);
    }

    //Read Single Review
    @GetMapping(value = "/{reviewId}")
    public Object getReview(@PathVariable long reviewId){
        Optional<ReviewEntity> review = reviewservice.getReview(reviewId);
        if (review.isPresent()){
            return new ResponseEntity<Optional<ReviewEntity>>(review, HttpStatus.OK);
        }
        return new ResponseEntity<String>(HttpStatus.NOT_FOUND);
    }

    //Read reviews by id 
    @GetMapping(value = "/reviews/{userId}")
    public Object getReviewByUserId(@PathVariable String userId){
        List<ReviewEntity> reviews = reviewservice.getReviewByUserId(userId);
        return new ResponseEntity<List<ReviewEntity>>(reviews, HttpStatus.OK);
    }

    @PutMapping(value = "/update/{reviewId}")
    public Object modifyReview(@PathVariable long reviewId, @RequestBody ReviewUpdateRequest request){
        return reviewservice.updateReview(reviewId, request);
    }

    //글 삭제(Request Parameter로 리뷰id 받아와야함)
    @DeleteMapping(value = "/delete")
    public Object deleteReview(@RequestParam long reviewId){
        
        return reviewservice.deleteReview(reviewId);
    }

    
}
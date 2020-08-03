package com.project.service;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

import com.project.model.Review;
import com.project.dao.review.ReviewDao;
import com.project.model.ReviewUpdateRequest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

@Service
public class ReviewService {
    
    @Autowired
    ReviewDao reviewDao;

    public List<Review> findAll(){
        return reviewDao.findAll();
    }

    public Object save(Review newReview){
        return reviewDao.save(newReview); 
    }

    //Optional returns object and null object
    public Optional<Review> getReview(long reviewId){
        return reviewDao.findById(reviewId);
    }

    public List<Review> getReviewByUserId(String userId){
        return reviewDao.findByUserId(userId);
    }

    public Object updateReview(long reviewId, ReviewUpdateRequest request){
        Optional<Review> review = reviewDao.findById(reviewId);
        review.ifPresent(r -> {
            r.setTitle(request.getTitle());
            r.setDescription(request.getDescription());
            r.setStar(request.getStar());
            r.setModifiedDate(LocalDateTime.now());
            reviewDao.save(r);
        });

        return new ResponseEntity<Optional<Review>>(review, HttpStatus.OK);
    }

    public Object deleteReview(long reviewId){
        reviewDao.findById(reviewId).ifPresent(r -> {
            reviewDao.delete(r);
        });
        return new ResponseEntity<String>(HttpStatus.OK);
    }
    
}
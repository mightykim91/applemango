package com.project.service.review;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

import com.project.model.review.*;
import com.project.service.user.FavorService;
import com.project.dao.review.ReviewDAO;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

@Service
public class ReviewService {
    
    @Autowired
    ReviewDAO reviewDao;
    
    @Autowired
    FavorService favorService;

    public List<ReviewEntity> findAll(){
        return reviewDao.findAll();
    }

    public Object save(ReviewEntity newReview){
        
        favorService.save(newReview);

        return reviewDao.save(newReview); 
    }

    //Optional returns object and null object
    public Optional<ReviewEntity> getReview(long reviewId){
        return reviewDao.findById(reviewId);
    }

    public List<ReviewEntity> getReviewByUserId(String userId){
        return reviewDao.findByUserId(userId);
    }

    public Object updateReview(long reviewId, ReviewUpdateRequest request){
        Optional<ReviewEntity> review = reviewDao.findById(reviewId);
        review.ifPresent(r -> {
            r.setTitle(request.getTitle());
            r.setDescription(request.getDescription());
            r.setStar(request.getStar());
            r.setModifiedDate(LocalDateTime.now());
            reviewDao.save(r);
        });

        return new ResponseEntity<Optional<ReviewEntity>>(review, HttpStatus.OK);
    }

    public Object deleteReview(long reviewId){
        reviewDao.findById(reviewId).ifPresent(r -> {
            reviewDao.delete(r);
        });
        return new ResponseEntity<List<ReviewEntity>>(reviewDao.findAll() ,HttpStatus.OK);
    }
    
}
package com.project.dao.review;

import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

import com.project.model.Review;


public interface ReviewDao extends JpaRepository<Review, Long>{
    //Get all Reviews
    public List<Review> findAll();

    //Get all reviews of written by certain user
    public List<Review> findByUserId(String userId);


}
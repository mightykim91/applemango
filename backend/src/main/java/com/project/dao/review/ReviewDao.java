package com.project.dao.review;

import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

import com.project.model.review.ReviewEntity;


public interface ReviewDAO extends JpaRepository<ReviewEntity, Long>{
    //Get all Reviews
    public List<ReviewEntity> findAll();

    //Get all reviews of written by certain user
    public List<ReviewEntity> findByUserId(String userId);


}
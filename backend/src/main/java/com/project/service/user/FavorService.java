package com.project.service.user;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

import com.project.model.Review;
import com.project.dao.restaurant.RestaurantDAO;
import com.project.dao.review.ReviewDao;
import com.project.dao.user.FavorDAO;
import com.project.model.ReviewUpdateRequest;
import com.project.model.restaurant.Restaurant;
import com.project.model.user.FavorEntity;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

@Service
public class FavorService {
    
    @Autowired
    FavorDAO favorDao;

    @Autowired
    RestaurantDAO restaurantDao;

    public List<FavorEntity> findAll(){
        return favorDao.findAll();
    }

    public Object save(FavorEntity newReview){
        return favorDao.save(newReview); 
    }



    public List<FavorEntity> getFavorlistByUid(String uid){
        return favorDao.findAllByUid(uid);
    }

    public List<FavorEntity> getFavorsByUid(String uid){
        return favorDao.findAllByUid(uid);
    }

   
    
}
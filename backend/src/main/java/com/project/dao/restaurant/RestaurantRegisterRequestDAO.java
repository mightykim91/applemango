package com.project.dao.restaurant;

import com.project.model.restaurant.RestaurantRegisterRequest;

import org.springframework.data.jpa.repository.JpaRepository;

public interface RestaurantRegisterRequestDAO extends JpaRepository<RestaurantRegisterRequest,String>{
    
}
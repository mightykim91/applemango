package com.project.controller.restaurant;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.project.dao.restaurant.RestaurantRegisterRequestDAO;
import com.project.dao.user.UserDAO;
import com.project.model.restaurant.RestaurantEntity;
import com.project.model.restaurant.RestaurantRegisterRequest;
import com.project.model.restaurant.RestaurantRegistrationForm;
import com.project.model.user.UserEntity;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@CrossOrigin
@RestController
@RequestMapping("/register")
public class RegisterRequestController {

    @Autowired
    RestaurantRegisterRequestDAO dao;

    @Autowired
    UserDAO userdao;

    ObjectMapper mapper = new ObjectMapper();

    //사업자가 보내는 요청 처리
    @PostMapping(value = "/restaurant")
    public Object sendRestaurantRegisterRequest(@RequestBody RestaurantRegistrationForm request) throws
    JsonProcessingException{

        UserEntity user = userdao.getUserByUid(request.getUserName());
        String restaurantInfo = mapper.writeValueAsString(request.getRestaurantInfo());
        RestaurantRegisterRequest registerRequest = new RestaurantRegisterRequest();
        registerRequest.setUser(user);
        registerRequest.setRestaurantInfo(restaurantInfo);
        dao.save(registerRequest);
        
        return registerRequest;
    }
    
}
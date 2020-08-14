package com.project.controller.restaurant;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.project.dao.restaurant.RestaurantDAO;
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
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import io.swagger.models.Response;

@RestController
@RequestMapping("/register")
public class RegisterRequestController {

    @Autowired
    RestaurantRegisterRequestDAO dao;

    @Autowired
    UserDAO userdao;

    @Autowired
    RestaurantDAO rstDao;

    ObjectMapper mapper = new ObjectMapper();

    // 사업자가 보내는 요청 처리    
    @PostMapping(value = "/restaurant")
    public ResponseEntity sendRestaurantRegisterRequest(@RequestBody RestaurantRegistrationForm request)
            throws JsonProcessingException {

        UserEntity user = userdao.getUserByUid(request.getUserName());
        String restaurantInfo = mapper.writeValueAsString(request.getRestaurantInfo());
        RestaurantRegisterRequest registerRequest = new RestaurantRegisterRequest();
        registerRequest.setUser(user);
        registerRequest.setRestaurantInfo(restaurantInfo);
        dao.save(registerRequest);

        return new ResponseEntity<>("success", HttpStatus.OK);
    }

    // 모든 요청 출력
    @GetMapping(value = "/all")
    public ResponseEntity getAllRequests() throws JsonMappingException, JsonProcessingException {
        List<RestaurantRegisterRequest> allRequests = dao.findAll();
        ArrayList<HashMap<String,Object>> response = new ArrayList<>();
        for (RestaurantRegisterRequest request : allRequests){
            System.out.println(mapper.readValue(request.getRestaurantInfo(),RestaurantEntity.class));
            HashMap<String,Object> tempResponse = new HashMap<>();
            tempResponse.put("requestId", request.getId());
            tempResponse.put("userName", request.getUser());
            tempResponse.put("restaurantInfo", mapper.readValue(request.getRestaurantInfo(),RestaurantEntity.class));
            response.add(tempResponse);
            System.out.println(tempResponse);
        }
        System.out.println(response);
        return new ResponseEntity<ArrayList<HashMap<String,Object>>>(response, HttpStatus.OK);
    }

    //요청 수락하기 위한 관리자 페이지
    @PostMapping(value="/accept")
    public ResponseEntity acceptRequest(@RequestParam long requestId) throws JsonMappingException, JsonProcessingException {
        RestaurantRegisterRequest request = dao.findRestaurantRegisterRequestById(requestId);
        RestaurantEntity requestedRestaurant = mapper.readValue(request.getRestaurantInfo(),RestaurantEntity.class);
        //소라 수정 --> username에서 uid로 수정
        String username = request.getUser().getUid();
        System.out.println("requestrst/accept userid"+ username);
        
        requestedRestaurant.setRuid(username);
        dao.delete(request);
        rstDao.save(requestedRestaurant);
        
        return new ResponseEntity<RestaurantEntity>(requestedRestaurant, HttpStatus.OK);
    }
    
}
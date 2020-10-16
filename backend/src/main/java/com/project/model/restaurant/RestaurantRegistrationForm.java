package com.project.model.restaurant;

import javax.validation.constraints.NotNull;

import lombok.Getter;

@Getter
public class RestaurantRegistrationForm {

    @NotNull
    private RestaurantEntity restaurantInfo;

    @NotNull
    //find with token and session later
    private String userName;
    
}
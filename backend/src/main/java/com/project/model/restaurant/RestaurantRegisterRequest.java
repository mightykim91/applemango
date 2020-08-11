package com.project.model.restaurant;

import com.project.model.user.UserEntity;

import org.json.JSONObject;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@Entity
@Table(name="RestaurantRegisterRequests")
public class RestaurantRegisterRequest {
    
    @Id
    @GeneratedValue(strategy=GenerationType.IDENTITY)
    private long id;

    @ManyToOne(targetEntity=UserEntity.class, fetch=FetchType.EAGER)
    @JoinColumn(name="user_id") //EAGER=즉시로딩, LAZY=지연로딩
    private UserEntity user;

    @Column(name="restaurant_info")
    private String restaurantInfo;

    
}
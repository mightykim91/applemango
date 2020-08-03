package com.project.model;

import java.time.LocalDateTime;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

import org.springframework.data.annotation.CreatedDate;
import org.springframework.data.annotation.LastModifiedDate;

import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;

@Entity
@Table(name = "reviewinfo")
public class Review {

    @Id
    @Column(name = "reid")
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;

    @Column(name="reuid")
    // @ManyToOne //Need to set Entity
    private String userId;

    @Column(name="rerid")
    private long restaurantId;

    @Column(name = "retitle")
    private String title;

    @Column(name = "redescription")
    private String description;

    @Column(name = "rerating")
    private int star;

    @CreatedDate
    @Column(name = "recreateddate")
    private LocalDateTime createdDate;

    @LastModifiedDate
    @Column(name = "remodifieddate")
    private LocalDateTime modifiedDate;

    //Default Constructor
    public Review(){};
    
    //Basic Constructor including username, review title, content, star
    public Review(String userId, String title, String description, int star){
        this.userId = userId;
        this.title = title;
        this.description = description;
        this.star = star;
        this.createdDate = LocalDateTime.now();
        this.modifiedDate = LocalDateTime.now();
    }

    //GETTER
    public long getReviewId(){
        return id;
    }

    public String getUserId(){
        return userId;
    }

    public long getRestaurantId(){
        return restaurantId;
    }

    public String getTitle(){
        return title;
    }

    public int getStar(){
        return star;
    }

    public String getDescription(){
        return description;
    }

    public LocalDateTime getCreatedDate(){
        return createdDate;
    }

    public LocalDateTime getModifiedDate(){
        return modifiedDate;
    }

    //SETTER

    //파라미터는 나중에 다른 엔티티에 맞춰서 바꾸기
    public void setUserId(String userId){
        this.userId = userId;
    }

    public void setTitle(String title){
        this.title = title;
    }

    public void setDescription(String description){
        this.description = description;
    }

    public void setStar(int star){
        this.star = star;
    }

    public void setModifiedDate(LocalDateTime modificationDateTime){
        this.modifiedDate = modificationDateTime;
    }

    public void setRestaurantId(long restaurantId){
        this.restaurantId = restaurantId;
    }

    


    
}
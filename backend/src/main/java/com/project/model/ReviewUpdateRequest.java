package com.project.model;

import javax.validation.constraints.NotNull;

public class ReviewUpdateRequest {
    
    @NotNull
    private String title;

    @NotNull
    private String description;
    
    @NotNull
    private int star;

    //getter, setter
    public String getTitle(){
        return this.title;
    }

    public String getDescription(){
        return this.description;
    }

    public int getStar(){
        return this.star;
    }
}
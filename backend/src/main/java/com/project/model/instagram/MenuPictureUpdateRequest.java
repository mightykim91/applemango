package com.project.model.instagram;

import javax.validation.constraints.NotNull;

public class MenuPictureUpdateRequest {
    
    @NotNull
    private int mid;

    @NotNull
    private String mimage;
 
    
    
    public int getMid(){
        return this.mid;
    }

    public String getMimage(){
        return this.mimage;
    }

}
package com.project.model.review;

import javax.validation.constraints.NotNull;

public class CommentCreationRequest {

    @NotNull
    private long reviewId;

    @NotNull
    private String content;

    @NotNull
    private String userId;

    //getter
    public long getReviewId(){
        return this.reviewId;
    }

    public String getUserId(){
        return this.userId;
    }

    public String getContent(){
        return this.content;
    }
    
}
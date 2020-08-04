package com.project.model.user;

import java.time.LocalDateTime;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

import org.springframework.data.annotation.CreatedDate;
import org.springframework.data.annotation.LastModifiedDate;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@Entity
@Table(name="userfavor")
public class FavorEntity {
    

    @Id 
    @Column(name = "uid")
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private String uid;

    @Column(name = "rid")
    private int rid;

    public FavorEntity(){};

    public FavorEntity(String uid, int rid){
        this.uid = uid;
        this.rid = rid;
    }

    public String getUid(){
        return this.uid;
    }
    public int getRid(){
        return this.rid;
    }

}
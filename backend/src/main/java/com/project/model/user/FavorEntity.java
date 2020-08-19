package com.project.model.user;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.JoinTable;
import javax.persistence.MapsId;
import javax.persistence.OneToOne;
import javax.persistence.Table;

import com.project.model.restaurant.RestaurantEntity;

import lombok.*;

@Getter
@Setter
@ToString
//@NoArgsConstructor
@Entity
@Table(name = "userfavor")
public class FavorEntity {
    
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "fid")
    private int fid;
 
    @Column(name = "uid")
    private String uid;

    @Column(name = "frid")
    private long frid;

    // @OneToOne
    // @JoinTable(name = "ffff", //조인테이블명
    //            joinColumns = @JoinColumn(name = "rid"), // 외래키
    //            inverseJoinColumns = @JoinColumn(name="frid") //반대 엔티티의 외래키
    //            )
    // private Restaurant restaurant;

    @OneToOne
    @JoinColumn(name = "frid",
    insertable = false, updatable = false)
    private RestaurantEntity restaurant;

}
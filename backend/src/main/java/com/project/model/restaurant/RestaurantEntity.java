package com.project.model.restaurant;
import lombok.*;

import javax.persistence.*;

import java.sql.Date;

//@ToString
//@NoArgsConstructor
@Getter @Setter
//@Builder
@Entity
@Table(name = "restaurantinfo")

public class RestaurantEntity {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int rid; // 식당 id
    private String rname; //식당 이름
    private String rbranch; //식당 지점
    private String ruid; //식당 주인 id
    private String rphone; //식당 번호
    private String raddr; //식당 주소
    private String rimage; //식당 로고 이미지
    private String rdescription; //식당 정보
    private Date rcreatedate; //식당 정보 등록

    public RestaurantEntity(){};
    

    public RestaurantEntity(String rname, String rbranch, String ruid, String rphone, String raddr) {
        this.rname = rname;
        this.rbranch = rbranch;
        this.ruid = ruid;
        this.rphone = rphone;
        this.raddr = raddr;
    }

    public RestaurantEntity(String rname, String rbranch, String ruid, String rphone, String raddr, String rimage, String rdescription, Date rcreatedate){
        this.rname = rname;
        this.rbranch = rbranch;
        this.ruid = ruid;
        this.rphone = rphone;
        this.raddr = raddr;
        this.rimage = rimage;
        this.rdescription = rdescription;
        this.rcreatedate = rcreatedate;
    }

    public String toString(){
        return "data check: " + 
               " rname =" + this.rname +
               " rbranch ="+this.rbranch+
               " ruid =" + this.ruid +
               " rphone =" + this.rphone +
               " raddr =" + this.raddr;
    }
    
}
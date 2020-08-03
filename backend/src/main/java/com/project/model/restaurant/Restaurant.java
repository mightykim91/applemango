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

public class Restaurant {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int rid; // 식당 id
    private String rname; //식당 이름
    private String rbranch; //식당 지점
    private String ruid; //식당 주인 id
    private String rphone; //식당 번호
    private String raddr; //식당 주소
    private String rlat; //식당 위도,경도
    private String rlng;
    private String rdescription; //식당 정보
    private Date rcreatedate; //식당 정보 등록

    public Restaurant(){};
    

    public Restaurant(String rname, String rbranch, String ruid, String rphone, String raddr) {
        this.rname = rname;
        this.rbranch = rbranch;
        this.ruid = ruid;
        this.rphone = rphone;
        this.raddr = raddr;
    }


    public Restaurant(String rname, String rbranch, String ruid, String rphone, String raddr, String rlat, String rlng, String rdescription, Date rcreatedate){
        this.rname = rname;
        this.rbranch = rbranch;
        this.ruid = ruid;
        this.rphone = rphone;
        this.raddr = raddr;
        this.rlat = rlat;
        this.rlng = rlng;
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
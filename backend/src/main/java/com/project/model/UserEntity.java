package com.project.model;

import lombok.*;

import javax.persistence.*;

import java.sql.Date;
import java.time.LocalDateTime;
import java.time.ZoneId;

@Getter
@Setter
@ToString
@Builder
//@NoArgsConstructor
@Entity
@Table(name = "userinfo")
public class UserEntity {

    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private String uid;
    private String upw;
    private int ukind;
    private String uname;
    private String uemail;
    private String uphone;
    private String uaddr;
    private String uaddrsido;
    private String uaddrgu;
    private String uaddrdong;
    private String uaddrdetail;
    private String uinstagramid;
    private Date ucreatedate;

    public UserEntity(){};
    
    public UserEntity(String uid, String upw,int ukind,String uname,String uemail,String uphone,String uaddr,String uaddrsido,String uaddrgu,String uaddrdong,String uaddrdetail, String uinstagramid, Date ucreatedate){
      
        this.uid = uid;
        this.upw = upw;
        this.ukind = ukind;
        this.uname = uname;
        this.uemail = uemail;
        this.uphone = uphone;
        this.uaddr = uaddr;
        this.uaddrsido = uaddrsido;
        this.uaddrgu = uaddrgu;
        this.uaddrdong = uaddrdong;
        this.uaddrdetail = uaddrdetail;
        this.uinstagramid = uinstagramid;
        this.ucreatedate = ucreatedate;
    }

    public String getUid(){
        return uid;
    }

    public String getUpw(){
        return upw;
    }

    public String getUemail(){
        return uemail;
    }
    
}

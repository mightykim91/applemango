package com.project.model.user;

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

    @Id 
    private String uid;
    private String upw;
    private int ukind;
    private String uname;
    private String uemail;
    private String uphone;
    private String uaddr;
    private String uinstagramid;
    private LocalDateTime ucreatedate;

    public UserEntity(){};
    
    public UserEntity(String uid, String upw,int ukind,String uname,String uemail,String uphone,String uaddr,String uinstagramid, LocalDateTime ucreatedate){
      
        this.uid = uid;
        this.upw = upw;
        this.ukind = ukind;
        this.uname = uname;
        this.uemail = uemail;
        this.uphone = uphone;
        this.uaddr = uaddr;
        this.uinstagramid = uinstagramid;
        this.ucreatedate = ucreatedate;
    }
    
}

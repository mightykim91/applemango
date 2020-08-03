package com.project.model.instagram;

import java.time.LocalDateTime;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

import net.bytebuddy.asm.Advice.Local;

import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;

@Entity
@Table(name = "instagrampictures")
public class InstaEntity {

    @Id
    @Column(name = "iid")
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int iid;

    @Column(name="irid")
    private int irid; // 연결 사업장 ID

    @Column(name = "rname")
    private String rname;

    @Column(name = "rbranch")
    private String rbranch;

    @Column(name = "instaid")
    private String instaid;

    @Column(name = "iurl")
    private String iurl;

    @Column(name = "likes")
    private int likes;

    @Column(name = "idate")
    private LocalDateTime idate;

    //Default Constructor
    public InstaEntity(){};
    
    //Basic Constructor including username, review title, content, star
    public InstaEntity(int iid,int irid, String rname, String rbranch, String instaid, String iurl, int likes,LocalDateTime idate){
        this.iid = iid;
        this.irid = irid; // 연결 사업장 ID
        this.rname = rname;
        this.rbranch = rbranch;
        this.instaid = instaid;
        this.iurl = iurl;
        this.likes = likes;
        this.idate = idate;
    }

    public int getIid(){
        return this.iid;
    }

    public int getIrid(){
        return this.irid;
    }
    public String getRname(){
        return this.rname;
    }

    public String getRbranch(){
        return this.rbranch;
    }


    public String getInstaid(){
        return this.instaid;
    }

    public String getIurl(){
        return this.iurl;
    }

    public int getLikes(){
        return this.likes;
    }

    public LocalDateTime getIdate(){
        return this.idate;
    }


    public void setIdate(LocalDateTime idate){
        this.idate = idate;
    }

    


    
}
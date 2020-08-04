package com.project.model.review;

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
@NoArgsConstructor
@Table(name="commentinfo")
public class CommentEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "cmid")
    private long id; //댓글 아이디

    @Column(name = "cmreid") //해당 리뷰 아이디(FK설정)
    private long reviewId;

    @Column(name="cmuid")
    private String userId; //작성자 아이디
    
    @Column(name="cmcontent") //댓글 내용
    private String content;

    @CreatedDate
    @Column(name = "cmcreateddate") //댓글 최초 작성일
    private LocalDateTime createdDate;

    @LastModifiedDate
    @Column(name = "cmmodifieddate") //댓글 수정일
    private LocalDateTime modifiedDate;
}
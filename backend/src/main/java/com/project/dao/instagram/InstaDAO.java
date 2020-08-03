package com.project.dao.instagram;

import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

import com.project.model.instagram.InstaEntity;

public interface InstaDAO extends JpaRepository<InstaEntity, Long>{
     //Get all Instagram Crawled pictures
     public List<InstaEntity> findAll();

     //Get allInstagram Crawled pictures of restaurant
     public List<InstaEntity> findByIrid(int irid);
 
 
}
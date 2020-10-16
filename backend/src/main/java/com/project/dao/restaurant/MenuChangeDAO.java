package com.project.dao.restaurant;

import com.project.model.restaurant.MenuEntity;

import java.util.List;
import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;

public interface MenuChangeDAO extends JpaRepository<MenuEntity, String> {
        //Get all Menu
        public List<MenuEntity> findAll();

        //Get all Menu of Restaurant
        public List<MenuEntity> findByMrid(int mrid);

        public Optional<MenuEntity> findByMid(int mid);
    
}
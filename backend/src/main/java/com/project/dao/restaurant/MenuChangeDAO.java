package com.project.dao.restaurant;

import com.project.model.restaurant.Menu;

import java.util.List;
import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;

public interface MenuChangeDAO extends JpaRepository<Menu, String> {
        //Get all Menu
        public List<Menu> findAll();

        //Get all Menu of Restaurant
        public List<Menu> findByMrid(int mrid);

        public Optional<Menu> findByMid(int mid);
    
}
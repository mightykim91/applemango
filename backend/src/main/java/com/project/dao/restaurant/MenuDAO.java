package com.project.dao.restaurant;

import java.util.List;
import java.util.Optional;

import com.project.model.restaurant.MenuEntity;

import org.springframework.data.jpa.repository.JpaRepository;

public interface MenuDAO extends JpaRepository<MenuEntity, String> {
    //public List<Menu> findAll();

    public List<MenuEntity> findAllByMrid(int mrid);
    public Optional<MenuEntity> findByMid(int mid);
 
}
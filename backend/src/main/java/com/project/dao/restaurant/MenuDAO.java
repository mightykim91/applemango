package com.project.dao.restaurant;

import java.util.List;

import com.project.model.restaurant.MenuEntity;

import org.springframework.data.jpa.repository.JpaRepository;

public interface MenuDAO extends JpaRepository<MenuEntity, String> {
    //public List<Menu> findAll();

    public List<MenuEntity> findAllByMrid(int mrid);

    public Object findByMname(String mname);
    public MenuEntity findByMid(int mid);


    
}
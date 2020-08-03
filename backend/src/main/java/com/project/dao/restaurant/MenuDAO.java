package com.project.dao.restaurant;

import java.util.List;

import com.project.model.restaurant.Menu;

import org.springframework.data.jpa.repository.JpaRepository;

public interface MenuDAO extends JpaRepository<Menu, String> {
    //public List<Menu> findAll();

    public List<Menu> findAllByMrid(int mrid);

    public Object findByMname(String mname);
    public Menu findByMid(int mid);


    
}
package com.project.dao.restaurant;
import java.util.List;
import java.util.Optional;

import com.project.model.restaurant.RestaurantEntity;

import org.springframework.data.jpa.repository.JpaRepository;
public interface RestaurantDAO extends JpaRepository<RestaurantEntity, String> {
    public List<RestaurantEntity> findAll();
    public Optional<RestaurantEntity> findByRid(int rid);
    public List<RestaurantEntity> findAllByRuid(String ruid);
}//end of interface
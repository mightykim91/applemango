package com.project.dao.restaurant;
import java.util.List;
import java.util.Optional;

import com.project.model.restaurant.Restaurant;

import org.springframework.data.jpa.repository.JpaRepository;
public interface RestaurantDAO extends JpaRepository<Restaurant, String> {
    public List<Restaurant> findAll();
    public Optional<Restaurant> findByRid(int rid);
    public List<Restaurant> findAllByRuid(String ruid);
}//end of interface
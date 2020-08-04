package com.project.dao.user;

import com.project.model.restaurant.Restaurant;
import com.project.model.user.FavorEntity;

import java.util.List;
import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;

public interface FavorDAO extends JpaRepository<FavorEntity,String>{
    
    public List<FavorEntity> findAllByUid(String uid);

    public FavorEntity findByRid(String rid);
    public FavorEntity findByUid(String uid);
}
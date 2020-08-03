package com.project.dao.user;

import com.project.model.user.FavorEntity;

import java.util.List;
import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;

public interface FavorDAO extends JpaRepository<FavorEntity,String>{
    
    
    FavorEntity getFavorByUid(String uid);
    FavorEntity getFavorByRid(int rid);

    public List<FavorEntity> findByUid(String uid);
    //Optional<FavorEntity> findByUid(String uid);
}
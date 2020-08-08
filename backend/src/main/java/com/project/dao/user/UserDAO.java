package com.project.dao.user;

import com.project.model.user.UserEntity;
import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;

public interface UserDAO extends JpaRepository<UserEntity,String>{
    

    UserEntity getUserByUemail(String uemail);
    UserEntity getUserByUid(String uid);


    Optional<UserEntity> findByUid(String uid);
    
    Optional<UserEntity> findByUidAndUpw(String uid,String upw);
}
package com.project.service.restaurant;

import java.util.List;
import java.util.Optional;

import com.project.dao.restaurant.RestaurantDAO;
import com.project.model.restaurant.*;

import org.springframework.stereotype.Service;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

@Service
public class RestaurantService {
    @Autowired
    RestaurantDAO rstDao;

    public List<Restaurant> findAll(){
        return rstDao.findAll();
    }

    public Optional<Restaurant> getRestaurantInfo(int rid){
        return rstDao.findByRid(rid);
    }

    public Object rstSave(Restaurant request) {
        return rstDao.save(request);
    }

    public List<Restaurant> getRestaurantList(String ruid) {
        return rstDao.findAllByRuid(ruid);
    }

    public Object Modrst(Restaurant request) {
        int rid = request.getRid();
        Optional<Restaurant> tmp = rstDao.findByRid(rid);
        tmp.ifPresent(rst -> {
            rst.setRname(request.getRname());
            rst.setRbranch(request.getRbranch());
            rst.setRphone(request.getRphone());
            rst.setRaddr(request.getRaddr());
        });

        return new ResponseEntity<Optional<Restaurant>>(tmp, HttpStatus.OK);
    }

    public Object Delrst(int rid) {
        rstDao.findByRid(rid).ifPresent(rst -> {
            rstDao.delete(rst);
        });
        return new ResponseEntity<String>(HttpStatus.OK);
    }
}
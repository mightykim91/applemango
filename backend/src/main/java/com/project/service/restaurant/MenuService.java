package com.project.service.restaurant;

import java.util.List;

import com.project.dao.restaurant.MenuDAO;
import com.project.model.restaurant.Menu;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

@Service
public class MenuService {
    @Autowired
    MenuDAO mDao;
    
    //save
    public Object regMenu(Menu newMenu){
        return mDao.save(newMenu);
    }

    //식당에 딸린 메뉴 전체 조회
    public List<Menu> listMenu(int mrid) {
        return mDao.findAllByMrid(mrid);
    }


    //메뉴 상세정보 조회
    public Object detailMenu(String mName){
        return mDao.findByMname(mName);
    }

    //modify
    public Object modMenu(int mid) {
        return null;
    }

    //delete
    public Object delMenu(int mid) {
        //mDao.findByMid(mid).ifPresent(m -> {mDao.delete(m);});
        return new ResponseEntity<>(HttpStatus.OK);
    }
}
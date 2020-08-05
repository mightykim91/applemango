package com.project.service.restaurant;

import java.util.List;
import java.util.Optional;

import com.project.dao.restaurant.MenuDAO;
import com.project.model.restaurant.MenuEntity;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

@Service
public class MenuService {
    @Autowired
    MenuDAO mDao;
    
    //save
    public Object regMenu(MenuEntity newMenu){
        return mDao.save(newMenu);
    }

    //식당에 딸린 메뉴 전체 조회
    public List<MenuEntity> listMenu(int mrid) {
        System.out.println("menu list service: "+ mrid);
        return mDao.findAllByMrid(mrid);
    }

    //modify
    public Object modMenu(MenuEntity modmenu) {
        System.out.println("modMenu Service modmenu check name:"+ modmenu.getMname()+" getmenu id:"+ modmenu.getMid());
        Optional<MenuEntity> menu = mDao.findByMid(modmenu.getMid());
        menu.ifPresent(m -> {
            m.setMname(modmenu.getMname());
            m.setMissig(modmenu.getmissig());
            m.setMprice(modmenu.getMprice());
            m.setMimage(modmenu.getMimage());
            mDao.save(m);
        });
        return new ResponseEntity<Optional<MenuEntity>>(menu, HttpStatus.OK);
    }

    //delete
    public Object delMenu(int mid) {
        //mDao.findByMid(mid).ifPresent(m -> {mDao.delete(m);});
        mDao.findByMid(mid).ifPresent(m -> {
            mDao.delete(m);
        });
        return new ResponseEntity<String>(HttpStatus.OK);
    }


}
package com.project.service.instagram;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

import com.project.model.instagram.InstaEntity;
import com.project.model.instagram.MenuPictureUpdateRequest;
import com.project.dao.instagram.InstaDAO;
import com.project.dao.restaurant.MenuChangeDAO;
import com.project.model.restaurant.MenuEntity;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

@Service
public class InstaService {
    
    @Autowired
    InstaDAO  instaDao;

    @Autowired
    MenuChangeDAO MenuDao;
    
    public List<InstaEntity> findAll(){
        return instaDao.findAll();
    }

    
    public List<InstaEntity> getInstaEntityByIrid(int irid){
        return instaDao.findByIrid(irid);
    }


	public Object updateInstaPicture(MenuPictureUpdateRequest request) {
        System.out.println("mid : " + request.getMid());
        
        Optional<MenuEntity> menuEntity = MenuDao.findByMid(request.getMid());
        
        menuEntity.ifPresent(r -> {
            System.out.println(r);
            r.setMimage(request.getMimage());
            MenuDao.save(r);
        });
        
        System.out.println("Service input test - code 13131322");
        
        return new ResponseEntity<Optional<MenuEntity>>(menuEntity, HttpStatus.OK);
        
	}
}
package com.project.controller.instagram;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

import com.project.dao.UserDAO;
import com.project.model.Review;
import com.project.service.ReviewService;
import com.project.service.instagram.InstaService;
import com.project.model.ReviewUpdateRequest;
import com.project.model.instagram.InstaEntity;
import com.project.model.instagram.MenuPictureUpdateRequest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@CrossOrigin
@Validated
@RestController
@RequestMapping("/instagram")
public class InstaController {
    
    @Autowired
    InstaService instaService;

    @GetMapping(value = "/all")
    public Object getAllReview(){
        List<InstaEntity> allInstaEntities = instaService.findAll();
        //System.out.println(allInstaEntities.get(0).getIid());
        return new ResponseEntity<List<InstaEntity>>(allInstaEntities, HttpStatus.OK);
    }

    @GetMapping(value = "/select/{irid}")
    public Object getReviewByIrid(@PathVariable int irid){
        List<InstaEntity> instaEntities = instaService.getInstaEntityByIrid(irid);
        return new ResponseEntity<List<InstaEntity>>(instaEntities, HttpStatus.OK);
     }

    @PostMapping(value = "/update")
    public Object updateMenuPicture(@RequestBody MenuPictureUpdateRequest request){
         return instaService.updateInstaPicture(request);
    }

     
}
package com.project.controller.restaurant;

import java.util.List;
import java.util.Optional;

import com.project.model.restaurant.*;
import com.project.service.restaurant.*;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.CrossOrigin;
// import org.springframework.web.bind.annotation.GetMapping;
// import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
// import org.springframework.web.bind.annotation.RequestMapping;
// import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
@CrossOrigin
@RestController
@RequestMapping("/rst")
public class RestaurantController {
    @Autowired 
    RestaurantService restaurantService;


    //모든 정보 조회
    @GetMapping(value = "/all")
    public Object getAllReview(){
        List<RestaurantEntity> allRst = restaurantService.findAll();
        return new ResponseEntity<List<RestaurantEntity>>(allRst, HttpStatus.OK);
    }

    //레스토랑 등록
    @PostMapping("/reg") 
    public Object rstReg(@RequestBody RestaurantEntity request) {
        System.out.println(request.toString());

        RestaurantEntity rst = new RestaurantEntity(request.getRname(), request.getRbranch(),
                                        request.getRuid(), request.getRphone(), request.getRaddr());
        if(restaurantService.rstSave(rst) == rst) {
            System.out.println("성공");
            return new ResponseEntity<Object>(HttpStatus.OK);
        }
        System.out.println("실패");
        return new ResponseEntity<Object>(HttpStatus.BAD_REQUEST);
    }

    //레스토랑 정보 가져오기
    @GetMapping("/detail")
    public Object getRestaurantInfo(@RequestParam("rid") String rid){
        System.out.println(" rid체크 in Rst Controller : "+rid);
        int ridnum = Integer.parseInt(rid);

        Optional<RestaurantEntity> result = restaurantService.getRestaurantInfo(ridnum);

        
        System.out.println(result.toString());
        return new ResponseEntity<Object>(result, HttpStatus.OK);
    }

    @GetMapping("/list")
    public ResponseEntity<List<RestaurantEntity>> getRestaurantList(@RequestParam("uid") String uid){
        // System.out.println("사용자의 아이디: "+uid);

        List<RestaurantEntity> result = null;

        if(!uid.equals("undefined") && uid!=null){
            result = restaurantService.getRestaurantList(uid);
            //System.out.println(result.get(0).getRname());
            return new ResponseEntity<List<RestaurantEntity>>(result, HttpStatus.OK);
        } else {
            return new ResponseEntity<List<RestaurantEntity>>(result, HttpStatus.BAD_REQUEST);
        }
    }

    //레스토랑 수정
    @PostMapping(value="/mod")
    public Object MenuMod(@RequestBody RestaurantEntity request) {
        //request.setRid(rid);;
        System.out.println("rst/mod 레스토랑 수정" + request.getRname()+ "주소 "+request.getRaddr());
        return restaurantService.Modrst(request);
    }

    //레스토랑 삭제
    @GetMapping("/del") 
    public Object rstDel(@RequestParam int rid) {
        System.out.println("rst/del 삭제 레스토랑 번호: "+rid);
        return restaurantService.Delrst(rid);
    }
}//end of class
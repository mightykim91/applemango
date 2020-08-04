package com.project.controller.user;

import java.util.List;

import javax.servlet.http.HttpSession;
import javax.validation.Valid;
import javax.validation.constraints.Min;

import com.project.model.user.UserEntity;
import com.project.model.user.FavorEntity;
import com.project.model.Review;
import com.project.service.user.*;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@CrossOrigin
@RestController
@RequestMapping("/user")
@Validated
public class UserController {

    
    private UserService userService;
    private FavorService favorService;


    public UserController(UserService userService){
        this.userService = userService;
    }

    @PostMapping("/")
    public Object add(@RequestBody @Valid UserEntity param){
        return "hello";
    }

    // @PostMapping("/add")
    // public Object add(@RequestBody @Valid UserEntity param){
    //     userService.add(param);
    //     return null;
    // }


    @GetMapping("/login")
    public Object userLogin(@RequestParam("uid")String uid,@RequestParam("upw") String upw, HttpSession session){
       
        return userService.login(uid,upw,session);
    }

    @GetMapping("/logout")
    public Object userLogout(HttpSession session){
       
        return session.toString();
    }

    @GetMapping(value = "/favors/{uid}")
    public Object getFavorByUserId(@PathVariable String uid){
        System.out.println("테스트1");
        List<FavorEntity> favors = favorService.getFavorsByUid(uid);
        System.out.println("테스트3");
        return 0;
        //return new ResponseEntity<List<FavorEntity>>(favors, HttpStatus.OK);
    }



    // @PutMapping("/edit/{seq}")
    // public Object edit(@RequestBody @Valid UserEntity param, @PathVariable("seq") @Min(1) String uid){
    //     param.setSeq(seq);
    //     userService.edit(param);
    //     return null;
    // }

    // @GetMapping("/{seq}")
    // public Object getUserOne(@RequestParam(required = true) final String email,@RequestParam(required = true) final String password){
    //     return userService.login(uid);
    // }

    // @GetMapping("/all")
    // public Object getUserAll(){
    //     return userService.getAll();
    // }

    // @DeleteMapping("/{seq}")
    // public Object delete(@PathVariable("seq") @Min(1) Long seq){
    //     userService.delete(seq);
    //     return null;
    // }
}

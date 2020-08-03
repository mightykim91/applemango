package com.project.controller.restaurant;

import java.util.List;

import com.project.model.restaurant.Menu;
import com.project.service.restaurant.MenuService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
@CrossOrigin
@RestController
@RequestMapping("/menu")
public class MenuController {
    @Autowired 
    MenuService menuService;

    //레스토랑 메뉴 등록하기
    @PostMapping("/reg")
    public Object MenuReg(@RequestBody Menu menu){
        System.out.println(menu.getMid());
        
        Menu menutmp = new Menu(menu.getMid(), menu.getMrid(), menu.getMissig(), menu.getMname(), menu.getMprice(), menu.getMimage());
        if(menuService.regMenu(menutmp) == menutmp) {
            System.out.println("성공");
            return new ResponseEntity<Object>(HttpStatus.OK);
        }
        System.out.println("실패");
        return new ResponseEntity<Object>(HttpStatus.BAD_REQUEST);
    }

    //레스토랑 메뉴 가져오기
    @GetMapping("/list")
    public ResponseEntity<List<Menu>> MenuList(@RequestParam int mrid){
        // int mrid = Integer.parseInt(strmrid);
        // System.out.println("mrid:"+mrid);
        System.out.println("메뉴리스트도달");
        List<Menu> result = menuService.listMenu(mrid);
        System.out.println("List 개수:"+ result.size());

        return new ResponseEntity<List<Menu>>(result, HttpStatus.OK);
    }

    //메뉴 상세 조회하기
    @GetMapping("/detail")
    public Object MenuDetail(@RequestParam String mname){
        Object tmp = menuService.detailMenu(mname);
        if(tmp!=null){
            return new ResponseEntity<Object>(HttpStatus.OK);
        } else return new ResponseEntity<Object>(HttpStatus.BAD_REQUEST);
    }
}
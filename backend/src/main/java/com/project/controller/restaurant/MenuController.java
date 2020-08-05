package com.project.controller.restaurant;

import java.util.List;

import com.project.model.restaurant.MenuEntity;
import com.project.service.restaurant.MenuService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
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
    public Object MenuReg(@RequestBody MenuEntity menu){

        System.out.println("menu/reg 레스토랑 번호:" + menu.getMrid());
        System.out.println(menu.toSring());
        MenuEntity menutmp = new MenuEntity(menu.getMrid(), menu.getmissig(), menu.getMname(), menu.getMprice(), menu.getMimage());
        if(menuService.regMenu(menutmp) == menutmp) {
            System.out.println("성공");
            return new ResponseEntity<Object>(HttpStatus.OK);
        }
        System.out.println("실패");
        return new ResponseEntity<Object>(HttpStatus.BAD_REQUEST);
    }

    //레스토랑 메뉴 가져오기
    @GetMapping("/list")
    public ResponseEntity<List<MenuEntity>> MenuList(@RequestParam int mrid){
        //System.out.println("menu/list 도달");
        List<MenuEntity> result = menuService.listMenu(mrid);
        //System.out.println("menu/list return List 개수:"+ result.size());

        return new ResponseEntity<List<MenuEntity>>(result, HttpStatus.OK);
    }

    //메뉴 수정
    @PostMapping(value="/mod")
    public Object MenuMod(@RequestParam int mid, @RequestBody MenuEntity menu) {
        menu.setMid(mid);
        System.out.println("menu/mod 레스토랑 번호:" + menu.getMrid()+ "메뉴번호:" + mid);
        return menuService.modMenu(menu);
    }

    //메뉴 삭제
    @GetMapping(value="/del")
    public Object MenuDel(@RequestParam int mid) {
        System.out.println("menu/del 메뉴 번호: "+ mid);
        return menuService.delMenu(mid);
    }
}
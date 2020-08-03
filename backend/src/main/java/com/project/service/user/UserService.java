package com.project.service.user;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Repository;
import org.springframework.stereotype.Service;

import javax.persistence.EntityManagerFactory;
import javax.persistence.PersistenceContext;
import javax.persistence.PersistenceUnit;
import javax.servlet.http.HttpSession;
import javax.transaction.Transactional;
import java.lang.Object;
import com.project.dao.user.UserDAO;
import com.project.model.UserEntity;

import io.swagger.annotations.ApiResponse;
import io.swagger.annotations.ApiResponses;
import io.swagger.annotations.ApiOperation;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

import java.util.Enumeration;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

@Service
public class UserService {

    @Autowired
    UserDAO userDAO;


    // @Autowired
    // SessionFactory sf;


    public Object login(final String uid, final String upw, final HttpSession session) {

        final Optional<UserEntity> user = userDAO.findByUidAndUpw(uid, upw);

        ResponseEntity response = null;
        final ResponseBody result = new ResponseBody();

        if (user.isPresent()) {

            result.status = true;
            result.data = "success";

            user.ifPresent(u -> {
                System.out.println("email : " + u.getUemail());
                session.setAttribute("user", u);
                session.setAttribute("uid", u.getUid());
                session.setAttribute("upw", u.getUpw());
                session.setAttribute("uemail", u.getUemail());
                result.object = session.getAttribute("user");

            });
            response = new ResponseEntity<>(result, HttpStatus.OK);
        } else {
            response = new ResponseEntity<>("로그인 실패", HttpStatus.OK);
        }

        final Enumeration se = session.getAttributeNames();

        while (se.hasMoreElements()) {
            final String getse = se.nextElement() + "";
            System.out.println("@@@@@@@ session : " + getse + " : " + session.getAttribute(getse));
        }

        // session.setAttribute("user",user);

        // Session session = sf.getCurrentSession();
        // session.persist(user);

        System.out.println("리스판스" + result.object);
        return response;
    }

    public Object logout(final HttpSession session) {

        session.invalidate();

        return session;
    }


  
}


class ResponseBody {
    
    public boolean status = false;
    public String data;
    public Object object;
}

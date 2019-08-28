package com.example.jvmshare.memery;


import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

/**
 * @author r2dxxc
 */
@Slf4j
@RestController
@RequestMapping(value = "/gc", produces = MediaType.APPLICATION_JSON_VALUE)
public class OutOfMemeryController {

    private Map leafMap = new HashMap();
    private Map leafMapSimple = new HashMap();



    @PostMapping(value = "/outOfMemerySimple/{id}")
    public ResponseEntity<String> outOfMemerySimple(@PathVariable String id) {

        byte[] bytes = new byte[1024*1024];
        leafMapSimple.put(id, bytes);
        System.out.println("hello");
        log.info("outOfMemerySimple called; Id: {} and leafMap.size: {} ",id, leafMapSimple.size());
        log.debug(" debug outOfMemerySimple called; Id: {} and leafMap.size: {} ",id, leafMapSimple.size());
        return ResponseEntity.status(HttpStatus.CREATED).body("Map size :"+leafMapSimple.size());
    }

    @PostMapping(value = "/addMemerySimple/{id}")
    public ResponseEntity<String> addMemerySimple(@PathVariable String id) {

        byte[] bytes = new byte[1024*1024];
        ArrayList<byte[]> arrayListSimple = new ArrayList<> ();
        arrayListSimple.add(bytes);
        log.info("addMemerySimple called; Id: {} and arrayListSimple.size: {}.",id,arrayListSimple.size());
        log.debug("debug outOfMemerySimple called; Id: {} and leafMap.size: {} ",id, arrayListSimple.size());
        return ResponseEntity.status(HttpStatus.CREATED).body("Map size :"+arrayListSimple.size());
    }


    @PostMapping(value = "/outOfMemery/{id}")
    public ResponseEntity<String> outOfMenery(@PathVariable String id) {
        MemVo vo = new MemVo();
        vo.setBytes(new Byte[1024*1024*10]);
        leafMap.put(id, vo);
        log.info("outOfMenery called; Id: {} and leafMap.size: {} ",id, leafMap.size());
        return ResponseEntity.status(HttpStatus.CREATED).body("Map size :"+leafMap.size());
    }

    @PostMapping(value = "/addMemery/{id}")
    public ResponseEntity<String> addMemery(@PathVariable String id) {
        MemVo vo = new MemVo();
        vo.setBytes(new Byte[1024*1024*10]);
        ArrayList<MemVo> arrayList = new ArrayList<> ();
        arrayList.add(vo);
        log.info("addMemery called; Id: {} and leafMap.size: {}.",id,arrayList.size());
        return ResponseEntity.status(HttpStatus.CREATED).body("Map size :"+arrayList.size());
    }


}

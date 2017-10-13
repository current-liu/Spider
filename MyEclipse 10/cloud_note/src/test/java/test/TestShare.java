package test;

import java.io.IOException;

import org.junit.Before;
import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import note.dao.ShareDao;
import note.entity.Share;


public class TestShare {
	private ApplicationContext ac;	
	private ShareDao dao;
	
	@Before
	public void init() throws IOException{
		ac = new ClassPathXmlApplicationContext("spring-mvc.xml");		
		dao = ac.getBean("shareDao",ShareDao.class);
		//System.out.println(dao);
	}
	@Test
	public void test1(){
		Share share = dao.findById("1787211c-26b5-4cc3-92be-0ad55df51113");
		System.out.println(share);
	}

}

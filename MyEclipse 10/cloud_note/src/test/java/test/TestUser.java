package test;

import java.io.IOException;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import note.dao.UserDao;
import note.entity.User;

public class TestUser {
	private ApplicationContext ac;	
	private UserDao dao;
	@Before
	public void init() throws IOException{
		ac = new ClassPathXmlApplicationContext("spring-mvc.xml");		
		dao = ac.getBean("userDao",UserDao.class);
		//System.out.println(dao);
	}
	
	@After
	public void destroy(){
		
	}
//	@Test
//	public void test1() throws IOException{
//		SqlSessionFactoryBuilder ssfb = new SqlSessionFactoryBuilder();
//		//将主配置文件转成reader流
//		String conf = "SqlMapConfig.xml";
//		Reader reader = Resources.getResourceAsReader(conf);
//		//加载reader流创建SqlSessionFactory
//		SqlSessionFactory ssf = ssfb.build(reader);
//		//利用Factory获取SqlSession
//		SqlSession session = ssf.openSession();
//		//UserDao dao = session.getMapper(UserDao.class);
//		User u= dao.findByName("caocao");
//		System.out.println(u);
//		
//	}

	@Test 
	public void test1(){
		User u = dao.findByName("demo");
		System.out.println(u);
	}
	@Test
	public void test2(){
		User u = dao.findById("3");
		System.out.println(u);
	}
	@Test
	public void test3(){
		User u = new User();
		u.setCn_user_name("beibei");
		u.setCn_user_password("1234");
		u.setCn_user_nick("k");
		dao.regist(u);
		System.out.println(u.getCn_user_id());
	}
	

}

package test;

import java.io.IOException;
import java.util.List;

import org.junit.Before;
import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import note.dao.AssociationDao;
import note.entity.NoteBook;
import note.entity.User;


public class TestAssociation {
	private ApplicationContext ac;	
	private AssociationDao dao;
	
	@Before
	public void init() throws IOException{
		ac = new ClassPathXmlApplicationContext("spring-mvc.xml");		
		dao = ac.getBean("associationDao",AssociationDao.class);
		
	}
	@Test
	public void test(){
		User u = dao.findUser("1");
		System.out.println(u);
		
	}
	@Test
	public void test1(){
		List<User> list = dao.findAll();
		for(User u : list){
			System.out.println(u.getCn_user_name());
			List<NoteBook> books = u.getBooks();
			for(NoteBook b : books){
				System.out.println(b.getCn_notebook_name());
			}			
		}
	}
	@Test
	public void test2(){
		List<NoteBook> list = dao.findAllBooks();
		
		for(NoteBook b : list){
			System.out.println(b.getCn_notebook_id()+" "+b.getCn_notebook_name());
			User u = b.getUser();
			System.out.println(u.getCn_user_id()+" "+u.getCn_user_name());
		}
	}

}

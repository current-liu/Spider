package test;

import java.io.IOException;
import java.sql.Timestamp;
import java.util.List;

import org.junit.Before;
import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import note.dao.NoteBookDao;
import note.entity.NoteBook;


public class TestNoteBook {
	private ApplicationContext ac;	
	private NoteBookDao dao;
	
	@Before
	public void init() throws IOException{
		ac = new ClassPathXmlApplicationContext("spring-mvc.xml");		
		dao = ac.getBean("noteBookDao",NoteBookDao.class);
		
	}
	
	@Test
	public void test1(){
		List<NoteBook> list = dao.findByUserId("1");
		System.out.println(list);
	}
	@Test
	public void test2(){
		NoteBook noteBook = new NoteBook();
		noteBook.setCn_notebook_id("10");	
		noteBook.setCn_notebook_name("@Test");
		noteBook.setCn_user_id("1");
		noteBook.setCn_notebook_type_id("5");
		noteBook.setCn_notebook_createtime(new Timestamp(System.currentTimeMillis()));
		noteBook.setCn_notebook_desc("@Test");
		dao.addBook(noteBook);
	}
	@Test
	public void test3(){
		NoteBook noteBook = dao.findById("1");
		System.out.println(noteBook);
		
	}
	
	

}

package test;

import java.io.IOException;
import java.sql.Timestamp;
import java.util.List;
import java.util.Map;

import org.junit.Before;
import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;


import note.dao.NoteDao;
import note.entity.Note;

public class TestNote {

	private ApplicationContext ac;	
	private NoteDao dao;
	
	@Before
	public void init() throws IOException{
		ac = new ClassPathXmlApplicationContext("spring-mvc.xml");		
		dao = ac.getBean("noteDao",NoteDao.class);
		
	}
	
	@Test
	public void test1(){
		Map<String,String> m = dao.findById("1");
		System.out.println(m);
	}
	@Test
	public void test2(){
		List<Map<String,String>> list = dao.findByBookId("1");
		System.out.println(list);
	}
	@Test
	public void test3(){
		Note note = new Note();
		note.setCn_note_id("1");
		note.setCn_note_title("updated");
		note.setCn_note_body("updated");
		dao.updateNote(note);
	}
	@Test
	public void test4(){
		Note note = new Note();			
		note.setCn_note_id("1");			
		Timestamp time = new Timestamp(System.currentTimeMillis());
		note.setCn_note_last_modify_time(time);
		dao.updateStatusBin(note);
	}
	@Test
	public void test5(){
		dao.updateStatusBin1("2");
	}
}

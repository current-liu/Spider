package note.service;

import java.sql.Timestamp;
import java.util.List;

import javax.annotation.Resource;

import org.springframework.stereotype.Service;

import note.dao.NoteBookDao;
import note.entity.NoteBook;
import note.uitl.NoteResult;
import note.uitl.NoteUtil;
@Service
public class NoteBookServiceImpl implements NoteBookService {
	@Resource
	private NoteBookDao bookDao;
	public NoteResult loadBooks(String userId) {
		List<NoteBook> list = bookDao.findByUserId(userId);
		NoteResult result = new NoteResult();
		result.setStatus(0);
		result.setMsg("查询笔记成功");
		result.setData(list);		
		return result;
	}
	
	public NoteResult addBook(String bookName, String userId) {
		NoteResult result = new NoteResult();
		NoteBook book = new NoteBook();
		book.setCn_notebook_name(bookName);
		book.setCn_user_id(userId);
		book.setCn_notebook_type_id("5");
		String bookId = NoteUtil.createId();
		book.setCn_notebook_id(bookId);
		book.setCn_notebook_createtime(new Timestamp(System.currentTimeMillis()));
		book.setCn_notebook_desc("");
		bookDao.addBook(book);
		result.setStatus(0);
		result.setMsg("创建笔记本成功");
		result.setData(bookId);//返回笔记本Id		
		return result;
	}

	public NoteResult deleteBook(String bookId) {
		NoteResult result = new NoteResult();
		bookDao.deleteBook(bookId);
		result.setStatus(0);
		result.setMsg("删除笔记成功");
		result.setData(bookId);		
		return result;
	}
}

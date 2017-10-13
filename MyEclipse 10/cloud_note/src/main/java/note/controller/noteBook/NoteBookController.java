package note.controller.noteBook;

import javax.annotation.Resource;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;


import note.service.NoteBookService;
import note.uitl.NoteResult;

@Controller
@RequestMapping("/noteBook")
public class NoteBookController {
	
	@Resource
	private NoteBookService noteBookService;
	
	@RequestMapping("/loadBooks.do")
	@ResponseBody
	public NoteResult loadBooks (String userId){
		//System.out.println(userId);
		NoteResult result = noteBookService.loadBooks(userId);
		return result;
	}
	@RequestMapping("/addBook.do")
	@ResponseBody
	public NoteResult addBook(String bookName,String userId){
		NoteResult result = noteBookService.addBook(bookName, userId);
		return result;
	}
	@RequestMapping("/deleteBook.do")
	@ResponseBody
	public NoteResult deleteBook (String bookId){
		//System.out.println(userId);
		NoteResult result = noteBookService.deleteBook(bookId);
		return result;
	}
	

}

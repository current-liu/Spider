package note.controller.note;

import javax.annotation.Resource;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import note.service.NoteBookService;
import note.service.NoteService;
import note.uitl.NoteResult;

@Controller
@RequestMapping("/note")
public class NoteController {
	
	@Resource
	private NoteService noteService;
	@Resource
	private NoteBookService noteBookService;
	
	@RequestMapping("/hightSearch.do")
	@ResponseBody
 	public NoteResult hightSearch(String title, String status, String begin, String end){
		if(begin!=null && !"".equals(begin)){
			System.out.println(begin);
		}
		NoteResult result = noteService.hightSearch(title, status, begin, end);
		System.out.println("hightSearch:"+result.getData());
		return result;
		
	}
	
	@RequestMapping("/loadNotes.do")
	@ResponseBody
 	public NoteResult loadNotes(String bookId){
		System.out.println("bookId:"+bookId);
		NoteResult result = noteService.loadNotes(bookId);
		System.out.println("loadNotes:"+result.getData());
		return result;
		
	}
	@RequestMapping("/loadNote.do")
	@ResponseBody
	public NoteResult loadNote(String noteId){
		System.out.println("noteId:"+noteId);
		NoteResult result = noteService.loadNote(noteId);
		System.out.println("loadNote:"+result);
		return result;
	}
	@RequestMapping("/addNote.do")
	@ResponseBody
	public NoteResult addNote(String noteTitle, String noteBody,String bookId, String userId){
		//System.out.println("noteTitle:"+noteTitle);
		NoteResult result = noteService.addNote(noteTitle, noteBody,bookId, userId);
		System.out.println("addNote:"+result);
		return result;
	}
	@RequestMapping("/updateNote.do")
	@ResponseBody
	public NoteResult updateNote(String noteId,String noteTitle,String noteBody){
		NoteResult result = noteService.updateNote(noteId, noteTitle, noteBody);
		return result;
	}
	@RequestMapping("/deleteNote.do")
	@ResponseBody
	public NoteResult deleteNote(String noteId){
		System.out.println("noteId:"+noteId);
		NoteResult result = noteService.deleteNote(noteId);
		System.out.println("deleteNote:"+result);
		return result;
	}
	@RequestMapping("/updateStatusBin.do")
	@ResponseBody
	public NoteResult updateStatusBin(String noteId){
		System.out.println("noteId:"+noteId);
		NoteResult result = noteService.updateStatusBin(noteId);
		System.out.println("updateStatusBin:"+result);
		return result;
	}
	@RequestMapping("/replayNote.do")
	@ResponseBody
	public NoteResult replayNote(String noteId,String bookId){
		System.out.println("noteId:"+noteId);
		NoteResult result = noteService.updateStatusNormal(noteId,bookId);		
		System.out.println("updateStatusNormal:"+result);
		return result;
	}
	@RequestMapping("/updateBookId.do")
	@ResponseBody
	public NoteResult updateBookId(String noteId,String bookId){
		System.out.println("noteId:"+noteId+",bookId:"+bookId);
		NoteResult result = noteService.updateBookId(noteId,bookId);
		System.out.println("updateBookId:"+result);
		return result;
	}
	@RequestMapping("/loadBin.do")
	@ResponseBody
	public NoteResult loadBin(String userId){
		NoteResult result = noteService.loadBin(userId);
		return result;
	}
	

}

package note.controller.user;

import java.security.NoSuchAlgorithmException;

import javax.annotation.Resource;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import note.service.UserService;
import note.uitl.NoteResult;

@Controller
@RequestMapping("/user")
public class UserController {
	
	@Resource
	private UserService userService;
	
	@RequestMapping("/login.do")
	@ResponseBody
	public NoteResult execute(String name,String password) throws NoSuchAlgorithmException{
		System.out.println(name+password);
		NoteResult result = userService.checkLogin(name, password);
		System.out.println(result);
		return result;
	}
	
	@RequestMapping("/regist.do")
	@ResponseBody
	public NoteResult execute(String name,String password,String nick) throws NoSuchAlgorithmException{
		NoteResult result = userService.regist(name, password, nick);
		return result;
	}
	@RequestMapping("/checkName.do")
	@ResponseBody
	public NoteResult execute(String name) throws NoSuchAlgorithmException{
		NoteResult result = userService.checkName(name);
		return result;
	}

}

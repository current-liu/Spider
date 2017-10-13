package note.service;

import java.security.NoSuchAlgorithmException;

import javax.annotation.Resource;

import org.springframework.stereotype.Service;

import note.dao.UserDao;
import note.entity.User;
import note.uitl.NoteResult;
import note.uitl.NoteUtil;

@Service("userService")
public class UserServiceImpl implements UserService {
	
	@Resource(name="userDao")
	private UserDao userDao;
	private NoteResult result = new NoteResult();
	
	
	public NoteResult checkLogin(String name, String password) throws NoSuchAlgorithmException {
		//用户名和密码检查
		User user = userDao.findByName(name);
		if(user==null){
			result.setStatus(1);
			result.setMsg("用户不存在");
			//result.setData("用户不存在");
			return result;
		}
		//将用户输入的密码加密
		String md5_pwd = NoteUtil.md5(password);
		if(!user.getCn_user_password()
				.equals(md5_pwd)){
			result.setStatus(2);
			result.setMsg("密码不正确");
			//result.setData();
			return result;
		}
		result.setStatus(0);
		result.setMsg("登录成功");
        result.setData(user.getCn_user_id());
		return result;			
	}
	public NoteResult regist(String name,String password,String nick) throws NoSuchAlgorithmException{
		//System.out.println(name+password+nick);		
		password = NoteUtil.md5(password);
		User u = new User();
		u.setCn_user_name(name);
		u.setCn_user_password(password);
		u.setCn_user_nick(nick);
		userDao.regist(u);
		result.setStatus(0);
		result.setMsg("注册成功，请登录");
		return result;
		
	}
	public NoteResult checkName(String name){
		User user = userDao.findByName(name);
		if(user==null){
			result.setStatus(0);
			result.setMsg("用户名可用");			
			return result;
		}else {
			result.setStatus(1);
			result.setMsg("用户名已存在");
			return result;
		}
		
	}

}

package note.service;

import java.security.NoSuchAlgorithmException;

import note.uitl.NoteResult;

public interface UserService {
	public NoteResult checkLogin(String name,String password) throws NoSuchAlgorithmException;
	public NoteResult regist(String name,String password,String nick) throws NoSuchAlgorithmException;
	public NoteResult checkName(String name);
}

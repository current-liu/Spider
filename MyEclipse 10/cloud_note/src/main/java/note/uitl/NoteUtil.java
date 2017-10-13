package note.uitl;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.UUID;

import org.apache.commons.codec.binary.Base64;

public class NoteUtil {
	public static String md5(String msg) throws NoSuchAlgorithmException{
		//利用md5对msg处理
		MessageDigest md = MessageDigest.getInstance("MD5");
		byte[]	input = msg.getBytes();
		byte[]	output = md.digest(input);
		//将md5处理的output结果转成字符串
		String result = Base64.encodeBase64String(output);
		return result;
		
	}
	/**
	 * 生成主键值
	 * @return 主键值
	 */
	public static String createId(){
		UUID uuid = UUID.randomUUID();
		return uuid.toString();
	}
	
	public static void main(String[] args) throws NoSuchAlgorithmException {
		System.out.println(md5("1234"));
//		System.out.println(md5("123456"));
//		System.out.println(md5("12354654676dfdfdfdf"));
		System.out.println(createId());
		System.out.println(createId());
	}

}

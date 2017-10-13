package note.aspect;

import java.io.FileWriter;
import java.io.PrintWriter;

import org.aspectj.lang.annotation.AfterThrowing;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.springframework.stereotype.Component;

@Component
@Aspect
public class NoteLogger {
	public void clogger(){
		System.out.println("进入controller...");
	}
	@Before("within(note.service..*)")
	//名称限定表达式:匹配note.service包及子包中所有类所有方法
	public void slogger(){
		System.out.println("进入Service...");
	}
	@Before("execution(* note.service.UserService.checkLogin(..))")
	//类型限定表达式:匹配note.service.UserService类中checkLogin()方法
	public void loginLogger(){
		System.out.println("进入userService.checkLogin()...");
	}
	@AfterThrowing(throwing="e",pointcut="within(note.cntroller..*)")
	public void exceptionControllerLogger(Exception e){
		System.out.println("记录controller异常信息："+e);
	}
	@AfterThrowing(throwing="e",pointcut="within(note.service..*)")
	public void exceptionServiceLogger(Exception e){
		System.out.println("记录service异常信息："+e);
		try {
			FileWriter fw = new FileWriter("D:\\error.txt");
			PrintWriter out = new PrintWriter(fw);
			//out.println("记录service异常信息：");
			e.printStackTrace(out);
		} catch (Exception ex) {
			System.out.println("记录异常信息失败");
		}
		
	}
	

}

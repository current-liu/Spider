/**
 * Copyright &copy; 2012-2016 <a href="https://github.com/thinkgem/jeesite">JeeSite</a> All rights reserved.
 */
package com.thinkgem.jeesite.modules.demo.entity;

import org.hibernate.validator.constraints.Length;

import com.thinkgem.jeesite.common.persistence.DataEntity;

/**
 * 班级表管理Entity
 * @author liuchao
 * @version 2017-05-12
 */
public class DemoClasses extends DataEntity<DemoClasses> {
	
	private static final long serialVersionUID = 1L;
	private String name;		// 班级
	
	public DemoClasses() {
		super();
	}

	public DemoClasses(String id){
		super(id);
	}

	@Length(min=1, max=1000, message="班级长度必须介于 1 和 1000 之间")
	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}
	
}
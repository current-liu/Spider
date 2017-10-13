$('section .option li').eq(3).addClass('active');
$('.download').mouseover(function(){
    $(this).find('.topline').stop().animate({'width':'100%'},300);
    $(this).find('.rightline').stop().animate({'height':'100%'},300);
    $(this).find('.bottomline').stop().animate({'width':'100%'},300);
    $(this).find('.leftline').stop().animate({'height':'100%'},300);
});
$('.download').mouseout(function(){
    $(this).find('.topline').stop().animate({'width':'0'},300);
    $(this).find('.rightline').stop().animate({'height':'0'},300);
    $(this).find('.bottomline').stop().animate({'width':'0'},300);
    $(this).find('.leftline').stop().animate({'height':'0'},300);
});
	
var spiderId = localStorage.getItem("spiderId");
if(spiderId = "null"){
	spiderId = "6";
}

//下载文档
function DownLoadFile(){
	document.getElementById("pf").href="document.docx";
    $("#fp").click();
}

//爬虫信息展示
$.ajax({
	url:url_head + "get_spider",
	type:"get",
	data: {"id":spiderId},
	async:true,
	dateType:"json",
	success:function(result){
		console.log(result);
		var spidername = $('aside .list li').children('.main').children('.mainone').children('.left');
		spidername.text(result[0].fields.name);
		var spidersite = $('aside .list li').children('.main').children('.mainone').children('.right').children('a');
		spidersite.text('目标站点:'+result[0].fields.target_site);
		spidersite.attr({"title":result[0].fields.target_site});
		var spiderlocation = $('aside .list li').children('.main').children('.mainone').children('.right').children('p');
		spiderlocation.text('目标位置:'+result[0].fields.loc);
	},
	error:function(XMLHttpRequest, textStatus, errorThrown) {
        console.log(XMLHttpRequest.status);
        console.log(XMLHttpRequest.readyState);
        console.log(textStatus);
    }
});

//日历
(function(){
  var dateObj = (function(){
    var _date = new Date();    // 默认为当前系统时间
    return {
      getDate : function(){
        return _date;
      },
      setDate : function(date) {
        _date = date;
      }
    };
  })();
 
  // 设置calendar div中的html部分
  renderHtml();
  // 表格中显示日期
  showCalendarData();
  // 绑定事件
  bindEvent();
 
  /**   * 渲染html结构   */
  function renderHtml() {
    var calendar = document.getElementById("calendar");
    var titleBox = document.createElement("div");  // 标题盒子 设置上一月 下一月 标题
    var bodyBox = document.createElement("div");  // 表格区 显示数据
 
    // 设置标题盒子中的html
    titleBox.className = 'calendar-title-box';
    titleBox.innerHTML = "<span class='prev-month' id='prevMonth'></span>" +
      "<span class='calendar-title' id='calendarTitle'></span>" +
      "<span id='nextMonth' class='next-month'></span>";
    calendar.appendChild(titleBox);    // 添加到calendar div中
 
    // 设置表格区的html结构
    bodyBox.className = 'calendar-body-box';
    var _headHtml = "<tr>" + 
              "<th>日</th>" +
              "<th>一</th>" +
              "<th>二</th>" +
              "<th>三</th>" +
              "<th>四</th>" +
              "<th>五</th>" +
              "<th>六</th>" +
            "</tr>";
    var _bodyHtml = "";
 
    // 一个月最多31天，所以一个月最多占6行表格
    for(var i = 0; i < 6; i++) {  
      _bodyHtml += "<tr>" +
              "<td></td>" +
              "<td></td>" +
              "<td></td>" +
              "<td></td>" +
              "<td></td>" +
              "<td></td>" +
              "<td></td>" +
            "</tr>";
    }
    bodyBox.innerHTML = "<table id='calendarTable' class='calendar-table'>" +
              _headHtml + _bodyHtml +
              "</table>";
    // 添加到calendar div中
    calendar.appendChild(bodyBox);
  }
 
  /**   * 表格中显示数据，并设置类名   */
  function showCalendarData() {
    var _year = dateObj.getDate().getFullYear();
    var _month = dateObj.getDate().getMonth() + 1;
    var _dateStr = getDateStr(dateObj.getDate());
 
    // 设置顶部标题栏中的 年、月信息
    var calendarTitle = document.getElementById("calendarTitle");
    var titleStr = _dateStr.substr(0, 4) + "年" + _dateStr.substr(4,2) + "月";
    calendarTitle.innerText = titleStr;
 
    // 设置表格中的日期数据
    var _table = document.getElementById("calendarTable");
    var _tds = _table.getElementsByTagName("td");
    var _firstDay = new Date(_year, _month - 1, 1);  // 当前月第一天
    for(var i = 0; i < _tds.length; i++) {
      var _thisDay = new Date(_year, _month - 1, i + 1 - _firstDay.getDay());
      var _thisDayStr = getDateStr(_thisDay);
      _tds[i].innerText = _thisDay.getDate();
      //_tds[i].data = _thisDayStr;
      _tds[i].setAttribute('data', _thisDayStr);
      if(_thisDayStr == getDateStr(new Date())) {    // 当前天
        _tds[i].className = 'currentDay';
      }else if(_thisDayStr.substr(0, 6) == getDateStr(_firstDay).substr(0, 6)) {
        _tds[i].className = 'currentMonth';  // 当前月
      }else {    // 其他月
        _tds[i].className = 'otherMonth';
      }
    }
  }
 
  /**   * 绑定上个月下个月事件   */
  function bindEvent() {
    var prevMonth = document.getElementById("prevMonth");
    var nextMonth = document.getElementById("nextMonth");
    addEvent(prevMonth, 'click', toPrevMonth);
    addEvent(nextMonth, 'click', toNextMonth);
    
    //点击表格中日期时候的事件
    var table = document.getElementById("calendarTable");
	  var tds = table.getElementsByTagName('td');
	  for(var i = 0; i < tds.length; i++) {
	  	addEvent(tds[i], 'click', function(e){
	  		var dateArr = e.target.getAttribute('data');
	  		console.log(spiderId);
		    
		    var date1 = dateArr.substring(4,0);
		    var date2 = dateArr.substring(4);
		    var date3 = date2.substring(2,0);
		    var date4 = date2.substring(2);
		    var date = date1 + "-" + date3 + "-" + date4;
		    console.log(date);
		    
		    $.ajax({
					url:url_head + "get_spiderstatus_on_day",
					type:"get",
					data: {"id":1, 'date':date},
					async:true,
					dateType:"json",
					success:function(result){
						console.log(result);
						console.log(result[0]);
						console.log(result[0].fields);
						$('.maintwo-right').text(result);
						
					},
					error:function(XMLHttpRequest, textStatus, errorThrown) {
				        console.log(XMLHttpRequest.status);
				        console.log(XMLHttpRequest.readyState);
				        console.log(textStatus);
				    }
				});
		    
		  });
	  }
  }
 
  /**   * 绑定事件   */
  function addEvent(dom, eType, func) {
    if(dom.addEventListener) {  // DOM 2.0
      dom.addEventListener(eType, function(e){
        func(e);
      });
    } else if(dom.attachEvent){  // IE5+
      dom.attachEvent('on' + eType, function(e){
        func(e);
      });
    } else {  // DOM 0
      dom['on' + eType] = function(e) {
        func(e);
      }
    }
  }
 
  /**   * 点击上个月图标触发   */
  function toPrevMonth() {
    var date = dateObj.getDate();
    dateObj.setDate(new Date(date.getFullYear(), date.getMonth() - 1, 1));
    showCalendarData();
  }
 
  /**   * 点击下个月图标触发   */
  function toNextMonth() {
    var date = dateObj.getDate();
    dateObj.setDate(new Date(date.getFullYear(), date.getMonth() + 1, 1));
    showCalendarData();
  }
 
  /**   * 日期转化为字符串， 4位年+2位月+2位日   */
  function getDateStr(date) {
    var _year = date.getFullYear();
    var _month = date.getMonth() + 1;    // 月从0开始计数
    var _d = date.getDate();
     
    _month = (_month > 9) ? ("" + _month) : ("0" + _month);
    _d = (_d > 9) ? ("" + _d) : ("0" + _d);
    return _year + _month + _d;
  }
  
  
  
  
  
//var table = document.getElementById("calendarTable");
//var tds = table.getElementsByTagName('td');
//console.log(tds);
//for(var i = 0; i < tds.length; i++) {
//		var html = "<div id='linshi' style='width:60px;height:60px;'></div>";
//		$('.currentMonth').eq(i).append(html);
//		var myChartContentMiddle = echarts.init(document.getElementById('linshi'));
//		myChartContentTopoption = {
//		    tooltip : {
//		        trigger: 'item',
//		        formatter: "{b} : {c} ({d}%)"
//		    },
//		    series : [
//		        {
//		            name: '',
//		            type: 'pie',
//		            radius : '55%',
//		            center: ['50%', '45%'],
//		            label: {
//	                normal: {
//	                    show: false,
//	                    position: 'center'
//	                },
//	                emphasis: {
//	                    show: false,
//	                    textStyle: {
//	                        fontSize: '30',
//	                        fontWeight: 'bold'
//	                    }
//	                }
//		            },
//		            data:[
//		                {value:25, name:'run'},
//		                {value:10, name:'pause'},
//		                {value:5, name:'error'}
//		            ],
//		            itemStyle: {
//		                emphasis: {
//		                    shadowBlur: 10,
//		                    shadowOffsetX: 0,
//		                    shadowColor: 'rgba(0, 0, 0, 0.5)'
//		                }
//		            }
//		        }
//		    ]
//		};
//		myChartContentMiddle.setOption(myChartContentTopoption);
//
//}
  

  
  
})();


//爬虫运行情况分析图
$.ajax({
	url:url_head +"get_operation_time_last_n_days",
	type:"get",
	data: {"id":spiderId, "n":"7"},
	async:true,
	dateType:"json",
	success:function(result){
		console.log(result);
		var dateArr = [];
		var runArr = [];
		var otherArr = [];
		for(i=0;i<result.length;i++){
			var dateObj = result[i].date;
			dateArr.push(dateObj);
			var runObj1 = result[i].operation_time.operation_time_seconds;
			var runObj;
			if(Number.isInteger(runObj1)){
				runObj = runObj1/3600
			}else{
				runObj = (runObj1/3600).toFixed(2)
			}
			runArr.push(runObj1);
			var otherObj1 = result[i].operation_time.leisure_seconds;
			var otherObj;
			if(Number.isInteger(otherObj1)){
				otherObj = otherObj1/3600
			}else{
				otherObj = (otherObj1/3600).toFixed(2)
			}
			otherArr.push(otherObj);			
		}
		console.log(dateArr);
		console.log(runArr);
		console.log(otherArr);


		var myChartMainFour = echarts.init(document.getElementById('mainfour'));
		var myChartMainFouroption = {
			tooltip : {
		        trigger: 'axis',
		        axisPointer : {
		            type : 'shadow'
		        }
		    },
		    legend: {
		        data: ['运行时间', '非运行时间']
		    },
		    grid: {
		        left: '3%',
		        right: '4%',
		        bottom: '3%',
		        containLabel: true
		    },
		    xAxis:  {
		        type: 'value'
		    },
		    yAxis: {
		        type: 'category',
		        data: dateArr
		    },
		    series: [
		        {
		            name: '运行时间',
		            type: 'bar',
		            stack: '总量',
		            label: {
		                normal: {
		                    show: true,
		                    position: 'insideLeft'
		                }
		            },
		            data: runArr
		        },
		        {
		            name: '非运行时间',
		            type: 'bar',
		            stack: '总量',
		            label: {
		                normal: {
		                    show: true,
		                    position: 'insideRight'
		                }
		            },
		            data: otherArr
		        }
		    ]
		};
		myChartMainFour.setOption(myChartMainFouroption);
	
	}
});
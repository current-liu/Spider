var url_head = "http://192.168.1.150:8000/manager/";

$('section').hover(function(){
	$(this).stop().animate({width:'160px'},500);
	$('section header').stop().animate({width:'160px'},500);
	$('section .option li').stop().animate({width:'160px'},500);
},function(){
	$(this).stop().animate({width:'60px'},500);
	$('section header').stop().animate({width:'60px'},500);
	$('section .option li').stop().animate({width:'60px'},500);
	}
);

var html = "";
	html+="<div class='fixed'><header><svg class='icon' aria-hidden='true'><use xlink:href='#icon-icons64x6479'></use></svg><span>Web Spider</span></header><ul class='option'><li><a href='Home.html'><svg class='icon' aria-hidden='true'><use xlink:href='#icon-quanbu2'></use></svg><span>Home</span></a></li><li><a href='Total.html'><svg class='icon' aria-hidden='true'><use xlink:href='#icon-quanbu1'></use></svg><span>Total</span></a></li><li><a href='List.html'><svg class='icon' aria-hidden='true'><use xlink:href='#icon-biaoge'></use></svg><span>List</span></a></li><li><a href='Info.html'><svg class='icon' aria-hidden='true'><use xlink:href='#icon-box'></use></svg><span>Info</span></a></li><li><a href='Run.html'><svg class='icon' aria-hidden='true'><use xlink:href='#icon-process'></use></svg><span>Run</span></a></li></ul></div>";
	html+="";
$('section').append(html);

//$('aside header .icon').click(function(){
//	$('section').stop().animate({width:'160px'},500);
//	$('section header').stop().animate({width:'160px'},500);
//	$('section .option li').stop().animate({width:'160px'},500);
//},function(){
//		$('section').stop().animate({width:'60px'},500);
//		$('section header').stop().animate({width:'60px'},500);
//		$('section .option li').stop().animate({width:'60px'},500);
//	}
//);
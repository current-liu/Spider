/**
 * Created by Administrator on 2017/9/1 0001.
 */
function fun(){
    var id = 1
    $.ajax({
        url:schema_url+'/ajax',
        type:'GET',
        data:{"id":id},
        dataTpye:"json",
        success:function(res){
            console.log(res)
        },
        error:function(XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }
    })
}



function get_dp_shops(){
    var id = 1
    $.ajax({
        url:schema_url+'/get_dp_shops',
        type:'GET',
        data:{"id":id},
        dataTpye:"json",
        success:function(res){
            console.log(res)
        },
        error:function(XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }
    })
}
function get_dp_shops(){
    var id = 1
    $.ajax({
        url:schema_url+'/get_dp_shops',
        type:'GET',
        data:{"id":id},
        dataTpye:"json",
        success:function(res){
            console.log(res)
        },
        error:function(XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }
    })
}


function get_dp_star() {
    n = 1
    $.ajax({
        url: schema_url + '/get_dp_star',
        type: 'GET',
        data:{"star" : n},
        dataTpye: "json",
        success: function (res) {
            console.log(res)
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }
    })
}



function selete_shop_all_star() {
    n = 1
    $.ajax({
        url: schema_url + '/selete_shop_all_star',
        type: 'GET',
        data:{"all_star" : n},
        dataTpye: "json",
        success: function (res) {
            console.log(res)
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }
    })
}
function selete_shop_all() {
    n = 1
    $.ajax({
        url: schema_url + '/selete_shop_all',
        type: 'GET',
        data:{"all" : n},
        dataTpye: "json",
        success: function (res) {
            console.log(res)
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }
    })
}
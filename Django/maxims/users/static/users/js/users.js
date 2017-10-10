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



function get_or_favorite() {
    n = 6
    $.ajax({
        url: schema_url + '/get_or_favorite',
        type: 'GET',
        data:{"id" : n},
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

function get_or_location() {
    n = 6
    $.ajax({
        url: schema_url + '/get_or_location',
        type: 'GET',
        data:{"id" : n},
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

function get_dp_location() {
    n = 6
    $.ajax({
        url: schema_url + '/get_dp_location',
        type: 'GET',
        data:{"id" : n},
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

function get_ta_location() {
    n = 6
    $.ajax({
        url: schema_url + '/get_ta_location',
        type: 'GET',
        data:{"id" : n},
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

function get_mfw_location() {
    n = 6
    $.ajax({
        url: schema_url + '/get_mfw_location',
        type: 'GET',
        data:{"id" : n},
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
function get_all_memberNum() {
    n = 6
    $.ajax({
        url: schema_url + '/get_all_memberNum',
        type: 'GET',
        data:{"id" : n},
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
function get_all_sex() {
    n = 6
    $.ajax({
        url: schema_url + '/get_all_sex',
        type: 'GET',
        data:{"id" : n},
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

function get_dp_province() {
    n = 6
    $.ajax({
        url: schema_url + '/get_dp_province',
        type: 'GET',
        data:{"id" : n},
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

function get_mfw_province() {
    n = 6
    $.ajax({
        url: schema_url + '/get_mfw_province',
        type: 'GET',
        data:{"id" : n},
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
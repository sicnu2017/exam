// JavaScript Document
$(document).on("click", "#btnGoon",function(e){
    if (e && e.preventDefault) {
        e.preventDefault();
    }else{
        e.returnValue = false;
    }
    var href=$(this).attr("href");
    var url="../../templates/exam/"+href+".html";
    $.get(url).done(function(response){
        $("#content").html(response);
    });
})

$(document).on("click", "#btnStart",function(e){
    if (e && e.preventDefault) {
        e.preventDefault();
    }else{
        e.returnValue = false;
    }
    var href=$(this).attr("href");
    var url="../../templates/exam/"+href+".html";
    $.get(url).done(function(response){
        $("#content").html(response);
    });
})

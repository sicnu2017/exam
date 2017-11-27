$(document).on("click", "#allgradeLink",function(e){
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

$(document).on("click", "#gradeLink",function(e){
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
$(document).on("click", "#returnGrade",function(e){
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
$(document).on("click", "#turnGrade",function(e){
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

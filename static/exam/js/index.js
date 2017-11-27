/**
 * Created by Wang on 2017/10/28.
 */
/*学生界面的导航*/
var studentNav=[
    {"icon":"kaoshi","content":"考试","link":"exam"},
    {"icon":"chengjichaxun","content":"成绩查询","link":"grade-search"},
    {"icon":"ICON","content":"个人信息维护","link":"update-info"}];

/*教师界面的导航*/
var teacherNav=[
    {"icon":"plus-itembank","content":"试题库","link":"item-bank"},
    {"icon":"jiaoxuebankaoshishezhi","content":"考试设置","link":"setExam"},
    {"icon":"yuejuanmokuai","content":"阅卷","link":"marking"},
    {"icon":"chengjitongji","content":"成绩统计","link":"grade-count"},
    {"icon":"ICON","content":"个人信息设置","link":"update-info"}];
/*var managerNav=[
 {"icon":"","content":"用户管理"},
 {"icon":"","content":"组织管理"},
 {"icon":"","content":"考试计划"},
 {"icon":"","content":"基础数据维护"}
 ]*/

//var userRole="teacher";
    console.log("userRole:"+ userRole);
    if(userRole=="teacher"){
        loadNav(teacherNav);
    }else{
        loadNav(studentNav);
    }
// $(document).ready(function(){
//     $.ajaxSetup({
//         data: {csrfmiddlewaretoken: '{{ csrf_token }}' },
//     });
//点击导航，加载对应功能模块
$(".nav-ul a").click(function(e){
    e.preventDefault();
    $(".nav-ul a").css({"background":"#263238"});
    $(".nav-ul a").removeClass("change");
    $(this).css({"background":"rgba(0,0,0,0.5)","color":"#fff"});
    $(this).addClass("change");
    // var url=$(this).attr("href")+".html";
    var url=$(this).attr("href");
    //动态加载template模块
    //  $.get("/"+url).done(function(response){
    //     $("#content").html(response);
    // });
    $.ajax({
        url: "/login/"+url,
        global: false,
        type: "POST",
        dataType: "html",
        async: false,
        success: function(response) {
            $("#content").html(response);
        }
    })
})

/*----------------------函数封装-----------------------------*/
//加载导航
function loadNav(navArr){
    $(".nav-ul").empty();       //清空所有子节点
    for(var i=0;i<navArr.length;i++){
        var $li = " <li class='nav-item'><a href='"+navArr[i].link+"'><i class='iconfont nav-icon icon-"+navArr[i].icon+"'></i><span>"+navArr[i].content+"</span> <i class='my-icon nav-more'></i></a></li>";
        $(".nav-ul").append($li);
    }
}
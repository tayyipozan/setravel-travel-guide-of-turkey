
$(".visible").on('click',function() {
    var $pwd = $(".pwd");
    if ($pwd.attr('type') == 'password') {
        $pwd.attr('type', 'text');
    } else {
        $pwd.attr('type', 'password');
    }
    
});
$(".revisible").on('click',function() {
    var $repwd = $(".repwd");
    if ($repwd.attr('type') == 'password') {
        $repwd.attr('type', 'text');
    } else {
        $repwd.attr('type', 'password');
    } 
});

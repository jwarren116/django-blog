$.backstretch("/static/blog/img/subway-1600.jpg");
$('.backstretch').css("opacity", 0.2);

function autoScrollTo(elem) {
    var top = $("#" + elem).offset().top - 150;
    $('html:not(:animated),body:not(:animated)').animate({ scrollTop: top }, 500);
}
$.backstretch("/static/blog/img/subway.jpg");
$('.backstretch').css("opacity", 0.4);

function autoScrollTo(elem) {
    var top = $("#" + elem).offset().top - 175;
    $("html, body").animate({ scrollTop: top }, 1000);
}
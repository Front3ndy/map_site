$(document).ready(function(){
    $(".invisible-text").hide();
    $(document).on('click', '.google-show-more-btn', function(){
        var moreLessButton=$(".invisible-text").is(":visible")?"Посмотреть больше":"Посмотреть меньше";
        $(this).text(moreLessButton);
        $(this).parent(".show-more-google").find(".invisible-text").toggle();
        $(this).parent(".show-more-google").find(".visible-text").toggle();
    });
});
$(function() {
  $('.review-more-link-first').click(function() {
    let is_hidden = false;

     if( $(".grid-element").hasClass('hidden') ){
     is_hidden = true;
      $('.review-more-link-first').html('Показать меньше'); }

     $(".grid-element").removeClass('hidden');

     if(!is_hidden){  $('.inv').addClass('hidden');
     $('.review-more-link-first').html('Показать больше');  }
  });
});
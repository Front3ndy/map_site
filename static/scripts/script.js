$(document).ready(function(){
	$('.google-show-more-btn').click(function(){
		$('.show-more-google').toggleClass('hide');	
		if ($('.show-more-google').hasClass('hide')) {
			$('.show-more-google').html('Подробнее');
		} else {
			$('.show-more-google').html('Скрыть');
		}		
		return false;
	});				
});
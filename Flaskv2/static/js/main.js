/* =================================
------------------------------------
	Cloud 83 - Hosting Template
	Version: 1.0
 ------------------------------------ 
 ====================================*/


'use strict';


$(window).on('load', function() {
	/*------------------
		Preloder
	--------------------*/
	$(".loader").fadeOut(); 
	$("#preloder").delay(400).fadeOut("slow");

});

(function($) {
	/*------------------
		Navigation
	--------------------*/
	$('.nav-switch').on('click', function(event) {
		$(this).toggleClass('active');
		$('.header-right').toggleClass('active');
		event.preventDefault();
	});


	/*------------------
		Background Set
	--------------------*/
	$('.set-bg').each(function() {
		var bg = $(this).data('setbg');
		$(this).css('background-image', 'url(' + bg + ')');
	});


	/*------------------
		Hero Slider
	--------------------*/
	$('.hero-slider').owlCarousel({
		loop: true,
		nav: false,
		dots: true,
		mouseDrag: false,
		animateOut: 'fadeOut',
		animateIn: 'fadeIn',
		items: 1,
		autoplay: true
	});

	var dot = $('.hero-slider .owl-dot');
	dot.each(function() {
		var index = $(this).index() + 1;
		if(index < 10){
			$(this).html('0').append(index);
			$(this).append('<span>.</span>');
		}else{
			$(this).html(index);
			$(this).append('<span>.</span>');
		}
	});


	/*------------------
		Video Popup 
	--------------------*/
	$('.video-popup').magnificPopup({
  		type: 'iframe'
	});

	


	/*------------------
		Testimonials 
	--------------------*/
	$('.testimonials-slider').owlCarousel({
		loop: true,
		nav: true,
		navText:['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>'],
		dots: true,
		margin: 128,
		center:true,
		items: 1
	});
	var dot = $('.testimonials-slider .owl-dot');
	dot.each(function() {
		var index = $(this).index() + 1;
		if(index < 10){
			$(this).html('0').append(index);
			$(this).append('<span>.</span>');
		}else{
			$(this).html(index);
			$(this).append('<span>.</span>');
		}
	});



	
	/*------------------
		Accordions
	--------------------*/
	$('.panel-link').on('click', function (e) {
		$('.panel-link').removeClass('active');
		var $this = $(this);
		if (!$this.hasClass('active')) {
			$this.addClass('active');
		}
		e.preventDefault();
	});


	/*------------------
		Circle progress
	--------------------*/
	$('.circle-progress').each(function() {
		var cpvalue = $(this).data("cpvalue");
		var cpcolor = $(this).data("cpcolor");
		var cptitle = $(this).data("cptitle");
		var cpid 	= $(this).data("cpid");

		$(this).append('<div class="'+ cpid +'"></div><div class="progress-info"><h2>'+ cpvalue +'%</h2><p>'+ cptitle +'</p></div>');

		if (cpvalue < 100) {

			$('.' + cpid).circleProgress({
				value: '0.' + cpvalue,
				size: 180,
				thickness: 7,
				fill: cpcolor,
				emptyFill: "rgba(0, 0, 0, 0)"
			});
		} else {
			$('.' + cpid).circleProgress({
				value: 1,
				size: 180,
				thickness: 7,
				fill: cpcolor,
				emptyFill: "rgba(0, 0, 0, 0)"
			});
		}

	});

})(jQuery);


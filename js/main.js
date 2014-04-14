/* custom javascript */
var focusTime = 800;

$( function() {
	$('.image2').css('opacity', 0);
	$('#button2').hide();
	
	$('#button1').click( function(){
		toggleFocus();
		$(this).hide();
		$('#button2').show();
		$('.clickme').hide();
	});
	$('#button2').click( function(){
		toggleFocus();
		$(this).hide();
		$('#button1').show();
		$('.clickme').hide();
	});	
});

function toggleFocus() {
	var img1El = $('.image1');
	var img2El = $('.image2');
	opac1 = img1El.css("opacity");
	opac2 = img2El.css("opacity");
	$('.image1').fadeTo(focusTime, 1 - opac1);
	$('.image2').fadeTo(focusTime, 1 - opac2);
}

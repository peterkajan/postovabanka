/* custom javascript */
var ACTIVITY_TYPES_CNT = 6;

function toggleActivityType(buttonEl, number) {
	check = $('#id_activity_type_' + number);
	check.prop('checked', !check.prop("checked"));
	$('#activity-type-btn-' + number).toggleClass('checked');
}
		
$( function(){
	for (var i = 0; i < ACTIVITY_TYPES_CNT; i++) {
		$('#activity-type-btn-' + i).click($.proxy(toggleActivityType, null, this, i));
	}
});

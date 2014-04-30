/* custom javascript */
var ACTIVITY_TYPES_CNT = 6;
var maxPhotoSize =4; //in MB

function toggleActivityType(buttonEl, number) {
    check = $('#id_activity_type_' + number);
    check.prop('checked', !check.prop("checked"));
    $('#activity-type-btn-' + number).toggleClass('checked');
}

$(function() {
    for (var i = 0; i < ACTIVITY_TYPES_CNT; i++) {
        $('#activity-type-btn-' + i).click($.proxy(toggleActivityType, null, this, i));
    }

    $("form").submit(function(event) {
        $('.progress').show();
    });

    $('#upload-btn').click(function() {

        $('input[type=file]').trigger('click');

    });
    $('input[type=file]').bind('change', function() {
        
        if(this.files[0].size>=1048576*maxPhotoSize)
            {
                
                document.getElementById("photo-div").innerHTML = document.getElementById("photo-div").innerHTML;
                alert("Priložená fotka musí mať menej ako "+maxPhotoSize+" MB. Prosím nahrajte menšiu.");
            }
    });

});

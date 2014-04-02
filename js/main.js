var workpacesWithAcc = [
  'BB', 
  'BD', 
  'BR', 
  'DK', 
  'HU', 
  'KO', 
  'KE', 
  'LE', 
  'LM', 
  'LC', 
  'MT', 
  'MI', 
  'NT', 
  'NZ', 
  'PP', 
  'PO', 
  'PD', 
  'RS', 
  'RO', 
  'RK', 
  'SE',  // presne 90 km tak este uvidime
  'SN', 
  'SP', 
  'TO', 
  'TV', 
  'TN', 
  'VK', 
  'VT', 
  'ZV', 
  'ZH', 
  'ZA', 
]

var indexOf = function(needle) {
    if(typeof Array.prototype.indexOf === 'function') {
        indexOf = Array.prototype.indexOf;
    } else {
        indexOf = function(needle) {
            var i = -1, index = -1;

            for(i = 0; i < this.length; i++) {
                if(this[i] === needle) {
                    index = i;
                    break;
                }
            }

            return index;
        };
    }

    return indexOf.call(this, needle);
};

var checkAcc = function() 
{  
    if ( indexOf.call(workpacesWithAcc,  $('select.workplace').val()) == -1)
    {                                                                               // without accommodation
        $("input.accomCheck").prop('disabled',true);
        $(".accomCheck").addClass("disabled");
        disableAccFields()
    }
    else
    {
        $("input.accomCheck").prop('disabled',false);
        $(".accomCheck").removeClass("disabled");
        checkAccFields()
    }
};
        
var disableAccFields = function()
{
    $( ".accom" ).prop('disabled',true);
    $( ".accom" ).removeClass("error");
    $( ".accom" ).addClass("disabled");
}

var checkAccFields = function() 
{  
    if ( ! $('input.accomCheck').is(':checked') )
    {
        disableAccFields()
    }
    else
    {
        $( ".accom" ).prop('disabled',false);
        $( ".accom" ).removeClass("disabled");
    }
};

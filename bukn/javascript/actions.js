
function close_poplogin()
{
    $("#login_pop").css(
        {
            "z-index": "-1",
            "display": "none"
        }
    );
}

function login()
{
    $.ajax({
        url: '/ajaxlogin/',
        type: 'post',
        data: $('#login_form').serialize(),
        async: false,
        success: function(msg) {
            switch(parseInt(msg)){
            case 0:
                alert('failed');
                break;
            case -1:
                alert('notactive');
                break;
            default:
                window.location = '/user/'+msg+'/';
                break;
            }
        },
        error: function(msg) {
            confirm('kk');
        }
    });
    return false
}
//function change_measure()
//{
//    $('div .measure div').removeClass('mouseover');
//    alert($('input[checked="checked"]')[0]);//.addClass('mouseover');
//    //$('input[checked="checked"]').parent().addClass('mouseover');
//}

//function hide_login()
//{
//        var pop_login_div = document.getElementById("login_pop");
//        pop_login_div.style.display = "none";
//        return;
//}

$(document).ready(
    function (){
        var login_pop = $("#login_pop");
        var username = login_pop.find('input[name="username"]');
        var password = login_pop.find('input[name="password"]');
        var password_text = login_pop.find('input[name="password_text"]');
        $('#login_button').click(function() {
            login_pop.css( { "display": "block", "z-index": "100" });
            username.val('<  your email  >');
            password_text.val('<  your password  >');
            password_text.css('display', '');
            password.css('display', 'none');
            login_pop.find('input').removeClass('gray').addClass('gray_prompt');
        }
    );
    $('#password').focusin(function() {
        password_text.css('display', 'none');
        password.css('display', '').removeClass('gray_prompt').addClass('focus').focus();
    });
    password.blur(function () {
        if ($(this).val() == '') {
            $(this).css('display', 'none');
            password_text.css('display', '');
        } else {
            $(this).removeClass('focus').addClass('gray_prompt');
        }
    });

    var username_state = 0
    username.bind({
        blur: function () {
            if ($(this).val() == '') {
                $(this).val('<  your email  >').removeClass('focus').addClass('gray_prompt');
                username_state = 0;
            } else {
                $(this).removeClass('focus').addClass('gray');
                username_state = 1;
            }
        },
        focus: function () {
            if (username_state == 0) {
                $(this).val('');
            }
            $(this).removeClass('gray_prompt gray').addClass('focus');
            username_state = 1;
        }
    });
    $('#close_pop').click(function () {
        login_pop.css( { "z-index": "-1", "display": "none" });
        username_state = 0;
    });
    }
);


$(document).ready(function() {
            $('#signupLink').click(function(e) {
                e.preventDefault();
                $('#loginCard').hide();
                $('#signupCard').show();
            });

            $('#loginLink').click(function(e) {
                e.preventDefault();
                $('#signupCard').hide();
                $('#loginCard').show();
            });
        });
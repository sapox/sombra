$(function() {
    $('#suma').click(function(e) {
        var minutes = parseInt($('#id_minutes').val());
        $('#id_minutes').val(minutes+1);
    });
    $('#resta').click(function(e) {
        var minutes = parseInt($('#id_minutes').val());
        if(minutes>0){
            $('#id_minutes').val(minutes-1);
        }
    });
    $('#play').click(function(e) {
        e.preventDefault();
        console.log(e);
        var minutes = $('#id_minutes').val();
        setTimeout(function(){
            // sonido}
            var music = new Audio("/static/sounds/pigue.mp3");
            music.play();
            var counter = 0;
            $(music).bind("ended", function() {
                music.play();
                if (counter < 1) {
                    $('#timer_form').submit()
                }
                counter -= 1;
            });

        }, (minutes * 60000));

        // console counter
        var counter = 0;
        setInterval(function() {
            counter += 1;
            $('#id_minutes').val(counter);
        }, 1000)
    })
});

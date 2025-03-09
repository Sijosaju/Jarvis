$(document).ready(function () {
    $('.tlt').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut",
        },
    });
    //siri config
   var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 640,
    height: 200,
    style:'ios9',
    amplitude:'1',
    speed:'0.30',
    autostart:true
  });
  //siri message animation
  $('.siri-message').textillate({
    loop: true,
    sync: true,
    in: {
        effect: "fadeInUp",
        sync:true
    },
    out: {
        effect: "fadeOutUp",
        sync:true
    },
});
//mic event handler
$("#MicBtn").click(function (e) { 
    eel.playAssistantSound()
    $("#Oval").attr("hidden", true);
    $("#SiriWave").attr("hidden", false);

    
});
});

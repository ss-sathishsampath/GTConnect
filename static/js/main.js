(function(){
	main = {};

    $body = $("body");
    $(document).on({
        ajaxStart: function() { $body.addClass("loading");},
        ajaxStop: function() { $body.removeClass("loading"); }
    });


    main.init = function(){        
    }

})();
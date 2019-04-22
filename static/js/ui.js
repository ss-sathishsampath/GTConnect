(function(argument) {
	
	uiHandler = {};

	$("#leftPanelToggleButton").click(function(ev){
		toggleLeftPanel();
	});

	$("#rightPanelToggleButton").click(function(ev){
		toggleRightPanel();
	});


	function toggleLeftPanel(){
		if(globalVars.leftPanelStatus==1){ // left panel open
	    	$("#leftPanel").removeClass('show');
	    	$("#leftPanel").addClass('hide');
					
			$("#leftPanelToggleButton").removeClass('glyphicon-remove-circle');
			$("#leftPanelToggleButton").addClass('glyphicon-menu-hamburger');
			globalVars.leftPanelStatus = 0;
		}else{ // left panel closed
			$("#leftPanel").removeClass('hide');
	    	$("#leftPanel").addClass('show');
			
			$("#leftPanelToggleButton").removeClass('glyphicon-menu-hamburger');
			$("#leftPanelToggleButton").addClass('glyphicon-remove-circle');
			globalVars.leftPanelStatus = 1;
		}
		resizeMainContainer();
	}

	function toggleRightPanel(){
		if(globalVars.rightPanelStatus==1){ // right panel open
	    	$("#rightPanel").removeClass('show');
	    	$("#rightPanel").addClass('hide');
			
			$("#rightPanelToggleButton").removeClass('glyphicon-remove-circle');
			$("#rightPanelToggleButton").addClass('glyphicon-menu-hamburger');
			globalVars.rightPanelStatus = 0;
		}else{ // right panel closed
			$("#rightPanel").removeClass('hide');
	    	$("#rightPanel").addClass('show');
					
			$("#rightPanelToggleButton").removeClass('glyphicon-menu-hamburger');
			$("#rightPanelToggleButton").addClass('glyphicon-remove-circle');
			globalVars.rightPanelStatus = 1;
		}	
		resizeMainContainer();
	}

	function resizeMainContainer(){
		$("#mainContainer").removeClass();
		if(globalVars.rightPanelStatus==1 && globalVars.leftPanelStatus==1){
			$("#mainContainer").addClass('col-md-8');
		}else if(globalVars.rightPanelStatus==0 && globalVars.leftPanelStatus==0){
			$("#mainContainer").addClass('col-md-12');
		}else if(globalVars.rightPanelStatus==0 && globalVars.leftPanelStatus==1){
			$("#mainContainer").addClass('col-md-10');
		}else if(globalVars.rightPanelStatus==1 && globalVars.leftPanelStatus==0){
			$("#mainContainer").addClass('col-md-10');
		}
	}

})()
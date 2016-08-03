module.exports = {
	login: function(){
		casper.then(function() {
    		this.sendKeys('#userid', "test"); 
			this.sendKeys('#password', "testing123"); 			
	    	this.click('button.btn.btn-primary'); 
		});
	},

	logout: function(){
		casper.then(function(){
			casper.waitForSelector('i.fa.fa-user', function() {
				casper.capture('screenshots/funcion_logout/logout1.png');
    			this.click('i.fa.fa-user');
    			casper.capture('screenshots/funcion_logout/logout2.png');
			});			
	        casper.waitForSelector('i#logout.fa.fa-sign-out', function(){
	        	casper.capture('screenshots/funcion_logout/logout3.png');
	        	this.click('i#logout.fa.fa-sign-out');
	        	this.wait(5000); //Sin este wait no se cierra la sesión
	        });	        

	        
		});		
	},

}
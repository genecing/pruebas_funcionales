casper.test.begin('Iniciar sesion con usuario invalido', 2, function suite(test){
	casper.start('http://emod-frontend-qa.internal.tidnode.cl/', function(){
		casper.capture('screenshots/211/login1.png');
		test.assertTitle("EMOD - tidchile", "Emod homepage title is the one expected");
		this.sendKeys('#userid', "usarioinconrrecto");
		this.sendKeys('#password', "testing123");
		casper.capture('screenshots/211/login2.png');
		this.click('button.btn.btn-primary');		
	});
	casper.then(function() {
		casper.waitForSelector('div.alert.alert-danger', function(){
			casper.capture('screenshots/211/login3.png');
			test.assertSelectorHasText('div.alert.alert-danger','Combinación usuario/contraseña incorrecta');
		});
    });

	casper.run(function(){
		test.done();
	});
});
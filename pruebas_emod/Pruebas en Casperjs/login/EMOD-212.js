casper.test.begin('Iniciar sesion con usuario valido contraseña incorrecta', 2, function suite(test){
	casper.start('http://emod-frontend-qa.internal.tidnode.cl/', function(){
		casper.capture('screenshots/212/login1.png');
		test.assertTitle("EMOD - tidchile", "Emod homepage title is the one expected");
		this.sendKeys('#userid', "test"); //usuario valido
		this.sendKeys('#password', "1"); //contraseña incorrecta
		casper.capture('screenshots/212/login2.png');
		this.click('button.btn.btn-primary');		
	});
	casper.then(function() {
		casper.waitForSelector('div.alert.alert-danger', function(){
			casper.capture('screenshots/212/login3.png');
			test.assertSelectorHasText('div.alert.alert-danger','Combinación usuario/contraseña incorrecta');
		});
    });

	casper.run(function(){
		test.done();
	});
});
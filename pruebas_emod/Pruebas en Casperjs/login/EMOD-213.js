casper.test.begin('iniciar sesion con campos en blanco', 2, function suite(test){
	casper.start('http://emod-frontend-qa.internal.tidnode.cl/', function(){
		//Dejar en blanco los campos
		casper.capture('screenshots/213/login0.png');
		this.echo("captura 0");
		test.assertTitle("EMOD - tidchile", "Emod homepage title is the one expected");
		this.echo("obtiene titulo pagina");
		//this.sendKeys('#userid', "test");
		this.click('button.btn.btn-primary');
		
		this.waitForSelector('div.alert.alert-danger', function(){
			this.echo("en waitforselector");
			casper.capture('screenshots/213/login3.png');
			this.echo("captura 3, en waitforselector");
			test.assertSelectorHasText('div.alert.alert-danger','Por favor introduce tu nombre de usuario');
			this.echo("luego de hacer assertSelectorHasText");
		});
		this.echo("Cuando termina el waitforselector");
			
		
	});

	
/*
	casper.waitForSelector('div.alert.alert-danger', function(){
			casper.capture('screenshots/213/login2.png');
			test.assertSelectorHasText('div.alert.alert-danger','Por favor introduce tu nombre de usuario');
	});

	/*casper.then(function(){
		casper.waitForSelector('div.alert.alert-danger', function(){
			casper.capture('screenshots/213/login2.png');
			test.assertSelectorHasText('div.alert.alert-danger','Por favor introduce tu nombre de usuario');
		});
	});

	casper.then(function(){
		this.sendKeys('#userid', "test");
		this.click('button.btn.btn-primary');
		casper.capture('screenshots/213/login3.png');
	});

	casper.then(function(){
		casper.waitForSelector('div.alert.alert-danger', function(){
			casper.capture('screenshots/213/login4.png');
			test.assertSelectorHasText('div.alert.alert-danger','Por favor introduce tu contraseña');
		});
	});*/

	casper.run(function(){
		test.done();
	});
});
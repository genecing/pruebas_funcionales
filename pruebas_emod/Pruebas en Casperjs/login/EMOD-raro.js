casper.options.waitTimeout = 10 * 1000;
casper.test.begin('iniciar sesion con campos en blanco', 2, function suite(test) {
	casper.start('http://emod-frontend-qa.internal.tidnode.cl/');
	// aparece botón login
	casper.waitForSelector('button.btn.btn-primary', function() {
		// se queja de ambos campos vacíos
		casper.waitForSelector('div.alert.alert-danger', function() {
			test.assertSelectorHasText('div.alert.alert-danger','Por favor introduce tu nombre de usuario');
			// se queja de contraseña vacía
			casper.sendKeys('.login-wrap input#userid', "test");
			casper.waitForSelectorTextChange('div.alert.alert-danger', function() {
				test.assertSelectorHasText('div.alert.alert-danger','Por favor introduce tu contraseña');
			});
			casper.click('button.btn.btn-primary');
		});
		casper.click('button.btn.btn-primary');
	});

	casper.run(function(){
		test.done();
	});
});
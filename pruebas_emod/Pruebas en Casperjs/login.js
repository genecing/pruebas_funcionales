var config = require('config.js');
var funciones = require('common.js');

casper.test.begin('prueba', 1, function suite(test){
	casper.start(config.baseURL, function(){
		test.assertTitle("EMOD - tidchile", "Emod homepage title is the one expected");
		casper.capture('screenshots/prueba_login/estado_inicial.png');
		funciones.login();
		funciones.logout();
		casper.capture('screenshots/prueba_login/estado_final.png');
	});

	casper.run(function(){
		test.done();
	});

});

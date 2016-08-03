var config = require('../config.js');
var funciones = require('../common.js');

casper.test.begin("Iniciar sesion con usuario valido", 1, function suite(test){
	casper.start(config.baseURL, function(){
		test.assertTitle("EMOD - tidchile", "Emod homepage title is the one expected");
		funciones.login();	
		funciones.logout();
	});

	casper.run(function(){
		test.done();
	});
});
<?php

require_once('crypto.php');

date_default_timezone_set('America/Chicago');

$username = 'administrator';
$date = date(DateTime::ISO8601);

print "User is $username and Date is $date \n";

$auth = encrypt(json_encode([
	'username' => $username,
	'date' => $date,
	]));

$cookieData = bin2hex($auth);

print "CookieData is $cookieData\n";

?>
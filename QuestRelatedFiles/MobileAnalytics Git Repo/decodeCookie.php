<?php

require_once('crypto.php');

$cookie = '82532b2136348aaa1fa7dd2243da1cc9fb13037c49259e5ed70768d4e9baa1c80b97fee8bda12881f978b87bc49a0053b14348637bec';

$decoded = decrypt(hex2bin($cookie));

print "The contents of the cookie was \n";
print "$decoded \n";

?>
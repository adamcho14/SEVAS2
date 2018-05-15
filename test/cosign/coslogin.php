<?php
  $ret_url = preg_replace ("/^" . preg_quote($_SERVER['SCRIPT_NAME'],'/') . "\?/", '', $_SERVER['REQUEST_URI']);
  $ret_url = preg_replace ("/do=login&?/", '', $ret_url);
  header("Location: $ret_url");
?>

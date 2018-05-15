<?php

  // nacitame infirmacieo JASe, najma odhlasovacie URL
  $cosign_central_logout = "https://login.uniba.sk/logout.cgi";
  $cosign_cookie_name = 'cosign-'.$_SERVER['SERVER_NAME'];
  $cosign_cookie_index = strtr($cosign_cookie_name,'.','_');
  $ret_uri = preg_replace ("/^" . preg_quote($_SERVER['SCRIPT_NAME'],'/') . "/", '', $_SERVER['REQUEST_URI']);

  $ret_url = 'http://' . $_SERVER['SERVER_NAME'];

  if ( ! isset( $_SERVER['HTTPS'] ) || $_SERVER['HTTPS'] == 'off' ) {
    if ( $_SERVER['PORT'] != '80' ) {
      $ret_url .= ':' . $_SERVER['PORT'];
    }
  }

  if(! empty($ret_uri)) $ret_url .= $ret_uri;

  if ( isset ( $_COOKIE[$cosign_cookie_index] ) )
  {
    /*
    * make any local additions here (e.g. expiring local sessions, etc.),
    * but it's important that there be no output on this page.
    */

    setcookie($cosign_cookie_name,"null",1,'/',"");
    setcookie(cosign_auth,"null",1,'/',"");
    setcookie('fe_typo_user',"null",1,'/',"");
    header( "Location: $cosign_central_logout?$ret_url" );
  }
  else
  {
    setcookie(cosign_auth,"null",1,'/',"");
    setcookie('fe_typo_user',"null",1,'/',"");
    header( "Location: $ret_url");
  }
?>

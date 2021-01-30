<?php
  define('FLAG', 'FLAG:19C4{cookie_is_nice}');

  $accts = array(
    'administrator' => 'bmLhVHjius',
    'guest' => 'guest',
  );

  function is_valid($username, $password)
  {
    global $accts;

    return array_key_exists($username, $accts) && $accts[$username] === $password;
  }
?>

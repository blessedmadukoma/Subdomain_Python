<?php

require ('Script.php');
$class=new Script();
$result=$class->subdomainArr();
// print_r($result);

foreach($result as $re){
    print_r($re);
}
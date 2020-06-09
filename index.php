<?php

require ('Script.php');
$class=new Script();
$result=$class->subdomainArr();
// print_r($result);

foreach($result as $re){
    echo "<pre>";
    echo "<a href='".$re['url']."'>".$re['name']."</a>";
    echo "</pre>";
}

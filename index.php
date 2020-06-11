<?php

require ('Script.php');
$class=new Script('jumia.com.ng');
$result=$class->subdomainArr();
// print_r($result);

if (is_array($result)) {
    foreach($result as $re){
        print_r($re);
        echo "<pre>";
        echo "<a href='".$re['url']."'>".$re['name']."</a>";
        echo "</pre>";
    } 
}else{
    echo $result;
}
 

